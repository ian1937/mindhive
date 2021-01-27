from django.db import models


class Days(models.TextChoices):
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'


class Role(models.Model):
    name = models.CharField(max_length=50)


class Shift(models.Model):
    day = models.CharField(max_length=10, choices=Days.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Employee(models.Model):
    name = models.CharField(max_length=50)

    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)


class Availability(models.Model):
    day = models.CharField(max_length=10, choices=Days.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
