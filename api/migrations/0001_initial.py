# Generated by Django 3.2.9 on 2021-12-16 00:30

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
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(blank=True, max_length=200, null=True)),
                ('color_code', models.CharField(blank=True, choices=[('gray', 'gray'), ('blue', 'blue'), ('purple', 'purple'), ('brown', 'brown')], max_length=6, null=True)),
                ('status', models.CharField(blank=True, choices=[('pre-inquiry', 'pre-inquiry'), ('in progress', 'in progress'), ('zero - inactive', 'zero - inactive')], max_length=20, null=True)),
                ('received_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('analyst', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cases_assigned', to='api.person')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cases', to='api.person')),
            ],
        ),
    ]
