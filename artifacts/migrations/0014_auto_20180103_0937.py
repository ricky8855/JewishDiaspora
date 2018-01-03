# Generated by Django 2.0 on 2018-01-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0013_auto_20180101_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifactimage',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='artifactimage',
            old_name='location',
            new_name='location_en',
        ),
        migrations.RenameField(
            model_name='artifactimage',
            old_name='year_era',
            new_name='year_era_en',
        ),
        migrations.RenameField(
            model_name='artifactimagecoord',
            old_name='info',
            new_name='info_en',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='acceptance_date',
        ),
        migrations.AddField(
            model_name='artifactimage',
            name='description_he',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='artifactimage',
            name='location_he',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Image location'),
        ),
        migrations.AddField(
            model_name='artifactimage',
            name='year_era_he',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Year/Era'),
        ),
        migrations.AddField(
            model_name='artifactimagecoord',
            name='info_he',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Info'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description english'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='description_he',
            field=models.TextField(blank=True, null=True, verbose_name='Description hebrew'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', max_length=250, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artifact',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pending approval'), (2, 'Missing info'), (3, 'Approved'), (4, 'Rejected'), (5, 'Disabled')], default=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='technical_data_en',
            field=models.TextField(blank=True, null=True, verbose_name='Technical data english'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='technical_data_he',
            field=models.TextField(blank=True, null=True, verbose_name='Technical data hebrew'),
        ),
    ]
