# Generated by Django 3.1.7 on 2021-03-03 19:41

import graph_app.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("graph_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="apiclient",
            managers=[
                ("objects", graph_app.managers.UserManager()),
            ],
        ),
    ]
