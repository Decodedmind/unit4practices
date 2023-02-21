from django.test import TestCase

from app import models as e


class test_airline(TestCase):
    def test_create_ticket(self):
        ticket = e.create_ticket("2023-05-14", "Tennesse", "Eddie")
        ticket2 = e.create_ticket("2023-02-11", "California", "julia", 1)
        ticket3 = e.create_ticket("2023-04-15", "New York", "patrick", 2)
        ticket4 = e.create_ticket("2023-01-18", "Boston", "alyx", 3)
        ticket5 = e.create_ticket("2023-04-29", "Chicago", "anthony", 4)

        self.assertEqual(ticket2.id, 2)
        self.assertEqual(ticket2.date, "2023-02-11")
        self.assertEqual(
            ticket2.destination,
            "California",
        )
        self.assertEqual(ticket2.passenger, "julia")
        self.assertEqual(ticket2.bag, 1)
        self.assertEqual(ticket2.first_class, False)

        self.assertEqual(ticket.bag, 0)

    def test_find_ticket_alyx(self):
        ticket = e.create_ticket("2023-05-14", "Tennesse", "Eddie")
        ticket2 = e.create_ticket("2023-02-11", "California", "julia", 1)
        ticket3 = e.create_ticket("2023-04-15", "New York", "patrick", 2)
        ticket4 = e.create_ticket("2023-01-18", "Boston", "alyx", 3)
        ticket5 = e.create_ticket("2023-04-29", "Chicago", "anthony", 4)

        found_ticket = e.find_ticket(4)

    def test_upgrade_ticket(self):
        ticket = e.create_ticket("2023-05-14", "Tennesse", "Eddie")
        ticket2 = e.create_ticket("2023-02-11", "California", "julia", 1)
        ticket3 = e.create_ticket("2023-04-15", "New York", "patrick", 2)
        ticket4 = e.create_ticket("2023-01-18", "Boston", "alyx", 3)
        ticket5 = e.create_ticket("2023-04-29", "Chicago", "anthony", 4)

        ticket = e.upgrade_ticket(3)
