# Generated by Django 3.1.4 on 2021-01-03 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0002_auto_20210101_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(help_text='Choose a category:             H -> House,            J -> Job,            S -> Sale,            O -> Other', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ads.category'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
