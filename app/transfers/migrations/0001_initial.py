# Generated by Django 4.0.5 on 2022-06-23 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transfer',
                'verbose_name_plural': 'Transfers',
            },
        ),
        migrations.CreateModel(
            name='TransferFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='transfers.transfer')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transfer File',
                'verbose_name_plural': 'Transfer Files',
            },
        ),
    ]