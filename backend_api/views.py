from django.http import JsonResponse
from django.forms.models import  model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ApartmentsSerializer
from .models import Apartments

# Create your views here.
@api_view(["GET"])
def api (request, *args, ** kwargs):
    instance =  Apartments.objects.all()

    serializer = ApartmentsSerializer(instance, many = True)

    return Response(serializer.data)
