# Generated by Django 3.0.3 on 2020-04-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('islands', '0002_auto_20200410_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='island',
            name='createTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
