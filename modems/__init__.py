"""Registrul modemurilor. main.py si testele ruleaza automat tot ce e aici.

Fisier COMUN: o intrare noua (de ex. DQPSK) se adauga doar cu acordul echipei.
"""
from .qpsk import QPSKModem
from .oqpsk import OQPSKModem
from .dpsk import DPSKModem

MODEMS = {
    "QPSK": QPSKModem,
    "OQPSK": OQPSKModem,
    "DPSK": DPSKModem,
}
