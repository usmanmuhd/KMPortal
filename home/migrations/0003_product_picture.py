# Generated by Django 2.1.7 on 2019-03-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190325_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='', upload_to='product'),
            preserve_default=False,
        ),
    ]
