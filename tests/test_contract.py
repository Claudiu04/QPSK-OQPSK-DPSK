"""Testele de acceptare COMUNE: se ruleaza automat pentru fiecare modem din registru.

Un modem e "gata" (poate intra pe main) cand trece toate testele de aici.
Testele BER depind si de channel.awgn si sim.theory (P4).

Fisier COMUN: nu se slabesc pragurile fara acordul echipei.
"""
import numpy as np
import pytest

from channel.channel import awgn
from modems import MODEMS
from sim.theory import theory_ber

N_LOOP = 20_000
N_BER = 200_000


@pytest.fixture
def bits():
    return np.random.default_rng(0).integers(0, 2, N_LOOP, dtype=np.uint8)


@pytest.mark.parametrize("name", list(MODEMS))
def test_loopback_fara_zgomot(name, bits):
    """1. demodulate(modulate(b)) == b, fara zgomot."""
    m = MODEMS[name]()
    out = m.demodulate(m.modulate(bits), len(bits))
    assert np.array_equal(out, bits)


@pytest.mark.parametrize("name", list(MODEMS))
def test_tipuri_si_lungimi(name, bits):
    """2. modulate -> complex; demodulate -> uint8 de lungime exact n_bits."""
    m = MODEMS[name]()
    tx = m.modulate(bits)
    assert np.iscomplexobj(tx)
    out = m.demodulate(tx, len(bits))
    assert out.dtype == np.uint8
    assert len(out) == len(bits)


@pytest.mark.parametrize("name", list(MODEMS))
def test_energie_simboluri(name, bits):
    """Simbolurile din map_bits au energie medie 1."""
    m = MODEMS[name]()
    s = m.map_bits(bits)
    assert np.mean(np.abs(s) ** 2) == pytest.approx(1.0, rel=1e-2)


@pytest.mark.parametrize("name", list(MODEMS))
@pytest.mark.parametrize("ebn0_db", [4, 6])
def test_ber_fata_de_teorie(name, ebn0_db):
    """3. BER simulat in +-25% fata de teorie la 4 si 6 dB."""
    m = MODEMS[name]()
    rng = np.random.default_rng(1)
    b = rng.integers(0, 2, N_BER, dtype=np.uint8)
    rx = awgn(m.modulate(b), ebn0_db, N_BER, rng)
    ber = np.mean(m.demodulate(rx, N_BER) != b)
    th = float(np.asarray(theory_ber(name, ebn0_db)))
    assert abs(ber - th) / th < 0.25, f"{name} @ {ebn0_db} dB: simulat {ber:.2e}, teorie {th:.2e}"
