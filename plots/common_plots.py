"""Graficele comune pentru toate modulatiile.

PROPRIETAR: Student 4 (Partea 4).
"""
import matplotlib

matplotlib.use("Agg")   # salveaza PNG-uri fara fereastra (merge si fara display)
import matplotlib.pyplot as plt  # noqa: E402


def plot_ber(curves, out_dir):
    """BER vs Eb/N0 (semilogy): curbele simulate din `curves` {nume: ber_array} + teoria. TODO P4"""
    raise NotImplementedError


def plot_constellations(out_dir):
    """Constelatii (modem.rx_samples) la 3 valori Eb/N0, pentru fiecare modem. TODO P4"""
    raise NotImplementedError


def plot_time_signals(out_dir):
    """Semnalele I/Q in timp pentru fiecare modem. TODO P4"""
    raise NotImplementedError


def plot_psd(out_dir):
    """PSD comparativ (scipy.signal.welch) pentru toate modulatiile. TODO P4"""
    raise NotImplementedError


def plot_all(curves, out_dir):
    """Apelata de main.py. Genereaza toate graficele comune in out_dir."""
    plot_ber(curves, out_dir)
    plot_constellations(out_dir)
    plot_time_signals(out_dir)
    plot_psd(out_dir)
