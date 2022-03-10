# Generated by Django 3.2.10 on 2022-03-10 20:31

import api.query
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=80, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
            bases=(api.query.GrapheneQueryMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(blank=True, max_length=200, null=True)),
                ('color_code', models.CharField(blank=True, choices=[('gray', 'gray'), ('blue', 'blue'), ('purple', 'purple'), ('brown', 'brown')], max_length=6, null=True)),
                ('status', models.CharField(blank=True, choices=[('pre-inquiry', 'pre-inquiry'), ('in progress', 'in progress'), ('zero - inactive', 'zero - inactive')], max_length=20, null=True)),
                ('received_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('analyst', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incidents_assigned', to='api.person')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incidents', to='api.person')),
            ],
            bases=(api.query.GrapheneQueryMixin, models.Model),
        ),
    ]
