// Builds the exam-day reference notes (.docx) for the 21 Oct 2026 C&P exam.
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, HeadingLevel, LevelFormat, BorderStyle, Footer,
  PageNumber,
} = require('docx');

const NAVY = '1F3A5F', AMBER_BG = 'FDF3E1', RED_BG = 'FBEAEA', NAVY_BG = 'E8EEF6', GREY = 'F3F5F7';
const CW = 10512;

const t = (text, o = {}) => new TextRun({ text, font: 'Calibri', size: o.size || 20, bold: o.bold, italics: o.italics, color: o.color });
const p = (runs, o = {}) => new Paragraph({
  children: Array.isArray(runs) ? runs : [t(runs, o)],
  spacing: { after: o.after ?? 80, before: o.before ?? 0 },
  alignment: o.align,
  numbering: o.bullet ? { reference: 'bul', level: 0 } : o.num ? { reference: 'num', level: 0, instance: o.num } : undefined,
  keepNext: o.keepNext,
});
const h1 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [t(text, { size: 28, bold: true, color: NAVY })], spacing: { before: 200, after: 100 }, keepNext: true,
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: NAVY, space: 2 } } });
const h2 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [t(text, { size: 23, bold: true, color: NAVY })], spacing: { before: 160, after: 60 }, keepNext: true });
const bul = (runs) => p(typeof runs === 'string' ? [t(runs)] : runs, { bullet: true, after: 40 });
const b = (s) => t(s, { bold: true });

const border = { style: BorderStyle.SINGLE, size: 4, color: 'BFC8D2' };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(content, width, o = {}) {
  const paras = (Array.isArray(content) ? content : [content]).map(c =>
    c instanceof Paragraph ? c : p(typeof c === 'string' ? [t(c, { bold: o.bold, size: o.size || 19 })] : c, { after: 30 }));
  return new TableCell({ children: paras, width: { size: width, type: WidthType.DXA }, borders,
    shading: o.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: o.fill } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 } });
}
function table(widths, rows, headerFill = NAVY_BG) {
  return new Table({
    width: { size: widths.reduce((a, c) => a + c, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({ cantSplit: true, tableHeader: i === 0,
      children: r.map((c, j) => cell(c, widths[j], i === 0 ? { bold: true, fill: headerFill, size: 18 } : {})) })),
  });
}
function box(fill, paras) {
  return new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [CW],
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({ children: paras, width: { size: CW, type: WidthType.DXA }, borders,
      shading: { type: ShadingType.CLEAR, color: 'auto', fill }, margins: { top: 100, bottom: 100, left: 140, right: 140 } })] })] });
}
const blank = '________________';

const children = [];

// ---------- Title ----------
children.push(new Paragraph({ children: [t('C&P EXAM-DAY NOTES', { size: 34, bold: true, color: NAVY })], spacing: { after: 40 } }));
children.push(p([t('Wednesday 21 Oct 2026 · VES telehealth (video) · Erica attending · Mental disorders / Initial PTSD (MST) · PTSD · MDD · GAD · OCD · SUD secondary', { size: 20 })], { after: 60 }));
children.push(p([b('VES: 877-637-8387   ·   Crisis: 988 then press 1 (or text 838255)   ·   Naloxone within reach')], { after: 120 }));
children.push(box(AMBER_BG, [
  p([b('How to use these notes. '), t('Glance for dates, medication names and your numbers. Don\'t read answers aloud. If asked, say: "I wrote down dates so I\'d get them right." Every line here is a reminder of something already in your record or something you confirmed is true. If anything here is not accurate today, say what IS true.')], { after: 0 }),
]));

// ---------- At the start ----------
children.push(h1('1. In the first two minutes'));
children.push(bul([b('Erica: '), t('"My wife is here; she helps me with daily things and with remembering. Is it okay if she stays — and could she add anything at the end if you want?" If asked to step out → agree.')]));
children.push(bul([b('"How are you?" '), t('Answer truthfully — not "good." Say if you barely slept, are anxious, or if Erica had to get you up / showered / dressed for this call.')]));
children.push(bul([b('Substances: '), t('Be honest about current opioid use, when you last used, and any withdrawal. Mention you are seeking treatment and the steps taken.')]));
children.push(bul([b('Grooming: '), t('If you look put-together because Erica helped, say so — otherwise "adequately groomed" goes in the report.')]));

