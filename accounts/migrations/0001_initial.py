# Generated by Django 5.0.2 on 2024-03-07 07:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cloth_post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField(unique=True)),
                ('initial_deposit_date', models.DateField(auto_now_add=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('buy_history', models.ManyToManyField(to='cloth_post.buynow')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
