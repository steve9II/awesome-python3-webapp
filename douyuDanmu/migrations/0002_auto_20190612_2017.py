# Generated by Django 2.2 on 2019-06-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='cid',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lead',
            name='bl',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='bnn',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]