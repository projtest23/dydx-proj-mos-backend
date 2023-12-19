from rest_framework.serializers import ModelSerializer
from ...models import Positions,Balance

class PositionSerializer(ModelSerializer):

    class Meta:
        model = Positions
        fields = [
            "id",
            "user",
            "market",
            "long",
            "size",
            "leverage",
            "realized_PL",
            "average_open",
            "created_date",
            "updated_date",
        ]


    def to_representation(self, instance):
        rep = super().to_representation(instance)
    
        return rep