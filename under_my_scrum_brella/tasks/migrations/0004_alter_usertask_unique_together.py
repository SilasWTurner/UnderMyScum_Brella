# Generated by Django 5.0.1 on 2024-03-18 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_grouptask_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usertask',
            unique_together=set(),
        ),
    ]
