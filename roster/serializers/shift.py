from rest_framework import serializers
from roster.models import Shift
from roster.serializers.employee import EmployeeSerializer


class ShiftSerializer(serializers.ModelSerializer):
    worked_by = EmployeeSerializer(read_only=True)

    class Meta:
        model = Shift
        fields = ["day", "start_time", "end_time", "worked_by"]