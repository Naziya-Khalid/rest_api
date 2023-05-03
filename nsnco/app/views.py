
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Work, Artist
from .serializers import WorkSerializer, ArtistSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Client
from .serializers import UserSerializer


class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    filter_backends = [SearchFilter]
    search_fields = ['artist__name', 'work_type']

    def get_queryset(self):
        queryset = Work.objects.all()
        artist_name = self.request.query_params.get('artist', None)
        if artist_name is not None:
            queryset = queryset.filter(artist__name=artist_name)
        work_type = self.request.query_params.get('work_type', None)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)
        return queryset

class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            client = Client.objects.create(user=user, name=user.username)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  