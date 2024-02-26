import unittest
from unittest.mock import patch
from io import StringIO
from main import Engine, Car


#Блочные тесты
class TestEngine(unittest.TestCase):
    def test_start_engine(self):
        engine = Engine(2000)
        expected_output = "Engine(2000) started\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            engine.start_engine()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_accelerate(self):
        engine = Engine(2000)
        expected_output = "Accelerating(2000) the engine\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            engine.accelerate()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_stop_engine(self):
        engine = Engine(2000)
        expected_output = "Engine(2000) stopped\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            engine.stop_engine()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_start_engine_negative(self):
        engine = Engine(-150)
        expected_output = "Несуществующая машина\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            engine.start_engine()
            self.assertEqual(fake_out.getvalue(), expected_output)


# Интеграционные тесты
class TestCar(unittest.TestCase):
    def test_start(self):
        my_car = Car("Toyota", "Camry", 2000)
        expected_output = "Starting the Toyota Camry\nEngine(2000) started\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            my_car.start()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_drive(self):
        my_car = Car("Toyota", "Camry", 2000)
        expected_output = "Driving the Toyota Camry\nAccelerating(2000) the engine\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            my_car.drive()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_stop(self):
        my_car = Car("Toyota", "Camry", 2000)
        expected_output = "Stopping the Toyota Camry\nEngine(2000) stopped\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            my_car.stop()
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
