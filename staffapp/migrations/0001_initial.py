# Generated by Django 2.0.6 on 2020-06-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('gender', models.SmallIntegerField(choices=[(0, 'female'), (1, 'male'), (2, 'unknown')], default=1)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('pic', models.ImageField(default='pic/1.jpg', upload_to='pic')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'db_table': 'drf_employee',
            },
        ),
    ]