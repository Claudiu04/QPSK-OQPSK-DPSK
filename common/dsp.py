"""Functii DSP comune (filtrare TX / filtru adaptat).

PROPRIETAR: Student 1 (Partea 1).

Versiunea de pornire e un PLACEHOLDER functional cu puls dreptunghiular,
ca ceilalti sa poata lucra din ziua 1. Cand rrc_taps e gata, P1 schimba
config.PULSE in "rrc". Semnaturile functiilor raman aceleasi, deci nimeni
altcineva nu trebuie sa modifice nimic.
"""
import numpy as np

import config


def rrc_taps(sps=config.SPS, beta=config.ROLLOFF, span=config.SPAN):
    """Coeficientii filtrului root-raised-cosine, normati la energie unitara.

    TODO P1:
      - numar impar de coeficienti: span * sps + 1, simetric in jurul lui t = 0
      - atentie la cele doua puncte unde numitorul formulei devine 0:
        t = 0 si |t| = T / (4 * beta)
      - la final: h / sqrt(sum(h**2))
    """
    raise NotImplementedError("P1: rrc_taps nu e implementat inca")


def pulse_taps(sps=config.SPS):
    """Filtrul de formare, normat la energie unitara: sum(h**2) == 1."""
    if config.PULSE == "rrc":
        return rrc_taps(sps)
    h = np.ones(sps)
    return h / np.sqrt(np.sum(h ** 2))


def tx_filter(symbols, sps=config.SPS, offset=0):
    """Un simbol la fiecare sps esantioane (intarziat cu offset), apoi filtrare."""
    up = np.zeros(len(symbols) * sps + offset, dtype=complex)
    up[offset::sps][:len(symbols)] = symbols
    return np.convolve(up, pulse_taps(sps))


def matched_filter(rx, sps=config.SPS):
    """Filtrul adaptat la pulse_taps()."""
    h = pulse_taps(sps)
    return np.convolve(rx, np.conj(h[::-1]))


def total_delay(sps=config.SPS):
    """Dupa TX + filtrul adaptat, simbolul k se afla la indexul total_delay() + k*sps."""
    return len(pulse_taps(sps)) - 1
