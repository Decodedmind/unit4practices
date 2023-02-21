from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Airline(models.Model):
    date = models.DateField()
    destination = models.TextField()
    passenger = models.TextField()
    bag = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)]
    )

    first_class = models.BooleanField(default=0)


def create_ticket(date, destination, passenger, bag=0):
    ticket = Airline(
        date=date,
        destination=destination,
        passenger=passenger,
        bag=bag,
    )
    ticket.save()
    return ticket


def find_ticket(id):
    try:
        ticket = Airline.objects.get(id=id)

        return ticket

    except Airline.DoesNotExist:
        raise ValueError("ticket not found")


def upgrade_ticket(id):
    ticket = find_ticket(id)
    if not ticket.first_class:
        ticket.first_class = True
        ticket.save()
        return ticket

    else:
        raise ValueError("you to broke")
