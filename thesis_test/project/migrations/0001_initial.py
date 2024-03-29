# Generated by Django 3.2.6 on 2021-12-03 13:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0002_auto_20211202_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.department')),
                ('employees', models.ManyToManyField(to='employees.Employee')),
            ],
        ),
    ]
