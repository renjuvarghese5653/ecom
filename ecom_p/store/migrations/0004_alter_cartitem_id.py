# Generated by Django 5.0.1 on 2024-02-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_cartitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
