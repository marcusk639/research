# Android Release Build Plan

**Goal:** Make `./gradlew bundleRelease` (and a one-command Fastlane equivalent) work for
regroup Android, matching the ease of iOS Archive → Organizer upload.

**Strategy source:** Audit of `regroup/mobile/android/`, `fastlane/`, and existing
`android/app/release/app-release.aab` (built 2026-05-28, 41MB).

**Session model:** Each phase is self-contained and can run in a fresh Claude Code context.

---

## Phase 0: Ground Truth (Read Before Starting Any Phase)

**Confirmed facts — do not re-derive:**

- `regroup/mobile/android/app/build.gradle` already has the full release signing block:
  reads `MYAPP_UPLOAD_STORE_FILE`, `MYAPP_UPLOAD_STORE_PASSWORD`, `MYAPP_UPLOAD_KEY_ALIAS`,
  `MYAPP_UPLOAD_KEY_PASSWORD` via `project.hasProperty()`. No code changes needed.
- `android/app/debug.keystore` — exists (debug builds work fine)
- `android/app/new_upload_certificate.pem` — exists (upload key certificate for Play App Signing reset)
- `android/app/release/app-release.aab` — a signed release AAB exists from 2026-05-28
- `fastlane/Fastfile` — has Android platform block, but only `metadata` and `screenshots` lanes
- `fastlane/Appfile` — `package_name("com.regroup.app")`, `json_key_file("fastlane/google-play-key.json")`
- `fastlane/google-play-key.json` — gitignored (must be obtained from Google Cloud Console)
- No `keystore.properties` file anywhere in the repo
- No `.jks` / `.keystore` file found on disk — **upload keystore is missing**
- `~/.gradle/gradle.properties` has no MYAPP keys

