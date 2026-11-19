"""Simulare Monte Carlo a BER.

PROPRIETAR: Student 4 (Partea 4). PRIORITATE: pe main la finalul saptamanii 1.
"""
import numpy as np

import config
from channel import channel


def ber_point(modem, ebn0_db, phase_deg=0.0, rng=None) -> float:
    """BER-ul unui modem la un singur Eb/N0.

    TODO P4: in blocuri de config.N_BITS:
      biti aleatori cu rng -> modem.modulate -> channel.phase_offset -> channel.awgn
      -> modem.demodulate -> numara erorile;
      te opresti la config.MIN_ERRORS erori sau config.MAX_BITS biti.
    """
    raise NotImplementedError


def ber_curve(modem, ebn0_db_list=config.EBN0_DB, phase_deg=0.0, seed=config.SEED) -> np.ndarray:
    """ber_point pentru fiecare Eb/N0, cu rng = np.random.default_rng(seed). TODO P4"""
    raise NotImplementedError
