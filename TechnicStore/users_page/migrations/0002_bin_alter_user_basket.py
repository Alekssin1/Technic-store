# Generated by Django 4.1.6 on 2023-03-18 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_valueproductattributes_options'),
        ('users_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='кількість')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.products', verbose_name='Кошик')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='basket',
            field=models.ManyToManyField(related_name='bin', to='users_page.bin', verbose_name='Кошик'),
        ),
    ]
