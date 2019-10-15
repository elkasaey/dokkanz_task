# Generated by Django 2.2.2 on 2019-10-15 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductCode', models.CharField(max_length=50)),
                ('ProductName', models.CharField(max_length=50)),
                ('ProductPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ProductQuantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.Category')),
                ('ProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.Product')),
            ],
        ),
    ]
