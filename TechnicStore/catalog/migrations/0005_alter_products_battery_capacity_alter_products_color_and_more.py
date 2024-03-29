# Generated by Django 4.1.6 on 2023-04-03 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_products_battery_capacity_products_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='battery_capacity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='battery_capacity', to='catalog.valueproductattributes', verbose_name='Ємність аккумулятора'),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='catalog.valueproductattributes', verbose_name='Колір'),
        ),
        migrations.AlterField(
            model_name='products',
            name='front_camera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='front_camera', to='catalog.valueproductattributes', verbose_name='Фронтальна камера'),
        ),
        migrations.AlterField(
            model_name='products',
            name='internal_memory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_memory', to='catalog.valueproductattributes', verbose_name="Внутрішня пам'ять"),
        ),
        migrations.AlterField(
            model_name='products',
            name='main_camera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_camera', to='catalog.valueproductattributes', verbose_name='Основна камера'),
        ),
        migrations.AlterField(
            model_name='products',
            name='number_SIM',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Number_SIM', to='catalog.valueproductattributes', verbose_name='Кількість SIM-карт'),
        ),
        migrations.AlterField(
            model_name='products',
            name='procesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='procesor', to='catalog.valueproductattributes', verbose_name='процесор'),
        ),
        migrations.AlterField(
            model_name='products',
            name='screen_diagonal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screen_diagonal', to='catalog.valueproductattributes', verbose_name='Діагональ екрану'),
        ),
        migrations.AlterField(
            model_name='products',
            name='screen_resolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screen_resolution', to='catalog.valueproductattributes', verbose_name='Роздільна здатність екрану'),
        ),
        migrations.AlterField(
            model_name='products',
            name='screen_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screen_type', to='catalog.valueproductattributes', verbose_name='Тип екрану'),
        ),
        migrations.AlterField(
            model_name='products',
            name='working_memory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='working_memory', to='catalog.valueproductattributes', verbose_name='Оперативна'),
        ),
    ]
