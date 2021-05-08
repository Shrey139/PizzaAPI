from django.db import models
from multiselectfield import MultiSelectField

TYPE = (
    ('Regular', 'Regular'),
    ('Square', 'Square'),
)

SIZE = (
    ('Small', 'Small'),
    ('Regular', 'Regular'),
    ('Large', 'Large'),
)

TOPPING = (
    ('onion', 'Onion'),
    ('tomato', 'Tomato'),
    ('corn', 'Corn'),
    ('capsicum', 'Capsicum'),
    ('cheese', 'Cheese'),
    ('jalepeno', 'Jalepeno'),
)

class Pizza(models.Model):
    type = models.CharField(max_length=50, null=True, choices=TYPE)
    size = models.CharField(max_length=20, null=True,choices=SIZE)
    topping = MultiSelectField(max_choices=5, choices=TOPPING)

    def __str__(self):
        return self.type
