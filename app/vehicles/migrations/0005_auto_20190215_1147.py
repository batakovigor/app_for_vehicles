# Generated by Django 2.1.7 on 2019-02-15 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_auto_20190215_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Марка АТС')),
            ],
            options={
                'verbose_name': 'Марка АТС',
                'verbose_name_plural': 'Марки АТС',
            },
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.ModelCar', verbose_name='Марка АТС'),
        ),
    ]