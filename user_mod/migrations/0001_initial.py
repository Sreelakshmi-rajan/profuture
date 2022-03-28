# Generated by Django 4.0.3 on 2022-03-21 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('userprofileid', models.AutoField(primary_key=True, serialize=False)),
                ('usertype', models.CharField(max_length=20)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]