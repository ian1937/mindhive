from rest_framework import serializers
from roster.models import Employee, Availability


class EmployeeNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["id", "name"]


class AvailabilitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Availability
        fields = ["id", "day", "start_time", "end_time", "employee"]
        
    def to_representation(self, instance):
        self.fields["employee"] =  EmployeeNameSerializer(required=False)
        return super(AvailabilitySerializer, self).to_representation(instance)