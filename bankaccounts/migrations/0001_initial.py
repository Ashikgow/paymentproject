# Generated by Django 4.2.4 on 2023-09-01 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('account_number', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=12, max_length=25, prefix='217', unique=True)),
                ('account_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=10, max_length=25, prefix='DIGP', unique=True)),
                ('pin_number', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=7, prefix='', unique=True)),
                ('account_status', models.CharField(choices=[['in_active', 'IN_ACTIVE'], ['active', 'ACTIVE']], default='in-active', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kyc_submitted', models.BooleanField(default=False)),
                ('kyc_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
