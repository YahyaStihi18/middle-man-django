# Generated by Django 3.0.6 on 2020-05-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_klm'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.FloatField(default=0.0),
        ),
    ]