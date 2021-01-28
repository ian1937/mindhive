from rest_framework import serializers
from roster.models import Role, Shift, Employee, Availability


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ["id", "name"]


class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = ["day", "start_time", "end_time"]


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["name", "role"]

    """ see https://stackoverflow.com/questions/50256852/django-rest-framework-post-foreign-key for details"""
    def to_representation(self, instance):
        self.fields["role"] =  RoleSerializer()
        return super(EmployeeSerializer, self).to_representation(instance)


class EmployeeNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["name"]


class AvailabilitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Availability
        fields = ["day", "start_time", "end_time", "employee"]
        
    def to_representation(self, instance):
        self.fields["employee"] =  EmployeeNameSerializer()
        return super(AvailabilitySerializer, self).to_representation(instance)
