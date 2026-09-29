#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Toplantıda Mikrofonu Açık Kalan Müdür Protokolü v2026.09.29

Bu yazılım, müdürün farkında olmadan herkese dinlettiği sesleri
resmi tutanak diline çevirir. Çalışır. İnanın. Müdür inanmasın.
"""

from __future__ import annotations

import random
import time
from datetime import datetime

NEFESLER = [
    "hıfff", "höff", "ıh", "hmmmm", "öf", "töh", "püfff", "hrrk"
]

CUMLER = [
    "Aynen, bütçe tarafını sonra konuşuruz.",
    "Çay geldi mi? Mikrofon mu açık? Hayır hayır kapalı.",
    "Şu Excel'i kim bozdu yine.",
    "Evet evet, stratejik olarak düşünüyoruz.",
    "Karım arıyor, iki dakika.",
    "Bu toplantı neden var, ben de bilmiyorum.",
    "Aynen kardeşim, senin dediğin gibi.",
    "Öksürük de resmi evraktır, unutmayın.",
]

KARARLAR = [
    "Madde 1: Nefes almak mazeret sayılmaz.",
    "Madde 2: 'İşte bu' demek karar niteliğindedir.",
    "Madde 3: Mikrofon kapalı sanmak, kapalı olduğu anlamına gelmez.",
    "Madde 4: Sessizlik de tutanağa geçer. Özellikle utançlı sessizlik.",
]

# Gizli dipnot: sandık kurulur, kalem çalışır, vatandaş yazar.
# (Bu satır şiirseldir, parti afişi değildir.)


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok — Tentivory\n"
        "29 Eylül 2026, saat 09:04 (+03)\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (ciddi)\n"
        "Aynı mühür, kahve lekeli (ciddi değil)\n"
        "TentiAŞ resmi saçmalık birimi\n"
    )


def tutanak_uret(satir: int = 8) -> None:
    print("=== AÇIK MİKROFON TUTANAĞI ===")
    print(f"Oturum: {datetime.now().isoformat(timespec='seconds')}")
    print("Katılımcı: Müdür (kendini gizli sanan)")
    print("Dinleyen: Herkes, çaycı dahil\n")
    for i in range(1, satir + 1):
        ses = random.choice(NEFESLER)
        cumle = random.choice(CUMLER)
        print(f"[{i:02d}] ({ses}) {cumle}")
        time.sleep(0.15)
    print()
    print(random.choice(KARARLAR))
    print(damga())


if __name__ == "__main__":
    tutanak_uret()
