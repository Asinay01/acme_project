from django.urls import include, path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.RegisterView.as_view(), name='registration'),
]