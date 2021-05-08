# Generated by Django 3.0.5 on 2021-05-08 15:02

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Regular', 'Regular'), ('Square', 'Square')], max_length=50, null=True)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Regular', 'Regular'), ('Large', 'Large')], max_length=20, null=True)),
                ('topping', multiselectfield.db.fields.MultiSelectField(choices=[('onion', 'Onion'), ('tomato', 'Tomato'), ('corn', 'Corn'), ('capsicum', 'Capsicum'), ('cheese', 'Cheese'), ('jalepeno', 'Jalepeno')], max_length=42)),
            ],
        ),
    ]