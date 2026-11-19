"""Parametri comuni ai simulatorului.

Se modifica DOAR de comun acord (anuntati pe grup inainte).
"""
import numpy as np

SPS = 8              # esantioane pe simbol; PAR, OQPSK foloseste SPS // 2
PULSE = "rect"       # "rect" sau "rrc" -> P1 il trece pe "rrc" cand rrc_taps e gata
ROLLOFF = 0.35       # beta pentru RRC
SPAN = 8             # lungimea filtrului RRC, in simboluri
SEED = 42
EBN0_DB = np.arange(0, 11)   # 0..10 dB
N_BITS = 200_000             # multiplu de 2
MIN_ERRORS = 100             # un punct BER se opreste dupa 100 de erori...
MAX_BITS = 5_000_000         # ...sau dupa atatia biti
RESULTS_DIR = "results"
