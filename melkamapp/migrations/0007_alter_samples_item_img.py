# Generated by Django 5.0.1 on 2024-08-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melkamapp', '0006_alter_samples_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samples',
            name='item_img',
            field=models.CharField(max_length=500),
        ),
    ]
