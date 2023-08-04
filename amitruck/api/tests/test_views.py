from api.models import Trip
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class CreateTripApiTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("get-create-trip")
        self.user = User.objects.create_user(username="testuser", password="12345")
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
        self.expected_response_keys = [
            "id",
            "done_by_user_id",
            "address_type",
            "driver_id",
            "vehicle_id",
            "customer_id",
            "address",
            "cargo_tonnage",
            "created_at",
            "updated_at",
        ]

    def test_post(self):
        self.assertEqual(self.initial_data.status_code, 201)
        self.assertEqual(Trip.objects.get().driver_id, 12345)

    def test_get(self):
        response = self.client.get(self.url)
        response_data = response.data[0]
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(self.expected_response_keys, response_data)

    def test_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
