# Generated by Django 2.0.1 on 2018-02-17 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('is_hr_practitioner', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=64)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('profile', models.URLField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(default='images/user_images/nothing.jpg', upload_to='images/user_images/%Y/%m/%d/%H_%M_%S')),
                ('bio', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, default=54.16045, null=True)),
                ('longitude', models.FloatField(blank=True, default=-92.01873, null=True)),
                ('zoom', models.IntegerField(blank=True, default=6, help_text='Sets the default zoom', null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
