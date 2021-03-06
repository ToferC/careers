# Generated by Django 2.0.1 on 2018-02-17 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opportunities.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('APPLIED', 'Applied'), ('SCREENED_IN', 'Screened In'), ('SCREENED_OUT', 'Screened Out'), ('REVIEW', 'Under Review'), ('ASSESSED', 'Assessment Completed'), ('RETAINED', 'Application Retained'), ('INTERVIEW', 'Interview Requested'), ('OFFERED', 'Job Offered'), ('REFUSED', 'Job Refused'), ('ACCEPTED', 'Job Accepted')], default='AP', max_length=32)),
                ('status_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.CharField(choices=[('MEETS', 'Meets requirement'), ('FAILS', 'Does not meet requirement'), ('EXCEEDS', 'Exceeds requirement')], default='ME', max_length=32)),
                ('rationale', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
                ('assessor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('req_type', models.CharField(choices=[('QUESTION', 'Question'), ('DEMOGRAPHIC', 'Demographic'), ('EDUCATION', 'Education'), ('CERTIFICATION', 'Certification'), ('SKILL', 'Skill'), ('TRAINING', 'Training'), ('EXPERIENCE', 'Experience'), ('BEHAVIOR', 'Behavior')], default='SK', max_length=32)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('weight', models.FloatField(default=1)),
                ('mandatory', models.BooleanField(default=False)),
                ('generic', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now=True)),
                ('date_edited', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('file', models.FileField(upload_to=opportunities.models.user_directory_path)),
                ('upload_date', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OpenRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendation_creator', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('country', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=256)),
                ('province', models.CharField(max_length=256)),
                ('street', models.CharField(max_length=256)),
                ('postal_code', models.CharField(max_length=6)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('apply_date', models.DateTimeField(verbose_name='apply by')),
                ('start_date', models.DateTimeField(verbose_name='starting date')),
                ('end_date', models.DateTimeField(verbose_name='ending date')),
                ('permanent_opportunity', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=124)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now=True)),
                ('date_edited', models.DateField(auto_now=True)),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Element')),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Opportunity')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence', models.TextField(max_length=500)),
                ('submitted_date', models.DateTimeField(auto_now=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('files', models.ManyToManyField(to='opportunities.File')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Requirement')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('level', models.CharField(choices=[('SEEKING', 'Seeking'), ('NOVICE', 'Novice'), ('TRAINED', 'Trained'), ('EXPERT', 'Expert'), ('MASTER', 'Master')], default='NO', max_length=15)),
                ('created_date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkillRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('SEEKING', 'Seeking'), ('NOVICE', 'Novice'), ('TRAINED', 'Trained'), ('EXPERT', 'Expert'), ('MASTER', 'Master')], default='NO', max_length=15)),
                ('text', models.TextField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(to='opportunities.Skill'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='elements',
            field=models.ManyToManyField(related_name='elements', through='opportunities.Requirement', to='opportunities.Element'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Requirement'),
        ),
        migrations.AddField(
            model_name='application',
            name='opportunity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_to_opportunity', to='opportunities.Opportunity'),
        ),
    ]
