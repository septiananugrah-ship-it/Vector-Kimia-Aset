"""Perkakas bersama untuk modul poster: tema, terjemahan, teks, dan bentuk dasar.

Terjemahan: semua teks poster ditulis dalam bahasa Inggris dan diterjemahkan
lewat kamus TR (lihat poster_i18n.py) saat bahasa aktif adalah "id".
"""
import math

from icons_lab_flat import solid
from poster_i18n import TR
from render import GRID, fitted, style_attrs
from textpath import text as _text
from textpath import width

_lang = ["en"]


def set_lang(lang):
    _lang[0] = lang


def tr(s):
    return TR.get(s, s) if _lang[0] == "id" else s


def text(s, *a, **k):
    return _text(tr(s), *a, **k)


THEMES = {
    "dark": dict(bg="#16213A", card="#1F2C48", card_stroke="#2C3D5E", plate="#E9F1F7", ink="#FFFFFF",
                 sub="#AEB9C9", accent="#3FB6C4", mood="on dark navy"),
    "light": dict(bg="#FFFFFF", card="#F2F6FA", card_stroke="#DCE4EE", plate="#FFFFFF", ink="#1E2A3A",
                  sub="#5B6878", accent="#1F9AA8", mood="on white"),
}
MX = 44  # margin kiri-kanan
COMMON_KW = ["chemistry", "science", "education", "school", "poster", "infographic", "chart", "classroom",
              "teaching", "learning", "student", "scientific", "vector", "illustration", "diagram",
              "educational", "laboratory", "chemical", "study", "reference"]


def fit_text(s, x, y, size, fill, max_w, weight="Bold", anchor="middle"):
    s = tr(s)
    w = width(s, size, weight)
    if w > max_w:
        size *= max_w / w
    return text(s, x, y, size, fill, weight, anchor)


def header(W, th, title, subtitle):
    return (text(title, W / 2, 66, 34, th["ink"]) +
            text(subtitle, W / 2, 92, 12.5, th["sub"], "Regular"))


def doc(W, H, th, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 5:.0f}" height="{H * 5:.0f}" '
            f'viewBox="0 0 {W} {H}">\n<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="{th["bg"]}"/>'
            f'{inner}\n</svg>\n')


def icon_at(body, stroke, x, y, size):
    """Ikon (grid 64) dipasang di kotak size x size pada (x, y)."""
    return (f'<g transform="translate({x:.2f} {y:.2f}) scale({size / GRID:.4f})">'
            f'<g {style_attrs(stroke)}>{fitted(body, stroke)}</g></g>')


def particle(cx, cy, r, col, key, shine=True):
    ball = solid(f"M{cx - r:.2f} {cy:.2f}a{r} {r} 0 1 0 {2 * r} 0a{r} {r} 0 1 0 {-2 * r} 0z", col, cx - r, cx + r)
    ball = ball.replace("{p}", key)
    if not shine:
        return ball
    return (ball +
            f'<ellipse cx="{cx - r * .35:.2f}" cy="{cy - r * .38:.2f}" rx="{r * .3:.2f}" ry="{r * .2:.2f}" '
            f'transform="rotate(-35 {cx - r * .35:.2f} {cy - r * .38:.2f})" fill="#FFFFFF" stroke="none"/>')


def arrow(x1, y1, x2, y2, col, bend=0):
    """Panah lengkung dari (x1,y1) ke (x2,y2); bend = lengkungan (negatif ke atas)."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + bend
    ang = math.atan2(y2 - my, x2 - mx)
    hx, hy = x2 - 12 * math.cos(ang), y2 - 12 * math.sin(ang)
    px, py = 6 * math.sin(ang), -6 * math.cos(ang)
    return (f'<path d="M{x1} {y1}Q{mx:.2f} {my + bend:.2f} {hx:.2f} {hy:.2f}" fill="none" stroke="{col}" '
            f'stroke-width="3.2" stroke-linecap="round"/>'
            f'<path d="M{x2} {y2}L{hx + px:.2f} {hy + py:.2f}L{hx - px:.2f} {hy - py:.2f}z" fill="{col}" '
            f'stroke="{col}" stroke-width="1.5" stroke-linejoin="round"/>')
