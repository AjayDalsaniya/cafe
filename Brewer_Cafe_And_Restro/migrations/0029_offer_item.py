# Generated by Django 4.1.3 on 2022-12-31 17:36

import Brewer_Cafe_And_Restro.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0028_alter_itemcategory_item_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('idoffer', models.AutoField(primary_key=True, serialize=False)),
                ('offer_value', models.DecimalField(decimal_places=1, max_digits=2)),
                ('offer_start_date', models.DateField()),
                ('offer_end_date', models.DateField()),
                ('offer_description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'offer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('iditem', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=60)),
                ('item_price', models.IntegerField()),
                ('item_description', models.CharField(max_length=200)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to=Brewer_Cafe_And_Restro.models.filepathItem)),
                ('item_category_iditem_category', models.ForeignKey(db_column='item_category_iditem_category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.itemcategory')),
                ('offer_idoffer', models.ForeignKey(db_column='offer_idoffer', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.offer')),
            ],
            options={
                'db_table': 'item',
                'managed': True,
            },
        ),
    ]
