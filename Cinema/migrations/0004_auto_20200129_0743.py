# Generated by Django 3.0 on 2020-01-29 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema', '0003_auto_20200129_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='mov_id',
            new_name='mov',
        ),
    ]
