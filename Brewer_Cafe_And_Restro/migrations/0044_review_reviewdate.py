# Generated by Django 4.1.3 on 2023-01-27 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0043_review_rating_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewDate',
            field=models.DateField(null=True, verbose_name=datetime.date.today),
        ),
    ]
