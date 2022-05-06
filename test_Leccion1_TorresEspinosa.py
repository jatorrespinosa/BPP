# --- Ejercicio Leccion 2 - BPP - TorresEspinosa,JoseAntonio ---
from Leccion1_TorresEspinosa import *
import unittest
import pandas as pd

class TextLeccion1(unittest.TestCase):
    # data = pd.DataFrame({'Enero':[100, -300, -200], 'Febrero':[500, -100, 400], 'Marzo':[1000, -900, 100]})

    def test_encuentra_meses(self):
        r_gasto, r_ahorro = encuentra_meses(data)
        self.assertEqual(r_gasto, 'Abril') and self.assertEqual(r_ahorro, 'Enero')
    
    def test_balance(self):
        t_gasto, t_ingreso = balance(data)
        self.assertEqual(t_gasto, -297934) and self.assertEqual(t_ingreso, 280961)

    def test_existe1(self):
        result = existe("inanzas2020.csv")
        self.assertFalse(result)
    
    def test_existe2(self):
        result = existe("finanzas2020.csv")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()