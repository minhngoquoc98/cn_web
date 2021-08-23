# Generated by Django 3.1.7 on 2021-08-20 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoMon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Bo_mon',
            },
        ),
        migrations.CreateModel(
            name='CanBo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ho_ten', models.CharField(max_length=255)),
                ('chuc_vu', models.CharField(blank=True, max_length=200, null=True)),
                ('dien_thoai_co_quan', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('dien_thoai_didong', models.CharField(max_length=200, null=True)),
                ('bo_mon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='danh_ba.bomon')),
            ],
            options={
                'db_table': 'can_bo',
            },
        ),
        migrations.CreateModel(
            name='CanBoDanhBa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'CanBoDanhBa',
            },
        ),
        migrations.CreateModel(
            name='Khoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Khoa',
            },
        ),
        migrations.CreateModel(
            name='DanhBa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canbo', models.ManyToManyField(through='danh_ba.CanBoDanhBa', to='danh_ba.CanBo')),
                ('khoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='danh_ba.khoa')),
            ],
            options={
                'db_table': 'Danh_ba',
            },
        ),
        migrations.AddField(
            model_name='canbodanhba',
            name='DanhBa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='danh_ba.danhba'),
        ),
        migrations.AddField(
            model_name='canbodanhba',
            name='canbo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='danh_ba.canbo'),
        ),
        migrations.AddField(
            model_name='bomon',
            name='khoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='danh_ba.khoa'),
        ),
    ]
