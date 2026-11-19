"""Curbele BER teoretice.

PROPRIETAR: Student 4 (Partea 4).
"""
import numpy as np


def theory_ber(name, ebn0_db) -> np.ndarray:
    """BER teoretic pe bit pentru modulatia `name` ("QPSK", "OQPSK", "DPSK").

    TODO P4 (scipy.special.erfc):
      QPSK, OQPSK: 0.5 * erfc(sqrt(Eb/N0))
      DPSK (DBPSK): 0.5 * exp(-Eb/N0)
    cu Eb/N0 in valoare liniara, nu in dB.
    """
    raise NotImplementedError
