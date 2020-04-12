# Generated by Django 3.0.3 on 2020-04-12 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('islands', '0005_island_rule'),
        ('accountInfos', '0006_auto_20200410_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='IslandReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now=True, null=True)),
                ('accountInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservedIslands', to='accountInfos.AccountInfo')),
                ('island', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='islands.Island')),
            ],
        ),
    ]