**Known gaps (what's still needed):**

- Upload keystore `.jks` file — must be located or regenerated (Phase 1)
- `fastlane/google-play-key.json` — must be downloaded from Google Cloud Console (Phase 3)

---

## Phase 1: Install Android SDK (Prerequisite — Do This First)

**Estimated time:** 15–30 minutes
**Blocker:** `./gradlew bundleRelease` fails with "SDK location not found" until this is done.
**Human action required:** Download and install Android Studio or SDK command-line tools.

### 1.1 — Check if SDK already exists

```bash
ls ~/Library/Android/sdk 2>/dev/null && echo "SDK found" || echo "SDK MISSING"
which android 2>/dev/null || echo "android CLI not on PATH"
```

If `SDK found`, skip to 1.4.

### 1.2 — Option A: Install via Android Studio (recommended — easiest)

1. Download from https://developer.android.com/studio
2. Move `Android Studio.app` to `/Applications/`
3. Launch it → complete the Setup Wizard (it installs the SDK automatically to `~/Library/Android/sdk`)
4. After setup, SDK is at `~/Library/Android/sdk` — no further configuration needed

### 1.3 — Option B: Command-line tools only (no IDE)

```bash
# Download command-line tools
curl -o ~/Downloads/cmdline-tools.zip \
  "https://dl.google.com/android/repository/commandlinetools-mac-11076708_latest.zip"
mkdir -p ~/Library/Android/sdk/cmdline-tools/latest
unzip ~/Downloads/cmdline-tools.zip -d ~/Library/Android/sdk/cmdline-tools/latest
mv ~/Library/Android/sdk/cmdline-tools/latest/cmdline-tools/* \
   ~/Library/Android/sdk/cmdline-tools/latest/

# Add to PATH (run once, then source)
echo 'export ANDROID_HOME="$HOME/Library/Android/sdk"' >> ~/.zshrc
echo 'export PATH="$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Install required SDK components
sdkmanager --sdk_root="$HOME/Library/Android/sdk" \
  "platforms;android-34" \
  "build-tools;34.0.0" \
  "ndk;23.1.7779620"
```

Accept the license prompts (`y` for each).

### 1.4 — Confirm `local.properties` points to the SDK

```bash
cat ~/dev/recovery-platform/regroup/mobile/android/local.properties
```

Expected content:

```
sdk.dir=/Users/<yourname>/Library/Android/sdk
```

If the file is missing or has the wrong path, create it:

```bash
echo "sdk.dir=$HOME/Library/Android/sdk" \
  > ~/dev/recovery-platform/regroup/mobile/android/local.properties
```

Verify `local.properties` is gitignored:

```bash
grep "local.properties" ~/dev/recovery-platform/regroup/mobile/android/.gitignore \
  || echo "NOT GITIGNORED — add it"
```

If not gitignored:

```bash
echo "local.properties" >> ~/dev/recovery-platform/regroup/mobile/android/.gitignore
```

### 1.5 — Smoke test the SDK

```bash
cd ~/dev/recovery-platform/regroup/mobile/android
./gradlew tasks --no-daemon 2>&1 | head -20
```

Expected: task list prints without "SDK location not found". If you see SDK errors, re-check 1.4.

### 1.6 — Verification checklist

- [ ] `ls ~/Library/Android/sdk/platforms` lists `android-34` (or higher)
- [ ] `ls ~/Library/Android/sdk/build-tools` lists at least one version
- [ ] `cat ~/dev/recovery-platform/regroup/mobile/android/local.properties` shows correct `sdk.dir`
- [ ] `git status ~/dev/recovery-platform/regroup/mobile/android/local.properties` — shows NOTHING (gitignored)
- [ ] `cd ~/dev/recovery-platform/regroup/mobile/android && ./gradlew tasks --no-daemon` exits 0

### 1.7 — Anti-pattern guards

- Do NOT commit `local.properties` — it contains a machine-specific path
- Do NOT install SDK components by specifying `sdk.dir` inside `build.gradle` — use `local.properties` only
- If using Option B and `sdkmanager` throws "Error: Unknown argument --sdk_root", omit the flag; it may auto-detect `$ANDROID_HOME`

---

## Phase 2: Locate or Regenerate the Upload Keystore

**Estimated time:** 15–60 minutes (depends on whether the keystore can be found)
**Prerequisite:** Phase 1 complete (SDK installed)
**Human action required for Path B**

### 2.1 — Path A: Find the existing keystore

Check these locations on the development machine:

```bash
# Common locations
find ~ -name "*.jks" -o -name "regroup*keystore*" -o -name "upload*key*" 2>/dev/null \
  | grep -v "node_modules\|.git\|Pods" | head -20

ls ~/Desktop/ ~/Documents/ ~/Downloads/ 2>/dev/null | grep -i "key\|store\|regroup"

# Check iCloud Drive
ls ~/Library/Mobile\ Documents/com~apple~CloudDocs/ 2>/dev/null | grep -i "key\|regroup"
```

If found, skip to Phase 2.3.

### 2.2 — Path B: Generate a new upload keystore (if original is lost)

> **Important:** Because Play App Signing is enabled, Google holds the actual signing key.
> The upload key is separate — losing it doesn't lose the app. You can reset it via
> Google Play Console → Setup → App integrity → Request key upgrade.
>
> If you reset the upload key in Play Console, `new_upload_certificate.pem` was already
> generated from that reset. Generate a matching new keystore:

```bash
keytool -genkey -v \
  -keystore ~/dev/recovery-platform/regroup/mobile/android/app/regroup-upload.jks \
  -alias regroup-upload \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000 \
  -dname "CN=Regroup,OU=Mobile,O=Recovery Platform,L=Austin,S=TX,C=US"
```

When prompted, set strong passwords and note them — they become `MYAPP_UPLOAD_*` values.

### 2.3 — Create `keystore.properties` (gitignored)

Confirm it is gitignored first:

```bash
grep "keystore.properties" ~/dev/recovery-platform/regroup/mobile/android/.gitignore 2>/dev/null \
  || grep "keystore.properties" ~/dev/recovery-platform/.gitignore 2>/dev/null \
  || echo "NOT GITIGNORED — add it before creating the file"
```

If not gitignored, add it:

```bash
echo "keystore.properties" >> ~/dev/recovery-platform/regroup/mobile/android/.gitignore
```

Create the file:

```bash
cat > ~/dev/recovery-platform/regroup/mobile/android/keystore.properties << 'EOF'
MYAPP_UPLOAD_STORE_FILE=regroup-upload.jks
MYAPP_UPLOAD_STORE_PASSWORD=PASTE_STORE_PASSWORD_HERE
MYAPP_UPLOAD_KEY_ALIAS=regroup-upload
MYAPP_UPLOAD_KEY_PASSWORD=PASTE_KEY_PASSWORD_HERE
EOF
```

### 2.4 — Update `build.gradle` to read from `keystore.properties`

The current signing block uses `project.hasProperty()` — this works when properties are
passed via `-P` flags or `~/.gradle/gradle.properties`. To make it work via the local file,
update the top of `android/app/build.gradle` to load the file automatically.

**Read the file first:**

```bash
head -30 ~/dev/recovery-platform/regroup/mobile/android/app/build.gradle
```

**Add this block at the top of `app/build.gradle` (before `android {`):**

```groovy
// Load signing properties from local keystore.properties (gitignored)
def keystorePropertiesFile = rootProject.file("keystore.properties")
def keystoreProperties = new Properties()
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
}
```

**Update the release `signingConfig` block to use it:**

```groovy
release {
    if (keystorePropertiesFile.exists()) {
        storeFile file(keystoreProperties['MYAPP_UPLOAD_STORE_FILE'])
        storePassword keystoreProperties['MYAPP_UPLOAD_STORE_PASSWORD']
        keyAlias keystoreProperties['MYAPP_UPLOAD_KEY_ALIAS']
        keyPassword keystoreProperties['MYAPP_UPLOAD_KEY_PASSWORD']
    } else if (project.hasProperty('MYAPP_UPLOAD_STORE_FILE')) {
        // CI fallback: properties passed via environment / -P flags
        storeFile file(MYAPP_UPLOAD_STORE_FILE)
        storePassword MYAPP_UPLOAD_STORE_PASSWORD
        keyAlias MYAPP_UPLOAD_KEY_ALIAS
        keyPassword MYAPP_UPLOAD_KEY_PASSWORD
    }
}
```

### 2.5 — Verification checklist

- [ ] `ls ~/dev/recovery-platform/regroup/mobile/android/app/regroup-upload.jks` exists
- [ ] `cat ~/dev/recovery-platform/regroup/mobile/android/keystore.properties` — has real values (not PASTE_*)
- [ ] `grep "keystore.properties" ~/dev/recovery-platform/regroup/mobile/android/.gitignore` returns a match
- [ ] `git status ~/dev/recovery-platform/regroup/mobile/android/keystore.properties` — shows NOTHING (gitignored)
- [ ] `git status ~/dev/recovery-platform/regroup/mobile/android/app/regroup-upload.jks` — shows NOTHING (gitignored)

### 2.6 — Anti-pattern guards

- NEVER commit `keystore.properties` or the `.jks` file
- NEVER commit `MYAPP_UPLOAD_STORE_PASSWORD` or `MYAPP_UPLOAD_KEY_PASSWORD` in plaintext anywhere
- If Path B (new keystore), register the new upload key certificate in Google Play Console before testing a release build

---

## Phase 3: Add Release Build Scripts

**Estimated time:** 10 minutes
**Prerequisite:** Phase 2 (keystore in place)
**Repos touched:** `regroup/mobile`

### 3.1 — Add npm scripts to `package.json`

Read current scripts first:

```bash
python3 -c "import json; d=json.load(open('$HOME/dev/recovery-platform/regroup/mobile/package.json')); [print(k) for k in d['scripts']]"
```

Add these three scripts to the `"scripts"` block in `package.json`:

```json
"build:android:release": "cd android && ./gradlew bundleRelease --no-daemon",
"build:android:apk": "cd android && ./gradlew assembleRelease --no-daemon",
"build:ios:archive": "xcodebuild -workspace ios/rats.xcworkspace -scheme rats -configuration Release archive -archivePath ios/build/rats.xcarchive"
```

> `build:ios:archive` is the iOS equivalent — adds parity so both platforms have a one-command build.

### 3.2 — Test the release build

```bash
cd ~/dev/recovery-platform/regroup/mobile
npm run build:android:release
```

Expected output path: `android/app/build/outputs/bundle/release/app-release.aab`

### 3.3 — Verification checklist

- [ ] `npm run build:android:release` exits with code 0
- [ ] `ls android/app/build/outputs/bundle/release/app-release.aab` exists and is >20MB
- [ ] `grep "build:android:release" package.json` returns a match

### 3.4 — Anti-pattern guards

- Do NOT use `assembleRelease` (produces APK) for Play Store submissions — use `bundleRelease` (produces AAB)
- Do NOT run the release build with `--daemon` in CI — use `--no-daemon`

---

## Phase 4: Add Fastlane Android Release Lane

**Estimated time:** 20 minutes
**Prerequisite:** Phase 3 passing (signed AAB builds cleanly)
**Human action required:** Download `google-play-key.json` from Google Cloud Console

### 4.1 — Get `google-play-key.json`

This is a Google Cloud service account key with Play Developer API access. To obtain it:

1. Go to [Google Play Console](https://play.google.com/console) → Setup → API access
2. Link to a Google Cloud project (or create one)
3. Create a service account with **Release Manager** role
4. Download the JSON key → save as `~/dev/recovery-platform/regroup/mobile/fastlane/google-play-key.json`

Verify it is gitignored:

```bash
grep "google-play-key" ~/dev/recovery-platform/regroup/mobile/.gitignore \
  ~/dev/recovery-platform/regroup/mobile/fastlane/.gitignore 2>/dev/null \
  || echo "NOT GITIGNORED"
```

If not gitignored, add it:

```bash
echo "fastlane/google-play-key.json" >> ~/dev/recovery-platform/regroup/mobile/.gitignore
```

### 4.2 — Add release lane to `fastlane/Fastfile`

Read the current Fastfile first:

```bash
cat ~/dev/recovery-platform/regroup/mobile/fastlane/Fastfile
```

Add the `release` lane inside the existing `platform :android do` block (before the closing `end`):

```ruby
  desc "Build signed release AAB and upload to Play Store internal track"
  lane :release do
    gradle(
      task: "bundle",
      build_type: "Release",
      project_dir: "android/",
      flags: "--no-daemon",
      properties: {
        "android.injected.signing.store.file" => ENV["MYAPP_UPLOAD_STORE_FILE"],
        "android.injected.signing.store.password" => ENV["MYAPP_UPLOAD_STORE_PASSWORD"],
        "android.injected.signing.key.alias" => ENV["MYAPP_UPLOAD_KEY_ALIAS"],
        "android.injected.signing.key.password" => ENV["MYAPP_UPLOAD_KEY_PASSWORD"],
      }
    )
    supply(
      track: "internal",
      aab: "android/app/build/outputs/bundle/release/app-release.aab",
      skip_upload_apk: true,
      skip_upload_screenshots: true,
      skip_upload_metadata: true,
      skip_upload_images: true,
      release_status: "draft"
    )
  end
```

> **Note:** Using `release_status: "draft"` prevents accidental promotion. Change to `"completed"` when ready for automatic internal-track publication.

### 4.3 — Add Fastlane gem to Gemfile

The current `Gemfile` only declares `cocoapods`. Add Fastlane:

```bash
# Read current Gemfile first
cat ~/dev/recovery-platform/regroup/mobile/Gemfile
```

Add `gem 'fastlane'` to the Gemfile, then:

```bash
cd ~/dev/recovery-platform/regroup/mobile && bundle install
```

### 4.4 — Test the lane (dry run)

```bash
cd ~/dev/recovery-platform/regroup/mobile
bundle exec fastlane android release
```

### 4.5 — Verification checklist

- [ ] `bundle exec fastlane android release` exits cleanly
- [ ] AAB appears in Google Play Console → Internal testing → Releases
- [ ] `grep "google-play-key.json" ~/dev/recovery-platform/regroup/mobile/.gitignore` returns a match
- [ ] `git status fastlane/google-play-key.json` — shows NOTHING (gitignored)
- [ ] `grep "release" ~/dev/recovery-platform/regroup/mobile/fastlane/Fastfile | grep "lane"` returns a match

---

## Phase 5: CI Secrets (For Future Automated Releases)

**Estimated time:** 10 minutes setup, build time varies
**Prerequisite:** Phases 2–4 passing locally

Add these GitHub Actions secrets to recovery-platform (Settings → Secrets and variables → Actions):

| Secret name                    | Value                                      |
| ------------------------------ | ------------------------------------------ |
| `MYAPP_UPLOAD_STORE_PASSWORD`  | Store password from `keystore.properties`  |
| `MYAPP_UPLOAD_KEY_ALIAS`       | Key alias (e.g. `regroup-upload`)          |
| `MYAPP_UPLOAD_KEY_PASSWORD`    | Key password from `keystore.properties`    |
| `MYAPP_UPLOAD_KEYSTORE_BASE64` | `base64 -i android/app/regroup-upload.jks` |

The keystore file cannot be stored as a GitHub secret directly (binary) — encode it first:

```bash
base64 -i ~/dev/recovery-platform/regroup/mobile/android/app/regroup-upload.jks | pbcopy
# Paste output as MYAPP_UPLOAD_KEYSTORE_BASE64 secret
```

In a future CI workflow, decode it before the build step:

```yaml
- name: Decode upload keystore
  run: |
    echo "${{ secrets.MYAPP_UPLOAD_KEYSTORE_BASE64 }}" | base64 --decode \
      > regroup/mobile/android/app/regroup-upload.jks
```

This phase is **optional** — local `npm run build:android:release` and `fastlane android release` are sufficient until automated release CI is needed.

---

## Quick Reference: Phase Order and Dependencies

```
Phase 1 (Android SDK)─── No deps — start here (human action required)
Phase 2 (Keystore)   ─── depends on: Phase 1 (SDK must be installed)
Phase 3 (Scripts)    ─── depends on: Phase 2 (keystore must be in place)
Phase 4 (Fastlane)   ─── depends on: Phase 3 + google-play-key.json (human action)
Phase 5 (CI secrets) ─── optional, depends on: Phases 2–4 all passing
```

## Final Verification

Run after all phases complete:

```bash
cd ~/dev/recovery-platform/regroup/mobile

# Phase 1 — SDK
ls ~/Library/Android/sdk/platforms 2>/dev/null && echo "SDK: OK" || echo "SDK: MISSING"

# Phase 2 — Keystore
ls android/app/regroup-upload.jks 2>/dev/null && echo "Keystore: OK" || echo "Keystore: MISSING"
cat android/keystore.properties | grep -v PASSWORD | grep "MYAPP"  # show non-secret lines

# Phase 3 — Release build
npm run build:android:release
ls android/app/build/outputs/bundle/release/app-release.aab && echo "AAB: OK"

# Phase 4 — Fastlane
bundle exec fastlane android release
```
