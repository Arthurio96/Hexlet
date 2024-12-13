from django.urls import path
from .views import add_test, get_tests, get_statistics

urlpatterns = [
    path('tests', add_test, name='add_test'),
    path('tests', get_tests, name='get_tests'),
    path('statistics', get_statistics, name='get_statistics'),
]
