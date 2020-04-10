# Generated by Django 3.0.3 on 2020-04-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sells', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='hashTagDescription',
            new_name='islandPassCode',
        ),
        migrations.AddField(
            model_name='sell',
            name='itemName',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sell',
            name='numberOfItem',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sell',
            name='unitPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sell',
            name='createTime',
            field=models.TimeField(auto_now=True),
        ),
    ]