"""Set piktogram bahaya GHS: 9 ikon tunggal, 1 lembar gabungan, dan label stiker EN/ID.
Bentuk piktogram diambil dari posters22.pictogram supaya poster dan ikon selalu sama.
"""
import poster_kit
from posters22 import GHS, pictogram
from textpath import text

INK = "#1E2A3A"
KEYWORDS = ["ghs", "hazard symbol", "hazard pictogram", "warning sign", "chemical safety", "safety label",
            "danger", "caution", "laboratory", "chemical", "chemistry", "lab safety", "sign", "symbol", "icon",
            "vector", "red diamond", "msds", "sds", "label", "workplace safety", "industrial"]


def _doc(W, H, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 10}" height="{H * 10}" viewBox="0 0 {W} {H}">\n'
            f'{inner}\n</svg>\n')


def assets():
    single, labels = [], {"en": [], "id": []}
    for kind, name, desc, _ex in GHS:
        single.append(dict(name=f"ghs-hazard-pictograms-{kind}", svg=_doc(200, 200, pictogram(kind, 100, 100, 92)),
                           size=4000, title=f"GHS {name.lower()} hazard pictogram, chemical warning symbol vector icon",
                           keywords=[name.lower(), desc.lower().split(",")[0]] + KEYWORDS))
        for lang in ("en", "id"):
            poster_kit.set_lang(lang)
            label = poster_kit.tr(name).upper()
            if len(label) > 18:  # label panjang dipecah dua baris di spasi terdekat ke tengah
                cut = min((i for i, c in enumerate(label) if c == " "), key=lambda i: abs(i - len(label) / 2))
                caption = text(label[:cut], 130, 272, 19, INK, "Bold") + text(label[cut + 1:], 130, 296, 19, INK, "Bold")
            else:
                caption = text(label, 130, 284, 21, INK, "Bold")
            inner = (f'<rect x="6" y="6" width="248" height="308" rx="26" fill="#FFFFFF" stroke="{INK}" '
                     f'stroke-width="5"/>' + pictogram(kind, 130, 128, 98) + caption)
            note = " in Indonesian language" if lang == "id" else ""
            sid = "ghs-hazard-labels" + ("" if lang == "en" else "-indonesian")
            labels[lang].append(dict(name=f"{sid}-{kind}", svg=_doc(260, 320, inner), size=4000,
                                     title=f"GHS {name.lower()} hazard label sticker{note}, printable chemical "
                                           "warning sign vector",
                                     keywords=(["indonesian", "bahasa indonesia"] if lang == "id" else [])
                                     + [name.lower(), "sticker"] + KEYWORDS))
    poster_kit.set_lang("en")
    sheet = "".join(pictogram(kind, 110 + (i % 3) * 210, 110 + (i // 3) * 210, 92)
                    for i, (kind, *_r) in enumerate(GHS))
    single.append(dict(name="ghs-hazard-pictograms-set", svg=_doc(640, 640, sheet), size=4000,
                       title="GHS hazard pictograms set, nine chemical warning symbols vector collection",
                       keywords=["set", "collection", "all ghs symbols"] + KEYWORDS))
    return [("ghs-hazard-pictograms", single), ("ghs-hazard-labels", labels["en"]),
            ("ghs-hazard-labels-indonesian", labels["id"])]
