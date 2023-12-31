# Generated by Django 4.2.4 on 2023-10-12 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0006_alter_transaction_receiver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=10, max_length=20, prefix='CRED', unique=True)),
                ('name', models.CharField(max_length=255)),
                ('number', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=16, max_length=16, prefix='', unique=True)),
                ('month', models.CharField(max_length=15)),
                ('year', models.IntegerField()),
                ('cvv', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=22, max_length=3, prefix='', unique=True)),
                ('card_type', models.CharField(choices=[['visa', 'VISA'], ['rupay', 'RUPAY'], ['mastercard', 'MASTERCARD'], ['platinum', 'PLATINUM']], max_length=20)),
                ('card_status', models.CharField(choices=[['active', 'ACTIVE'], ['inactive', 'INACTIVE']], default='in_active', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
