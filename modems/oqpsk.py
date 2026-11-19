"""OQPSK: QPSK cu componenta Q intarziata cu T/2.

PROPRIETAR: Student 2 (Partea 2).
"""
import numpy as np

import config
from common import dsp
from common.interfaces import Modem


class OQPSKModem(Modem):
    name = "OQPSK"
    bits_per_symbol = 2

    def __init__(self, sps=config.SPS):
        super().__init__(sps)
        assert self.sps % 2 == 0, "OQPSK are nevoie de SPS par (offset = SPS // 2)"

    def map_bits(self, bits):
        # TODO P2: mapare Gray ca la QPSK; I si Q tratate ca doua fluxuri separate.
        # Rescrie maparea aici (nu importa din qpsk.py), ca sa nu depinzi de P1.
        raise NotImplementedError

    def modulate(self, bits):
        # TODO P2: I prin dsp.tx_filter(I, offset=0), Q prin dsp.tx_filter(Q, offset=sps // 2),
        # combinate ca I + jQ (Q iese mai lung cu sps // 2 esantioane -> aliniaza lungimile)
        raise NotImplementedError

    def demodulate(self, rx, n_bits):
        # TODO P2: un singur dsp.matched_filter; I la D + k*sps, Q la D + k*sps + sps // 2,
        # unde D = dsp.total_delay()
        raise NotImplementedError

    def rx_samples(self, rx, n_bits):
        # TODO P2: zI + 1j*zQ, fiecare la momentul lui de decizie
        raise NotImplementedError
