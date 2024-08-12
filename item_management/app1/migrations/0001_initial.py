# Generated by Django 5.1 on 2024-08-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('available', 'Available ✅'), ('unavailable', 'Unavailable ❌')], default='available', max_length=12)),
                ('description', models.TextField(max_length=200)),
                ('file', models.ImageField(upload_to='images/')),
            ],
        ),
    ]