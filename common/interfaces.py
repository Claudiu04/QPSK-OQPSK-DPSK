"""CONTRACTUL comun pe care il respecta toate modemurile.

Nu se modifica fara acordul tuturor: main.py, simularea si testele
se bazeaza exact pe aceste semnaturi.
"""
from abc import ABC, abstractmethod

import numpy as np

import config


class Modem(ABC):
    name = "BASE"          # "QPSK", "OQPSK", "DPSK"
    bits_per_symbol = 1

    def __init__(self, sps=config.SPS):
        self.sps = sps

    @abstractmethod
    def map_bits(self, bits: np.ndarray) -> np.ndarray:
        """biti uint8 (0/1) -> simboluri complexe, 1 esantion/simbol, energie medie 1."""

    @abstractmethod
    def modulate(self, bits: np.ndarray) -> np.ndarray:
        """biti -> semnal complex in banda de baza, sps esantioane/simbol, filtrat TX."""

    @abstractmethod
    def demodulate(self, rx: np.ndarray, n_bits: int) -> np.ndarray:
        """semnal receptionat -> EXACT n_bits biti uint8 (filtru adaptat + esantionare + decizie)."""

    @abstractmethod
    def rx_samples(self, rx: np.ndarray, n_bits: int) -> np.ndarray:
        """esantioanele complexe dupa filtrul adaptat, la momentele de decizie (pentru constelatie)."""
