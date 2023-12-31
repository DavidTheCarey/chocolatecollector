# Generated by Django 4.2.5 on 2023-09-29 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Order Date')),
                ('location', models.CharField(default='Boston', max_length=100)),
                ('chocolate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.chocolate')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
