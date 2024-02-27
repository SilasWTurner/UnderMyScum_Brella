# Generated by Django 5.1.dev20240130101038 on 2024-02-27 10:24

from django.db import migrations

def set_index_values(apps,schema_editor):
    Item = apps.get_model('items','Item')
    for item_name, index_value in [('Bin Hat', 0), ('Glasses', 1), ('Gold Medal', 2), ('Rubish Picker', 3), ('Water Bottle', 4)]:
        Item.objects.filter(item_name=item_name).update(item_index=index_value)


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_item_item_index'),
    ]

    operations = [
        migrations.RunPython(set_index_values),
    ]