// ---------- Timeline ----------
children.push(h1('2. Dates (verify against your records)'));
children.push(table([2400, 8112], [
  ['When', 'What'],
  ['05/30/1989', 'DOB (Cherie\'s 1st letter says 1998 / "Kline" — clerical error)'],
  ['~2007 (age 18)', 'Self-reported anxiety/depression treatment; kratom; DUI (expunged); paraphernalia arrest at 20'],
  ['11/23/2009', 'Enlisted USAF — BMT Lackland (Honor Graduate) → Sheppard → Seymour Johnson AFB, 4th EMS, F-15E crew chief (2A333)'],
  ['2011 (records also say 2012)', 'Ankle fracture, Wayne Memorial — morphine, oxycodone'],
  ['Early 2012', 'Harassment by coworker\'s wife begins'],
  ['Summer / mid–late 2012', 'Sexual assault while incapacitated — coworker\'s (civilian) wife. 21-0781 "service member" = ERROR'],
  ['Late 2012', 'Alcohol-related disciplinary action'],
  ['2012–2013', 'Drinking up, insomnia (Ambien/Restoril), withdrew; told Poquette (his statement gives no date) and Reyes ("late 2013")'],
  ['11/22/2013', 'Separated, Honorable (SrA)'],
  ['2013–2015', 'Crash: opioids → benzos, panic, isolation; savings gone ~1 yr; asked Poquette for money'],
  ['09/2015', 'VA Jennings CBOC — denied MST; PTSD screen 0/4'],
  ['2016 / 2017', 'Acadiana inpatient ×2; B.S. Computer Science (McNeese) 12/2016'],
  ['2018', 'Victory detox/residential/IOP (denied trauma at intakes); near job loss; met Erica'],
  ['Jan–Feb 2022', 'Starlite — LEC-5 "unwanted sexual experience"; EMDR; DVT/PE → Eliquis'],
  ['11/2022', 'Married Erica (Jure)'],
  ['2023', 'Starlite Jan + Jul–Aug (OCD F42.2 coded); Cherie Mills, LCSW from 02/06/2023 (CPT); job loss ~6 mo unemployed'],
  ['Jul–Aug 2024', 'Starlite (discharge: "gainfully employed"); TVC claim appointment 8/14/24; 2024 claim denied (records not obtained)'],
  ['Dec 2024', 'LAID OFF → Starlite 12/26/24–1/3/25 (left AMA for remote CTO offer)'],
  ['Apr 2025', 'Ocean\'s Luxury Rehab ~3 wks'],
  ['04/17–05/11/2026', 'Harmony Junction (24 days) → Zoe PHP (left early); FMLA; Recover evals 5/14–15'],
  ['May–Jun 2026', 'Claim received 5/19; DASS-21 6/9 (all Extremely severe); WHODAS 6/11 (~70%); relapse ~early June; Suboxone stopped'],
  ['June 2026', 'PIP / performance → negotiated severance → left software career'],
  ['Jun–Jul 2026', 'Reyes 6/16 · 21-0781 + personal statement 6/17 · Poquette 6/29 · Cherie letter 7/2 (+ updated letter, filed) · Erica 7/12'],
  ['Now', 'Unemployed; using opioids; not in treatment, seeking it. Goff statement never submitted. No sleep study.'],
]));

// ---------- Meds ----------
children.push(h1('3. Diagnoses, treatment, medications'));
children.push(p([b('Diagnosed: '), t('PTSD, MDD, GAD, OCD, SUD (opioid, sedative) — Cherie Mills, LCSW; MDD/GAD also coded at Starlite 2023–24, Harmony 2026, Recover 2026; OCD coded at Starlite Jul–Aug 2023 and Jul–Aug 2024. Recover 5/15 eval mentions PTSD as "childhood trauma and military experiences." Self-reported autism spectrum. F15.20 (amphetamine) at Harmony — if unknown, say so; don\'t invent.')]));
children.push(p([b('Treatment now: '), t('Cherie (last visit: ' + blank + ')  ·  VA / WellMind: ' + blank + '  ·  SUD treatment steps taken: ' + blank)]));
children.push(table([3000, 2000, 2400, 3112], [
  ['Medication', 'Dose', 'Prescriber', 'Taking as prescribed?'],
  ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''],
]));
children.push(p([t('Verify: Eliquis still current? Suboxone stopped June 2026.', { italics: true, size: 18 })]));

