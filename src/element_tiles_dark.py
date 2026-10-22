"""Bentuk ubin unsur tema gelap, dipakai element_tiles_dark1..3 (modul ini sendiri bukan set)."""
from periodic import CAT
from textpath import text

NAVY, NAVY2 = "#1B2742", "#22304F"


def dark_tile(z, sym, name, mass, cat):
    col = CAT[cat][1]
    return (f'<path d="M4 10a6 6 0 0 1 6-6h44a6 6 0 0 1 6 6v44a6 6 0 0 1-6 6H10a6 6 0 0 1-6-6z" fill="{NAVY}"/>'
            f'<path d="M38 4h16a6 6 0 0 1 6 6v44a6 6 0 0 1-6 6H38z" fill="{NAVY2}" stroke="none"/>'
            f'<path d="M6.8 10.8a4 4 0 0 1 4-4h42.4a4 4 0 0 1 4 4v42.4a4 4 0 0 1-4 4H10.8a4 4 0 0 '
            f'1-4-4z" fill="none" stroke="{col}" stroke-width="1.5"/>'
            + text(str(z), 11.5, 17, 7.5, col, "Bold", "start")
            + text(sym, 32, 38.5, 23 if len(sym) == 1 else 20, "#FFFFFF")
            + text(name, 32, 47.5, 6.4 if len(name) < 10 else 5.6, col, "SemiBold")
            + text(mass, 32, 53.2, 4.6, "#AEB9C9", "Regular"))
