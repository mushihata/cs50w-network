# Generated by Django 3.1.1 on 2020-10-20 15:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20201016_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followings',
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followeings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
