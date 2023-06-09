# Generated by Django 4.2.2 on 2023-06-14 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_remove_product_account'),
        ('user_app', '0004_alter_account_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='product',
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.account')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_app.product')),
            ],
        ),
    ]
