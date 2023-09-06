from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=254, verbose_name='Широта')),
                ('longitude', models.FloatField(max_length=254, verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
            options={
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='PerevalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otc', models.CharField(max_length=255, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=64, verbose_name='Номер телефона')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('N', 'Новый'), ('P', 'Модерируется'), ('A', 'Принят'), ('R', 'Отклонен')], default='N', max_length=1)),
                ('beauty_title', models.CharField(max_length=254)),
                ('title', models.CharField(max_length=254)),
                ('other_titles', models.CharField(max_length=254)),
                ('connect', models.TextField(blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('level_spring', models.CharField(blank=True, max_length=254, verbose_name='Сложность весной')),
                ('level_summer', models.CharField(blank=True, max_length=254, verbose_name='Сложность летом')),
                ('level_autumn', models.CharField(blank=True, max_length=254, verbose_name='Сложность осенью')),
                ('level_winter', models.CharField(blank=True, max_length=254, verbose_name='Сложность зимой')),
                ('coords', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_main.coords')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pereval', to='app_main.perevaluser')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, verbose_name='Название')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Время добавления')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.perevaladd')),
            ],
            options={
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
