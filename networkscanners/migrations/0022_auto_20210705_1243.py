# Generated by Django 3.1.12 on 2021-07-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkscanners', '0021_auto_20210531_2022'),
    ]

    operations = [
        migrations.DeleteModel(
            name='openvas_scan_db',
        ),
        migrations.DeleteModel(
            name='ov_scan_result_db',
        ),
        migrations.AlterField(
            model_name='networkscanresultsdb',
            name='port',
            field=models.TextField(blank=True, null=True),
        ),
    ]
