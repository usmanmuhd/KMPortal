# Generated by Django 2.1.7 on 2019-03-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='automobile_used_in',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]