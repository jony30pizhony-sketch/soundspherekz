from rest_framework import generics
from .models import AndroidHeadUnit
from .serializers import HeadUnitSerializer

class HeadUnitListAPIView(generics.ListAPIView):
    queryset = AndroidHeadUnit.objects.all()
    serializer_class = HeadUnitSerializer

class HeadUnitDetailAPIView(generics.RetrieveAPIView):
    queryset = AndroidHeadUnit.objects.all()
    serializer_class = HeadUnitSerializer