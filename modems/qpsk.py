"""QPSK cu mapare Gray.

PROPRIETAR: Student 1 (Partea 1).
"""
import numpy as np

from common import dsp
from common.interfaces import Modem


class QPSKModem(Modem):
    name = "QPSK"
    bits_per_symbol = 2

    def map_bits(self, bits):
        # TODO P1: perechi de biti -> (+-1 +-j)/sqrt(2), mapare Gray, energie medie 1.
        # Atentie: bits e uint8, 1 - 2*bits da 255 in loc de -1 -> bits.astype(int)
        raise NotImplementedError

    def modulate(self, bits):
        # TODO P1: map_bits + dsp.tx_filter
        raise NotImplementedError

    def demodulate(self, rx, n_bits):
        # TODO P1: dsp.matched_filter, esantionare la dsp.total_delay() + k*sps,
        # decizie pe semnul lui I si Q, demapare -> exact n_bits biti uint8
        raise NotImplementedError

    def rx_samples(self, rx, n_bits):
        # TODO P1: aceleasi esantioane ca in demodulate, inainte de decizie
        raise NotImplementedError
