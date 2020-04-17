# Generated by Django 3.0.3 on 2020-04-10 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bts_asset_db', '0016_auto_20200409_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_channel',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='is_consumable',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_set', to='bts_asset_db.Item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stored_item_set', to='bts_asset_db.Item'),
        ),
        migrations.DeleteModel(
            name='ItemChannel',
        ),
    ]
