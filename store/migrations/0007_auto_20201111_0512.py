# Generated by Django 3.1.3 on 2020-11-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20201110_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