// ---------- Frequency worksheet ----------
children.push(h1('4. My real numbers — fill in with Erica before Wednesday'));
children.push(p([t('Use real, current numbers. Typical week AND worst stretch. If you don\'t know, estimate honestly and say it\'s an estimate. Don\'t write a number you can\'t stand behind.', { italics: true, size: 19 })]));
children.push(table([4300, 2400, 3812], [
  ['Symptom / function', 'Typical week', 'Worst stretch (when / how long)'],
  ['Panic attacks — per week; how long each; recovery time', '', ''],
  ['Depressed days in last 14', '', ''],
  ['Suicidal thoughts — how often; passive or active; triggers', '', ''],
  ['Nightmares — nights per week', '', ''],
  ['Sleep — hours per night; awakenings', '', ''],
  ['OCD rituals / checking — hours per day; what they are', '', ''],
  ['Days I left the house (and why; alone or with Erica)', '', ''],
  ['Days I showered / brushed teeth WITHOUT prompting', '', ''],
  ['What Erica does for me (hygiene, clothes, meals, hair, meds, money, appointments) — how often', '', ''],
  ['Anger outbursts — how often; worst recent', '', ''],
  ['Hours per day stuck on the fear of being fired / failing; how sure (0–100%)', '', ''],
  ['Last contact with a friend (who, what, who started it)', '', ''],
  ['AA — times per month; do I speak; anyone I know there', '', ''],
  ['The weekly outing — what, whose idea, what happens after', '', ''],
  ['Current use — what, how much per day, last use', '', ''],
  ['Longest sober period; were nightmares/panic/SI still there?', '', ''],
]));

// ---------- Ten things ----------
children.push(h1('5. The ten things that decide this exam'));
const ten = [
  ['Social prong vs. marriage', 'Say exactly what the marriage is now (caregiving? near-divorce? counseling?) and exactly what exists outside it. AA and the weekly outing: describe precisely, not defensively.'],
  ['ADLs / hygiene', 'Who does what, how often, what happens without Erica. Volunteer it if not asked.'],
  ['Fear of being fired / failing', 'Content, certainty, what evidence does to it, hours per day, what you do because of it (overwork → collapse). Don\'t say "delusion" — let the examiner choose the word.'],
  ['Suicidal ideation', 'Real frequency and nature. "Denies SI" entries = you denied it at intakes to avoid a hold. Answer the attempts/overdose question plainly.'],
  ['Non-disclosure 2015–2024', 'Your own reasons: shame, didn\'t see it as assault, distrust, fear of holds. Stay consistent with your signed statement (told a Starlite therapist in 2022).'],
  ['Active opioid use', 'Honest. Which symptoms persist when sober (if true). The order: assault → symptoms → self-medication. Seeking treatment.'],
  ['Pre-service history', 'Age-18 anxiety/depression, kratom, DUI, arrest, childhood — answer honestly; then the contrast: Honor Grad, functioning, friends → post-2012 change.'],
  ['21-0781 error + Goff', 'She was a coworker\'s wife (civilian as far as you know); "service member" was a mistake. Goff agreed but never sent it.'],
  ['Work read as capacity', '2018 near-loss → 2023 loss → Dec 2024 layoff → June 2026 PIP/severance → left field. The overwork was fear-driven and ended in collapse. Disclose any work you do now.'],
  ['Thin exam', 'Use the last question ("anything else?") to add what was missed.'],
];
children.push(table([400, 2600, 7512], [['#', 'Issue', 'Reminder'], ...ten.map((r, i) => [String(i + 1), r[0], r[1]])]));

// ---------- Tough questions ----------
children.push(h1('6. Tough questions — facts to include, in my own words (only if true)'));
const tq = [
  ['"Why did you deny MST in 2015 and trauma at rehab intakes?"', ['I didn\'t think of what happened as "assault" — male, female perpetrator, shame.', 'Intakes were short, with strangers, and I was there to detox.', 'Saying "trauma" or SI risked a hold; I wanted to get through.', 'My signed statement says I told a Starlite therapist in 2022 (it says "Melissa Robbins"; records say "Robbin Lynch") — what is true about that: ' + blank, 'Worked through it in depth with Cherie (since 2023).', '2022 Starlite LEC-5 — what was true about checking that box: ' + blank]],
  ['"Your records say anxiety/depression and kratom at 18."', ['What exactly happened then (who, how long, how bad): ' + blank, 'How I functioned then: graduated, MEPS, enlisted, BMT Honor Grad.', 'What was new or worse after 2012: nightmares, hypervigilance, shame, panic, SI, the disorder-level drug use.']],
  ['"You denied SI on 5/14 and ~6/25 but wrote \'every day\' on 6/17."', ['My actual pattern: ' + blank, 'I deny it to new providers to avoid involuntary holds (Cherie documented this).']],
  ['"You were \'gainfully employed\' in 2024 and got a CTO offer."', ['Employed mid-2024 — then laid off Dec 2024; June 2026 PIP/severance; then left the field.', 'Overwork was driven by the fear of being fired; it always ended in collapse/relapse/treatment.']],
  ['"You\'re married and go to AA — that\'s social."', ['What Erica does for me day to day, and what I can give back: ' + blank, 'AA: how often, whether I speak, who knows me: ' + blank, 'Friends/family outside the marriage — last real contact: ' + blank]],
  ['"Are your symptoms just the opioids?"', ['Symptoms started after 2012, before the opioid disorder.', 'During sober stretches / residential: ' + blank, 'What using does for me (quiets panic, sleep, numbs memories/fear): ' + blank]],
  ['"Was she a service member?"', ['No — a coworker\'s wife; the 21-0781 entry was an error. Reyes ("wife of a coworker"), Poquette ("one of our friend\'s wife"), my personal statement and CPT worksheet agree.']],
  ['"Who manages your money?"', ['Truthful answer: ' + blank + ' (an honest "Erica does" may lead VA to propose a fiduciary — that\'s okay; never shade it).']],
];
for (const [q, items] of tq) {
  children.push(p([b(q)], { after: 30, keepNext: true }));
  for (const it of items) children.push(bul(it));
}

