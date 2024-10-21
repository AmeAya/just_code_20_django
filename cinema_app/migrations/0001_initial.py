# Generated by Django 5.1.2 on 2024-10-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('genre', models.CharField(max_length=255)),
                ('duration', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=255)),
            ],
        ),
    ]
