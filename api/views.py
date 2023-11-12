from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView

from api.models import Letter, Package
from api.serializers import LetterSerializer, PackageSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class RUDLetter(RetrieveUpdateDestroyAPIView):
    queryset = Letter.objects.all()
    serializer = LetterSerializer


class CreateLetter(CreateAPIView):
    queryset = Letter.objects.all()
    serializer = LetterSerializer


class RUDPackager(RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer = PackageSerializer


class CreateLPackage(CreateAPIView):
    queryset = Package.objects.all()
    serializer = PackageSerializer
