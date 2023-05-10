from app01 import models
from app01.utils.BootstrapModelForm import BootstrapModelForm
from django.core.exceptions import ValidationError


class FlightModelForm(BootstrapModelForm):
    class Meta:
        model = models.Flight
        fields = ["flight_id", "airline_name", "departure_time", "arrival_time", "departure_location",
                  "arrival_location", "flight_price", "seat_number"]
