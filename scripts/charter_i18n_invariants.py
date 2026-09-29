#!/usr/bin/env python3
"""Check the source-text invariants of the 24 charter language editions.

The English charter (charter/BUDDHIST-AI-CHARTER.md) quotes the Buddha's final
words as trilingual blocks — Pāli · Chinese · Tibetan — and charter/i18n/README.md
promises that every language edition keeps those blocks. This script makes that
promise testable. It does NOT judge the translations themselves (that is for
named human reviewers); it only checks that the quoted source text survived.

Invariants per edition (exit 1 if any fails):
  * the two Pāli quotations appear exactly once each, verbatim;
  * the two Tibetan lines appear (Vayadhammā line twice: preface + closing);
  * the Chinese line appears in every block (twice for 诸行无常, once for 自灯明),
    in one of the accepted script variants: simplified (canonical), traditional
    (zh-TW, ko, vi), or Japanese shinjitai (ja);
  * the closing block's first line (the edition's own rendering) is not just a
    copy of the Chinese line (except the two Chinese editions, where it is the
    same language).

Run:  python3 scripts/charter_i18n_invariants.py
First run 2026-09-29: 9 of 24 editions failed (ar fa id km mn tr had dropped the
Chinese line from all three blocks; ko and vi had replaced it with a Hangul /
Hán-Việt reading; ja had rewritten its last clause in Japanese and used the
Chinese line as its own closing rendering). All fixed the same day; pi's closing,
which paraphrased the Pāli instead of quoting it, was fixed by hand (not a
script-detectable case).
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
I18N = os.path.join(HERE, '..', 'charter', 'i18n')

P1 = '*"Vayadhammā saṅkhārā, appamādena sampādetha."*'
P2 = '*"Attadīpā viharatha attasaraṇā anaññasaraṇā, dhammadīpā dhammasaraṇā anaññasaraṇā."*'
BO1 = '**ལས་སུ་བྱས་པ་ཐམས་ཅད་མི་རྟག་པ་ཡིན། བག་ཡོད་པས་སྒྲུབ་པར་གྱིས་ཤིག**'
BO2 = ('**བདག་ཉིད་མར་མེར་གྱུར་ཅིག། བདག་ཉིད་སྐྱབས་སུ་གྱུར་ཅིག། ཆོས་མར་མེར་གྱུར་ཅིག། '
       'ཆོས་སྐྱབས་སུ་གྱུར་ཅིག། གཞན་ཡང་སྐྱབས་སུ་མ་གྱུར་ཅིག**')
ZH1 = ['诸行无常，当自精勤。', '諸行無常，當自精勤。', '諸行無常、当自精勤。']
ZH2 = ['自灯明，自归依；法灯明，法归依。莫余归依。',
       '自燈明，自歸依；法燈明，法歸依。莫餘歸依。',
       '自灯明、自帰依；法灯明、法帰依。莫余帰依。']
CHINESE_EDITIONS = ('CHARTER.zh-CN.md', 'CHARTER.zh-TW.md')


def check(path):
    t = open(path, encoding='utf8').read()
    name = os.path.basename(path)
    r = []
    if t.count(P1) != 1:
        r.append('pali-1 x%d' % t.count(P1))
    if t.count(P2) != 1:
        r.append('pali-2 x%d' % t.count(P2))
    if t.count(BO1) != 2:
        r.append('bo-1 x%d' % t.count(BO1))
    if t.count(BO2) != 1:
        r.append('bo-2 x%d' % t.count(BO2))
    n1 = sum(t.count('***' + v + '***') for v in ZH1)
    n2 = sum(t.count('***' + v + '***') for v in ZH2)
    if n1 != 2:
        r.append('zh-1 x%d' % n1)
    if n2 != 1:
        r.append('zh-2 x%d' % n2)
    lines = t.split('\n')
    for i, l in enumerate(lines):
        if l.startswith('> ***') and any(v in l for v in ZH1):
            prev = lines[i - 1]
            if any(v in prev for v in ZH1) and name not in CHINESE_EDITIONS:
                r.append('closing rendering duplicates the Chinese line @%d' % (i + 1))
    return name, r


def main():
    files = sorted(glob.glob(os.path.join(I18N, 'CHARTER.*.md')))
    bad = 0
    for f in files:
        name, r = check(f)
        print('%-18s %s' % (name, 'OK' if not r else '; '.join(r)))
        bad += bool(r)
    print('%d editions, %d failing' % (len(files), bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
