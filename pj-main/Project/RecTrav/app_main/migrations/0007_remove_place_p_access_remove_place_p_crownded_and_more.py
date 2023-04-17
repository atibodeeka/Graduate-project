# Generated by Django 4.0.6 on 2022-09-14 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_main', '0006_place_p_access_place_p_crownded_place_p_landscape_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='p_access',
        ),
        migrations.RemoveField(
            model_name='place',
            name='p_crownded',
        ),
        migrations.RemoveField(
            model_name='place',
            name='p_landscape',
        ),
        migrations.RemoveField(
            model_name='place',
            name='p_satisfaction',
        ),
        migrations.RemoveField(
            model_name='place',
            name='p_spacial',
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisfaction', models.IntegerField(null=True)),
                ('access', models.IntegerField(null=True)),
                ('crownded', models.IntegerField(null=True)),
                ('landscape', models.IntegerField(null=True)),
                ('spacial', models.IntegerField(null=True)),
                ('p_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_main.place')),
                ('u_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]