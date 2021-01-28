from django.db import models


class Days(models.TextChoices):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"[{self.id}] {self.name}"


class Shift(models.Model):
    day = models.CharField(max_length=10, choices=Days.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f"{self.day}: {self.start_time} - {self.end_time}"


class Employee(models.Model):
    name = models.CharField(max_length=50)

    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.role})"


class Availability(models.Model):
    day = models.CharField(max_length=10, choices=Days.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.day}: {self.start_time} - {self.end_time}"
