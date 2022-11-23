from rest_framework.serializers import ModelSerializer
from .models import Apartments

class ApartmentsSerializer(ModelSerializer):
    class Meta:
        model = Apartments
        fields = '__all__'