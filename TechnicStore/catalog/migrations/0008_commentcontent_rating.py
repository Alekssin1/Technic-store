# Generated by Django 4.1.6 on 2023-04-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_products_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentcontent',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Рейтинг'),
        ),
    ]
