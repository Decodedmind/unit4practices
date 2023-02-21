from django.db import models


class TaxiBusiness(models.Model):
    occupied = models.BooleanField()
    capacity = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    fare = models.FloatField()
    taxi_type = models.TextField()
    taxi_number = models.IntegerField()
    note = models.TextField(blank=True, null=True)


def create_taxi(occupied, capacity, number, fare, taxi_type, taxi_number, note):
    taxi = TaxiBusiness(
        occupied=occupied,
        capacity=capacity,
        number=number,
        fare=fare,
        taxi_type=taxi_type,
        taxi_number=taxi_number,
        note=note,
    )
    taxi.save()
    return taxi


def send_taxi(id, number):
    taxi = TaxiBusiness.objects.get(id=id)
    if number <= taxi.capacity:
        taxi.occupied = True
        taxi.number = number

        taxi.save()
        return taxi
    else:
        raise ValueError("cant")


def finish_fare(id, distance):
    taxi = TaxiBusiness.objects.get(id=id)
    if taxi.occupied == True:
        taxi.number = 0
        taxi.occupied = False
        cost = taxi.fare * distance
        taxi.save()
        return cost

    else:
        raise ValueError("what do you mean you ain't got no money")


def remove_taxi(taxi_number):
    try:
        taxi = TaxiBusiness.objects.get(taxi_number=taxi_number)
        taxi.delete()
    except TaxiBusiness.DoesNotExist:
        raise ValueError("taxi doesn't exist")


def find_taxi(taxi_number):
    try:
        taxi = TaxiBusiness.objects.get(taxi_number=taxi_number)

        return taxi

    except:
        raise ValueError("no taxi available")


def filter_un_occupied(occupied):
    taxi = TaxiBusiness.objects.filter(occupied=occupied)
    if taxi.occupied == False:
        return taxi


def capacity_no_occupied(capacity):
    return TaxiBusiness.objects, filter(occupied=False, capacity__gte=capacity)
