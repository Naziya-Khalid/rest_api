from django.urls import path
from . import views
from .views import RegistrationView

urlpatterns = [
    path('api/works/', views.WorkList.as_view(), name='work-list'),
    path('api/artists/', views.ArtistList.as_view(), name='artist-list'),
    path('api/register/', RegistrationView.as_view(), name='register')
]

