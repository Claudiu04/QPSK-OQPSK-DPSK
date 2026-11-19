"""DPSK (DBPSK, 1 bit/simbol) cu detectie diferentiala.

PROPRIETAR: Student 3 (Partea 3).
Bonus: o clasa DQPSKModem separata, adaugata in modems/__init__.py cu acordul echipei.
"""
import numpy as np

from common import dsp
from common.interfaces import Modem


class DPSKModem(Modem):
    name = "DPSK"
    bits_per_symbol = 1

    def map_bits(self, bits):
        # TODO P3: codare diferentiala d_k = d_{k-1} XOR b_k, cu un simbol de referinta d_0
        # la inceput -> n_bits + 1 simboluri BPSK (+-1)
        raise NotImplementedError

    def modulate(self, bits):
        # TODO P3: map_bits + dsp.tx_filter
        raise NotImplementedError

    def demodulate(self, rx, n_bits):
        # TODO P3: dsp.matched_filter, esantionare la D + k*sps pentru n_bits + 1 simboluri,
        # z_k = r_k * conj(r_{k-1}), decizie pe semnul lui Re(z_k)
        raise NotImplementedError

    def rx_samples(self, rx, n_bits):
        # TODO P3: esantioanele r_k (constelatia +-1)
        raise NotImplementedError
