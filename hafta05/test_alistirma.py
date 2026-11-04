# Alıştırma 4: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import indirim_orani, sepet_toplami, en_pahali_urun


def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145

@pytest.mark.parametrize(
    "tutar, beklenen_indirim",
    [
        (0, 0),
        (99, 0),
        (100, 5),
        (499, 5),
        (500, 10),
        (999, 10),
        (1000, 15),
        (1500, 15),
    ],
)
def test_indirim_orani_sinirlari(tutar, beklenen_indirim):
    assert indirim_orani(tutar) == beklenen_indirim


def test_indirim_orani_negatif_tutar_hatasi():
    with pytest.raises(ValueError, match="tutar negatif olamaz"):
        indirim_orani(-1)

def test_sepet_toplami_bos_sepet():
    assert sepet_toplami([]) == 0


@pytest.mark.parametrize("adet", [0, -1])
def test_sepet_toplami_gecersiz_adet_hatasi(adet):
    sepet = [{"urun": "çay", "fiyat": 20, "adet": adet}]
    with pytest.raises(ValueError, match="adet pozitif olmalı"):
        sepet_toplami(sepet)

def test_en_pahali_urun_bos_sepet():
    assert en_pahali_urun([]) is None


def test_en_pahali_urun_tek_veya_farkli_fiyatlar():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 1},
        {"urun": "tost", "fiyat": 60, "adet": 1},
        {"urun": "simit", "fiyat": 15, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "tost"


def test_en_pahali_urun_esit_fiyatta_ilki_donmeli():
    sepet = [
        {"urun": "kahve", "fiyat": 50, "adet": 1},
        {"urun": "pasta", "fiyat": 50, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "kahve"
