# Generated by Django 3.1 on 2020-08-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collector', '0002_auto_20200827_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='PXIConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('packet_size', models.IntegerField(default=200)),
                ('packet_header_1', models.IntegerField(default=27)),
                ('packet_header_2', models.IntegerField(default=59)),
                ('packet_header_3', models.IntegerField(default=27)),
                ('crc_size', models.IntegerField(default=2)),
            ],
        ),
    ]