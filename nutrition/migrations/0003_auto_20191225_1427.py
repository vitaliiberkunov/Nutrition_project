# Generated by Django 3.0.1 on 2019-12-25 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_auto_20191225_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nutrition.Program'),
        ),
    ]
