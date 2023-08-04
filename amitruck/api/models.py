from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication


class CustomAuthToken(TokenAuthentication):
    keyword = "api_token"


class AddressType(models.TextChoices):
    PICKUP = "pickup_point", _("Pickup point")
    DROPOFF = "drop_off_point", _("Drop off point")


class Trip(models.Model):
    driver_id = models.IntegerField(null=False)
    vehicle_id = models.IntegerField(null=False)
    customer_id = models.IntegerField(null=False)
    address = models.CharField(max_length=50, null=True, blank=True)
    cargo_tonnage = models.DecimalField(max_digits=10, decimal_places=2)
    address_type = models.CharField(
        choices=AddressType.choices, max_length=20, default=AddressType.PICKUP
    )
    done_by_user_id = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Trip")
        verbose_name_plural = _("Trips")

    def __str__(self) -> str:
        return f"{self.customer_id} - {self.created_at}"
