# Generated by Django 3.0 on 2021-08-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='type',
            field=models.CharField(default='', max_length=256, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(default='', max_length=256, verbose_name='类型'),
        ),
    ]
