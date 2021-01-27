from rest_framework import serializers
from roster.models import Role, Shift, Employee, Availability


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('name',)


class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = ('day', 'start_time', 'end_time')


class EmployeeSerializer(serializers.ModelSerializer):
    pass


class AvailabilitySerializer(serializers.ModelSerializer):
    pass
