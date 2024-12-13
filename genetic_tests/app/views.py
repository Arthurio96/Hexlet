from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Max, Count, Q
from .models import GeneticTest
from .serializers import GeneticTestSerializer

@api_view(['POST'])
def add_test(request):
    serializer = GeneticTestSerializer(data=request.data)
    if serializer.is_valid():
        test = serializer.save()
        return Response({"message": "Данные успешно добавлены", "id": test.id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tests(request):
    species_filter = request.GET.get('species')
    tests = GeneticTest.objects.all()
    if species_filter:
        tests = tests.filter(species=species_filter)
    serializer = GeneticTestSerializer(tests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_statistics(request):
    stats = GeneticTest.objects.values('species').annotate(
        total_tests=Count('id'),
        avg_milk_yield=Avg('milk_yield'),
        max_milk_yield=Max('milk_yield'),
        good_health_percentage=Count('id', filter=Q(health_status='good')) * 100.0 / Count('id')
    )
    return Response({"statistics": list(stats)})