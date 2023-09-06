from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perevaluser',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True, verbose_name='Эл.почта'),
        ),
        migrations.AddField(
            model_name='perevaluser',
            name='fam',
            field=models.CharField(default=None, max_length=254, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='perevaluser',
            name='name',
            field=models.CharField(default=None, max_length=254, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='perevaladd',
            name='level_autumn',
            field=models.CharField(max_length=254, verbose_name='Сложность осенью'),
        ),
        migrations.AlterField(
            model_name='perevaladd',
            name='level_spring',
            field=models.CharField(max_length=254, verbose_name='Сложность весной'),
        ),
        migrations.AlterField(
            model_name='perevaladd',
            name='level_summer',
            field=models.CharField(max_length=254, verbose_name='Сложность летом'),
        ),
        migrations.AlterField(
            model_name='perevaladd',
            name='level_winter',
            field=models.CharField(max_length=254, verbose_name='Сложность зимой'),
        ),
    ]
