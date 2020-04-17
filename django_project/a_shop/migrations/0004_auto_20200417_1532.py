# Generated by Django 3.0.5 on 2020-04-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_shop', '0003_auto_20200417_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'archive'), (2, 'approved'), (3, 'rejected'), (1, 'pending'), (4, 'sent email')], default=1),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_status',
            field=models.SmallIntegerField(choices=[(1, 'active'), (0, 'inactive')], default=0),
        ),
    ]
