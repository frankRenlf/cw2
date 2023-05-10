from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Admin(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Employees(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname


# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    gender_choices = (
        (0, "female"),
        (1, "male"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField()
    # delete relevant user
    # depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE)
    # remove depart_id
    depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Passenger(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class payment_method(models.Model):
    payment_platform = models.CharField(max_length=16)

    def __str__(self):
        return self.payment_platform


class Order(models.Model):
    number = models.CharField(max_length=64)
    flight = models.ForeignKey(to="Flight", to_field="id",
                               null=True, blank=True, on_delete=models.SET_NULL)
    passenger = models.ForeignKey(to="Passenger", to_field="id",
                                  null=True, blank=True, on_delete=models.SET_NULL)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    create_time = models.DateTimeField()
    status_choices = (
        (1, "Paid"),
        (0, "Unpaid")
    )
    status = models.SmallIntegerField(choices=status_choices, default=0)
    payment_platform = models.ForeignKey(to="payment_method", to_field="id",
                                         null=True, blank=True, on_delete=models.SET_NULL)

    def to_json(self):
        return {
            "order_id": self.id,
            "number": self.number,
            "flight_id": self.flight_id,
            "passenger_id": self.passenger_id,
            "price": self.price,
            "create_time": self.create_time.isoformat(),
            "status": self.status,
            "payment_platform": self.payment_platform_id
        }


@receiver(pre_save, sender=Order)
def update_order_price(sender, instance, **kwargs):
    if instance.flight:
        instance.price = instance.flight.flight_price


class Flight(models.Model):
    flight_id = models.IntegerField()
    airline_name = models.CharField(max_length=16)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    departure_location = models.CharField(max_length=64)
    arrival_location = models.CharField(max_length=64)
    flight_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    seat_number = models.IntegerField()

    def __str__(self):
        return self.airline_name

    def to_json(self):
        return {
            "flight_id": self.flight_id,
            "airline_name": self.airline_name,
            "departure_time": self.departure_time.isoformat(),
            "arrival_time": self.arrival_time.isoformat(),
            "departure_location": self.departure_location,
            "arrival_location": self.arrival_location,
            "flight_price": str(self.flight_price),
            "seat_number": self.seat_number,
        }


class PrettyNumber(models.Model):
    mobile = models.CharField(max_length=11)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    level_choices = (
        (1, "FIRST"),
        (2, "SECOND"),
        (3, "THIRD"),
    )
    status_choices = (
        (0, "Occupied"),
        (1, "Available")
    )
    level = models.SmallIntegerField(choices=level_choices, default=1)
    status = models.SmallIntegerField(choices=status_choices, default=1)