// ---------- Corrections + do/don't ----------
children.push(h1('7. Small corrections — say calmly if they come up'));
for (const s of [
  'Cherie\'s first letter: DOB 1998 → 1989; "Kline" → Klein; phone number appears two ways.',
  '21-0781 Item 9: "female service member" → coworker\'s (civilian) wife.',
  'Goff: promised on the 21-0781, never submitted.',
  'Ankle date: my statement says May 2011, a 2015 VA note says 2012 — "I believe 2011; my records conflict."',
  'Harmony Junction: 24 days by discharge dates (my statement said 25).',
  '2022 Starlite therapist: my statement says "Melissa Robbins"; Starlite records say "Robbin Lynch, MS, LCDC" — give the name as best I remember.',
  'Reyes\'s form says "4th Maintenance Squadron" — the unit was 4th Equipment Maintenance Squadron.',
]) children.push(bul(s));

children.push(h1('8. Do / Don\'t'));
children.push(table([5256, 5256], [
  ['DO', 'DON\'T'],
  [['Give numbers, durations, consequences', 'Describe a typical day AND a bad day', 'Give a real example from the last month', 'Say "I don\'t remember" when you don\'t', 'Tell the examiner if a panic attack starts; ask for a break', 'Answer every questionnaire item honestly, one at a time', 'Use the "anything else?" question'],
   ['Say "fine" or "good" by reflex', 'Use clinical labels about yourself ("I\'m delusional")', 'Add new assault details not in your filings', 'Contradict records without explaining', 'Exaggerate — or minimize out of pride or loyalty', 'Attend impaired; record the exam; argue if Erica is asked to step out', 'Read answers off this page']],
]));

children.push(h1('9. Before saying goodbye — did I cover…'));
for (const s of [
  'Erica\'s help with hygiene, clothes, meals, hair, meds, money, appointments',
  'That today is not a typical day (if true) and how a bad day looks',
  'Panic / depression / SI / nightmares / OCD with numbers',
  'Every relationship outside the marriage — exactly',
  'Why records say "denies" (SI and trauma)',
  'Symptoms during sober periods; seeking treatment',
  'The work sequence and why I can\'t sustain work now',
  'That Erica can describe what she sees, if the examiner will hear from her',
]) children.push(p([t('☐  ' + s)], { after: 40 }));

children.push(box(NAVY_BG, [p([b('After: '), t('Write the debrief within an hour (topics covered/not covered, questionnaires, length, examiner name). Send it to the VSO. Ask the VSO to pull the DBQ when it posts. Sleep apnea: file an Intent to File (21-0966) if one was never filed.')], { after: 0 })]));
children.push(p([t('Prep material — not evidence; never submit to VA. Not legal or medical advice. Contains personal health information.', { italics: true, size: 16, color: '666666' })], { before: 120 }));

const doc = new Document({
  creator: 'Prepared for Marcus Klein',
  title: 'C&P Exam-Day Notes — 21 Oct 2026',
  styles: { default: { document: { run: { font: 'Calibri', size: 20 } } } },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] },
  ] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 864, bottom: 864, left: 864, right: 864 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
      t('C&P exam-day notes · M. Klein · page ', { size: 16, color: '777777' }),
      new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '777777', font: 'Calibri' }),
    ] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => {
  const out = path.join(__dirname, '..', 'CP-EXAM-DAY-NOTES-2026-10-21.docx');
  fs.writeFileSync(out, buf);
  console.log('docx written', out);
});
