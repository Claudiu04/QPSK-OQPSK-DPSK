"""Modelul de canal.

PROPRIETAR: Student 4 (Partea 4). PRIORITATE: pe main la finalul saptamanii 1,
pentru ca analizele P2 si P3 depind de el.
"""
import numpy as np


def awgn(x, ebn0_db, n_bits, rng):
    """Adauga zgomot alb gaussian complex pentru un Eb/N0 dat (in dB).

    TODO P4:
      Eb = sum(|x|^2) / n_bits
      N0 = Eb / 10^(ebn0_db / 10)
      zgomot complex cu varianta N0 pe esantion (N0/2 pe I si N0/2 pe Q), generat cu rng
    """
    raise NotImplementedError


def phase_offset(x, deg):
    """Rotire constanta de faza: x * e^(j*phi). TODO P4"""
    raise NotImplementedError


def freq_offset(x, f_norm):
    """Offset de frecventa: x[n] * e^(j*2*pi*f_norm*n), f_norm = delta_f / f_esantionare. TODO P4"""
    raise NotImplementedError
