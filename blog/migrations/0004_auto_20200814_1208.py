# Generated by Django 3.0.8 on 2020-08-14 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200812_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-publish'], 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['parent__id', 'position'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.Category', verbose_name='زیر دسته'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(related_name='article', to='blog.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
    ]