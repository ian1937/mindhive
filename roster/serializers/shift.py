from rest_framework import serializers
from roster.models import Shift
from roster.serializers.role import EmployeeSetSerializer


class ShiftSerializer(serializers.ModelSerializer):
    worked_by = EmployeeSetSerializer(read_only=True)

    class Meta:
        model = Shift
        fields = ["day", "start_time", "end_time", "worked_by"]