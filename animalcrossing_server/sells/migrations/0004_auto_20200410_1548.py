# Generated by Django 3.0.3 on 2020-04-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sells', '0003_auto_20200410_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='close',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='createTime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='islandPassCode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='itemName',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='numberOfItem',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='reportCount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='unitPrice',
            field=models.IntegerField(default=0, null=True),
        ),
    ]