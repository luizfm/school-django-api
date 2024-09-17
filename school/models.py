from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    document = models.CharField(max_length=11)
    birth_date = models.DateField()
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    LEVEL = (
        ('B', 'Base'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )

    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=1, choices = LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.code
    
class Registration(models.Model):
    PERIOD = (("M", "Morning"), ("A", "Afternoon"), ("N", "Night"))

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, default="M", blank=False, null=False)

    def __str__(self):
        return self.period
