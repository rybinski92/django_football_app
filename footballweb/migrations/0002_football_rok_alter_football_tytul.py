# Generated by Django 4.2.5 on 2023-09-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("footballweb", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="football",
            name="rok",
            field=models.PositiveSmallIntegerField(default=1900),
        ),
        migrations.AlterField(
            model_name="football",
            name="tytul",
            field=models.CharField(max_length=64, unique=True),
        ),
    ]