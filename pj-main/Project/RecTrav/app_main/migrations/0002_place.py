# Generated by Django 4.0.6 on 2022-08-02 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=60)),
                ('p_address', models.CharField(max_length=60)),
                ('p_province', models.CharField(max_length=60)),
                ('p_district', models.CharField(max_length=60)),
                ('p_subdistrict', models.CharField(max_length=60)),
                ('p_postnumber', models.CharField(max_length=60)),
            ],
        ),
    ]
