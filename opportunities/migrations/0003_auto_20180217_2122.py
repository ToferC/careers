# Generated by Django 2.0.1 on 2018-02-17 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0002_auto_20180217_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='element',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='file',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='openrecommendation',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendation_creator', to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='openrecommendation',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='response',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Member'),
        ),
        migrations.AlterField(
            model_name='skillrecommendation',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.Member'),
        ),
    ]
