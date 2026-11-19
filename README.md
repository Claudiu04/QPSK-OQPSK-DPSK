# Proiect Comunicații de Date – QPSK / OQPSK / DPSK

Un singur simulator Python în care QPSK, OQPSK și DPSK sunt trei modemuri
interschimbabile, cu aceeași interfață (`common/interfaces.py`). Fiecare
student lucrează doar în fișierele lui; `main.py` le rulează automat pe toate.

Planul detaliat (ce are fiecare de făcut, întrebări pentru prezentare,
calendar) e în documentul echipei „Plan proiect CD – QPSK / OQPSK / DPSK în Python”.

## Pornire

```bash
git clone <url-repo>
cd proiect_cd
python -m venv .venv
# Windows: .venv\Scripts\activate    Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt

python main.py     # rulează tot și pune figurile în results/
pytest             # testele de acceptare
```

La început `main.py` raportează toate părțile ca „neimplementat”, iar
`pytest` pică: e normal, testele devin verzi pe măsură ce completați
fișierele.

În PyCharm: deschideți folderul `proiect_cd` ca proiect, setați interpretorul
pe `.venv`, iar la rularea testelor alegeți pytest ca test runner.

## Cine ce face

| Partea | Cine | Fișiere proprii |
| --- | --- | --- |
| 1 – QPSK + filtrul RRC | Student 1 | `common/dsp.py`, `modems/qpsk.py`, `analysis/qpsk_analysis.py`, `tests/test_qpsk.py` |
| 2 – OQPSK | Student 2 | `modems/oqpsk.py`, `analysis/oqpsk_analysis.py`, `tests/test_oqpsk.py` |
| 3 – DPSK | Student 3 | `modems/dpsk.py`, `analysis/dpsk_analysis.py`, `tests/test_dpsk.py` |
| 4 – Canal, simulare, grafice, integrare | Student 4 | `channel/`, `sim/`, `plots/`, `main.py`, `tests/test_integration.py` |

Fișiere **comune** (se schimbă doar de comun acord): `config.py`,
`common/interfaces.py`, `modems/__init__.py`, `tests/test_contract.py`.

Fiecare `TODO` din cod spune exact ce e de implementat acolo.

## Dependențe între părți

- `common/dsp.py` pornește cu un puls dreptunghiular funcțional, deci
  P1, P2 și P3 pot testa loopback-ul din prima zi. Când P1 termină
  `rrc_taps`, schimbă `PULSE = "rrc"` în `config.py` și toți trec pe RRC
  fără să modifice nimic.
- Testele BER și analizele P2/P3 au nevoie de `channel/channel.py` și
  `sim/` de la P4, de aceea P4 le livrează primele (săptămâna 1).

## Când e gata o parte

Un modem poate intra pe `main` când trece **toate** testele din
`tests/test_contract.py` pentru el:

1. loopback fără zgomot: biții ieșiți sunt identici cu cei intrați;
2. `modulate` întoarce `complex`, `demodulate` întoarce `uint8` de lungime exact `n_bits`;
3. simbolurile au energie medie 1;
4. BER-ul simulat la 4 și 6 dB e în ±25% față de teorie.

Rulați doar testele unui modem cu: `pytest -k QPSK` (sau `OQPSK`, `DPSK`).
Atenție: `-k QPSK` prinde și OQPSK; pentru doar QPSK folosiți `pytest -k "QPSK and not OQPSK"`.

## Git

1. Fiecare lucrează pe branch-ul lui: `p1-qpsk`, `p2-oqpsk`, `p3-dpsk`, `p4-sim`.
   ```bash
   git checkout -b p1-qpsk
   # ... lucru ...
   git add <fișierele tale>
   git commit -m "QPSK: map_bits + modulate"
   git push -u origin p1-qpsk
   ```
2. Pull request către `main` doar cu testele voastre trecute local.
3. Student 4 face review și merge. Pentru că nimeni nu atinge fișierele
   altcuiva, merge-urile nu au conflicte.
4. Înainte să începeți ceva nou: `git checkout main && git pull`, apoi
   `git checkout p1-qpsk && git merge main`.

## Capcane cunoscute

- `1 - 2*bits` pe un vector `uint8` dă 255 în loc de −1 → `bits.astype(int)`.
- După filtrul adaptat, simbolul k e la `dsp.total_delay() + k*sps`.
  BER ≈ 0.5 fără zgomot înseamnă aproape sigur index de eșantionare greșit.
- `SPS` trebuie să fie par, iar `N_BITS` multiplu de 2.
- Nu folosiți `np.random.seed` global; primiți `rng` ca parametru.
