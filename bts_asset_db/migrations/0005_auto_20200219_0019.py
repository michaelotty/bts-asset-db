# Generated by Django 3.0.3 on 2020-02-19 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bts_asset_db', '0004_auto_20200218_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualtests',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bts_asset_db.Item'),
        ),
    ]
