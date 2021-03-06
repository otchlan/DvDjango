# Generated by Django 2.1.7 on 2019-04-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_avalaiability'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperProduct',
            fields=[
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('avalaiability', models.BooleanField()),
                ('coins', models.BooleanField(primary_key=True, serialize=False)),
            ],
        ),
    ]
