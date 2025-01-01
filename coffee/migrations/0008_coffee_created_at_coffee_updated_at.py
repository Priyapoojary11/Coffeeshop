# Generated by Django 5.1 on 2024-12-16 08:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0007_alter_order_total_cost_alter_orderitem_item_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
