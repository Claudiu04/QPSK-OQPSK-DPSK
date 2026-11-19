"""Punctul de intrare: ruleaza simularea completa si pune toate figurile in results/.

PROPRIETAR: Student 4 (Partea 4).

Merge din prima zi: partile neterminate sunt raportate ca "neimplementat",
iar o parte cu erori nu le blocheaza pe celelalte.
"""
import importlib
import traceback
from pathlib import Path

import config
from modems import MODEMS
from plots import common_plots
from sim.ber import ber_curve

ANALYSES = [
    "analysis.qpsk_analysis",
    "analysis.oqpsk_analysis",
    "analysis.dpsk_analysis",
]


def _try(label, fn, *args):
    """Ruleaza fn(*args); intoarce (rezultat, status) fara sa opreasca programul."""
    try:
        return fn(*args), "OK"
    except NotImplementedError:
        return None, "neimplementat"
    except Exception:
        traceback.print_exc()
        return None, "EROARE (vezi traceback-ul de mai sus)"


def main():
    out_dir = Path(config.RESULTS_DIR)
    out_dir.mkdir(exist_ok=True)
    status = {}

    # 1. curbele BER pentru fiecare modem din registru
    curves = {}
    for name, cls in MODEMS.items():
        ber, status[f"BER {name}"] = _try(name, lambda c=cls: ber_curve(c()))
        if ber is not None:
            curves[name] = ber

    # 2. graficele comune (P4)
    _, status["grafice comune"] = _try("plots", common_plots.plot_all, curves, out_dir)

    # 3. analizele fiecarei parti (P1, P2, P3)
    for mod_name in ANALYSES:
        mod = importlib.import_module(mod_name)
        _, status[mod_name] = _try(mod_name, mod.run, out_dir)

    # 4. rezumat
    print("\n=== Stare proiect ===")
    for what, st in status.items():
        print(f"  {what:<28} {st}")

    if curves:
        print("\n=== BER simulat ===")
        header = "Eb/N0 [dB] " + "".join(f"{n:>12}" for n in curves)
        print(header)
        for i, eb in enumerate(config.EBN0_DB):
            print(f"{eb:>10} " + "".join(f"{curves[n][i]:>12.2e}" for n in curves))

    print(f"\nFigurile sunt in {out_dir.resolve()}")


if __name__ == "__main__":
    main()
