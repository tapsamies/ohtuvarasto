import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(),0)

    def test_virheellinen_tilavuus_toimii(self):
        self.varasto = Varasto(-20)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_virheellinen_alkusaldo_toimii(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(),10)

    def test_lisays_negatiivinen(self):
        self.assertIsNone(self.varasto.lisaa_varastoon(-5))

    def test_otetaan_negatiivinen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-5),0)

    def test_otetaan_kaikki(self):
        self.varasto =Varasto(20)
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10000),20)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(),20)
    
    def test_varasto_vastaa_oikein(self):
        self.assertLogs(print(self.varasto),"saldo = 0, vielä tilaa 10")
