from datetime import datetime

from django.db.models import Model, CharField, EmailField, BooleanField, DateField
from django.utils.timezone import now


class Employee(Model):
    status_choices = [
        (1, 'Active'),
        (0, 'Inactive')
    ]

    name = CharField(max_length=255)
    email = EmailField(max_length=150)
    age = DateField()
    address = CharField(max_length=255)
    status = BooleanField(choices=status_choices, default=False)
    phone = CharField(max_length=15)

    @property
    def age_year(self):
        return now().year  - self.age.year

    def __str__(self):
        return f'{self.name}'
