from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from roster.models import Shift
from roster.serializers import ShiftSerializer


@api_view(["GET", "POST", "DELETE"])
def shifts(request):
    
    if request.method == "GET":
        shifts = Shift.objects.all()
        serializer = ShiftSerializer(shifts, many=True)
        return Response(serializer.data, status=200)

    elif request.method == "POST":
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

    elif request.method == "DELETE":
        shifts = Shift.objects.all()
        shifts.delete()
        return Response(status=204)

    return HttpResponse(status=404)


@api_view(["GET", "PUT", "DELETE"])
def shift(request, id):

    try:
        shift = Shift.objects.get(id=id)
    except Shift.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ShiftSerializer(shift)
        return Response(serializer.data, status=200)

    return HttpResponse(status=404)
