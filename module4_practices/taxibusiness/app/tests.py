from django.test import TestCase

from app import models as e


class TaxiBusiness(TestCase):
    def test_create_taxi(self):
        taxi = e.create_taxi(False, 4, 0, 1.5, "car", 111, "")
        taxi2 = e.create_taxi(True, 8, 8, 3.5, "van", 122, "")
        taxi3 = e.create_taxi(False, 20, 0, 0.50, "bus", 133, "")

        self.assertEquals(taxi.id, 1)
        self.assertEquals(taxi.occupied, False)
        self.assertEqual(taxi.capacity, 4)
        self.assertEqual(taxi.number, 0)
        self.assertEqual(taxi.fare, 1.5)
        self.assertEqual(taxi.taxi_type, "car")
        self.assertEqual(taxi.taxi_number, 111)
        self.assertEqual(taxi.note, "")

        self.assertEquals(taxi2.id, 2)
        self.assertEquals(
            taxi2.occupied,
            True,
        )
        self.assertEqual(taxi2.capacity, 8)
        self.assertEqual(taxi2.number, 8)
        self.assertEqual(taxi2.fare, 3.5)
        self.assertEqual(taxi2.taxi_type, "van")
        self.assertEqual(taxi2.taxi_number, 122)
        self.assertEqual(taxi2.note, "")

        self.assertEquals(taxi3.id, 3)
        self.assertEquals(taxi3.occupied, False)
        self.assertEqual(taxi3.capacity, 20)
        self.assertEqual(taxi3.number, 0)
        self.assertEqual(taxi3.fare, 0.50)
        self.assertEqual(taxi3.taxi_type, "bus")
        self.assertEqual(taxi3.taxi_number, 133)
        self.assertEqual(taxi3.note, "")

    def test_send_taxi(self):
        taxi = e.create_taxi(False, 4, 0, 1.5, "car", 111, "")
        taxi2 = e.create_taxi(True, 8, 8, 3.5, "van", 122, "")
        taxi3 = e.create_taxi(False, 20, 0, 0.50, "bus", 133, "")

        self.assertEqual(taxi.occupied, False)
        self.assertEqual(taxi.number, 0)

        taxi = e.send_taxi(1, 2)

        self.assertEqual(taxi.occupied, True)
        self.assertEqual(taxi.number, 2)

    def test_finish_fare(self):
        taxi = e.create_taxi(False, 4, 0, 1.5, "car", 111, "")
        taxi2 = e.create_taxi(True, 8, 8, 3.5, "van", 122, "")
        taxi3 = e.create_taxi(False, 20, 0, 0.50, "bus", 133, "")

        cost = e.finish_fare(2, 4)
        self.assertEqual(cost, 14)
    

    def test_remove_taxi(self):
        taxi = e.create_taxi(False, 4, 0, 1.5, "car", 111, "")
        taxi2 = e.create_taxi(True, 8, 8, 3.5, "van", 122, "")
        taxi3 = e.create_taxi(False, 20, 0, 0.50, "bus", 133, "")

        