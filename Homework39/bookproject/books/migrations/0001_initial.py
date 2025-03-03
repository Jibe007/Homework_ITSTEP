# Generated by Django 5.1.6 on 2025-02-17 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('published_date', models.DateField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category')),
            ],
        ),
    ]
