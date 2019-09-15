# Generated by Django 2.2.5 on 2019-09-15 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ormdemo', '0002_auto_20190915_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ormdemo.Teacher', verbose_name='讲师'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='ormdemo.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='teacherassistant',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ormdemo.Teacher', verbose_name='讲师'),
        ),
    ]
