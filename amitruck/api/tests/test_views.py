from api.models import Trip
from django.conf import settings
from django.urls import reverse
from rest_framework.test import APITestCase


class CreateTripApiTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("get-create-trip")
        self.user = settings.AUTH_USER_MODEL.objects.create_user(
            username="testuser", password="12345"
        )
        self.client.force_authenticate(user=self.user)
        self.initial_data = self.client.post(
            self.url,
            {
                "address_type": "pickup_point",
                "driver_id": 12345,
                "vehicle_id": 12345,
                "customer_id": 12345,
                "address": "Kenya",
                "cargo_tonnage": "12.76",
            },
            format="json",
        )

    def test_post(self):
        self.assertEqual(self.initial_data.status_code, 201)

    def test_get(self):
        response = self.client.get(self.url)
        response_data = response.data[0]
        self.assertEqual(response.status_code, 200)
