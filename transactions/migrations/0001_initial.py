# Generated by Django 4.0.4 on 2022-08-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_name', models.CharField(max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
