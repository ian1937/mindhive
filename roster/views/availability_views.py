from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from roster.models import Availability
from roster.serializers.availability import AvailabilitySerializer


@api_view(["GET", "POST", "DELETE"])
def availabilities(request):

    if request.method == "GET":
        availabilities = Availability.objects.all()
        serializer = AvailabilitySerializer(availabilities, many=True)
        return Response(serializer.data, status=200)

    elif request.method == "POST":
        serializer = AvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

    elif request.method == "DELETE":
        availabilities = Availability.objects.all()
        availabilities.delete()
        return Response(status=204)

    return HttpResponse(status=404)


@api_view(["GET", "PUT", "DELETE"])
def availability(request, id):

    try:
        availability = Availability.objects.get(id=id)
    except Availability.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = AvailabilitySerializer(availability)
        return Response(serializer.data, status=200)

    elif request.method == "PUT":
        serializer = AvailabilitySerializer(availability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

    elif request.method == "DELETE":
        availability.delete()
        return Response(status=204)

    return HttpResponse(status=404)
    