# Generated by Django 5.1 on 2024-08-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_product_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.ImageField(default='default-product.jpg', upload_to='images/'),
        ),
    ]
