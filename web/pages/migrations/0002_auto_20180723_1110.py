# Generated by Django 2.0.6 on 2018-07-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='pages',
            name='tite',
            field=models.CharField(max_length=150),
        ),
    ]
