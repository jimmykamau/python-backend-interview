from api.models import AddressType, Trip
from rest_framework import serializers


class TripSerializer(serializers.ModelSerializer):
    done_by_user_id = serializers.SerializerMethodField("_user")
    address_type = serializers.ChoiceField(choices=AddressType.choices)

    class Meta:
        model = Trip
        fields = "__all__"

    def _user(self, obj):
        request = self.context.get("request", None)
        if request:
            return request.user.pk
