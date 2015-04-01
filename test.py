# Mateusz Gawron, grupa sroda 8:00
# Testy jednostkowe
# np. python test.py

import unittest
from Pilot import Pilot
from Generator import Generator
from main import run

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
        self.pilot = Pilot(self.generator)

    # Testy klasy Generator       
    def test_generator_get_data(self):
        data = self.generator.get_data()
        self.assertIn(data[0], [True, False], "is_left nie jest wartoscia logiczna")
        self.assertTrue(data[1] <= 5.0, "angle wykracza poza zakres")

    # Testy klasy Pilot
    def test_pilot_make_correction_1(self):
        self.pilot.angle = 10.0
        self.pilot.make_correction(False)
        self.assertEqual(self.pilot.angle, 9.0, "Niepoprawna korekcja kata")

    def test_pilot_make_correction_2(self):
        self.pilot.angle = 0.5
        self.pilot.make_correction(False)
        self.assertEqual(self.pilot.angle, 0.0, "Niepoprawna korekcja kata")

    def test_pilot_make_correction_3(self):
        self.pilot.angle = 0.0
        self.pilot.make_correction(False)
        self.assertEqual(self.pilot.angle, 0.0, "Niepoprawna korekcja kata")
        
    def test_pilot_make_timestep_1(self):
        self.pilot.minute = 0
        self.pilot.second = 0
        self.pilot.make_timestep(False)
        self.assertEqual(self.pilot.minute, 0, "Niepoprawna wartosc minuty")
        self.assertEqual(self.pilot.second, 1, "Niepoprawna wartosc sekundy")
    
    def test_pilot_make_timestep_2(self):
        self.pilot.minute = 0
        self.pilot.second = 59
        self.pilot.make_timestep(False)
        self.assertEqual(self.pilot.minute, 1, "Niepoprawna wartosc minuty")
        self.assertEqual(self.pilot.second, 0, "Niepoprawna wartosc sekundy")

    def test_pilot_make_timestep_3(self):
        self.pilot.minute = 59
        self.pilot.second = 59
        self.pilot.make_timestep(False)
        self.assertEqual(self.pilot.minute, 0, "Niepoprawna wartosc minuty")
        self.assertEqual(self.pilot.second, 0, "Niepoprawna wartosc sekundy")

if __name__ == '__main__':
    unittest.main()
