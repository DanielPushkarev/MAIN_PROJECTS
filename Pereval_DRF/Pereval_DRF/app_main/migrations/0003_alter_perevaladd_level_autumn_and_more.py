from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0002_perevaluser_email_perevaluser_fam_perevaluser_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladd',
            name='level_autumn',
            field=models.CharField(blank=True, max_length=254, verbose_name='Сложность осенью'),
        ),
        migrations.AlterField(
            model_name='perevaladd',
            name='level_spring',
            field=models.CharField(blank=True, max_length=254, verbose_name='Сложность весной'),
        ),
        migrations.AlterField(
            model_name='perevaladd',
            name='level_summer',
            field=models.CharField(blank=True, max_length=254, verbose_name='Сложность летом'),
        ),
        migrations.AlterField(
            model_name='perevaladd',
            name='level_winter',
            field=models.CharField(blank=True, max_length=254, verbose_name='Сложность зимой'),
        ),
    ]
