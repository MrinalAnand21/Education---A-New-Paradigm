# Generated by Django 3.0.5 on 2023-04-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating1', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], max_length=500)),
                ('rating2', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], max_length=500)),
                ('rating3', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], max_length=500)),
                ('suggestions', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedbacks',
            },
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('Standard 1', 'Standard 1'), ('Standard 2', 'Standard 2'), ('Standard 3', 'Standard 3'), ('Standard 4', 'Standard 4'), ('Standard 5', 'Standard 5'), ('Standard 6', 'Standard 6'), ('Standard 7', 'Standard 7'), ('Standard 8', 'Standard 8'), ('Standard 9', 'Standard 9'), ('Standard 10', 'Standard 10')], default='Standard 1', max_length=100),
        ),
    ]
