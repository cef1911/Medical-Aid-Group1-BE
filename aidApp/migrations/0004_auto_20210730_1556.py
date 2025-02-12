# Generated by Django 3.2.4 on 2021-07-30 19:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aidApp', '0003_auto_20210710_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('your_email', models.EmailField(max_length=60)),
                ('nature_of_enquiry', models.TextField(choices=[('Feedback', 'Feedback'), ('Careers', 'Careers'), ('Support', 'Support')], default='Feedback')),
                ('subject', models.CharField(max_length=50, null=True)),
                ('your_message', models.TextField(max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='subject',
        ),
        migrations.AddField(
            model_name='appointment',
            name='app_date',
            field=models.DateField(default=datetime.date(2021, 7, 30)),
        ),
        migrations.AddField(
            model_name='appointment',
            name='app_status',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='appointment',
            name='app_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.AddField(
            model_name='feedback',
            name='response_type',
            field=models.TextField(choices=[('complaint', 'complaint'), ('other', 'other')], default='complaint'),
        ),
        migrations.AddField(
            model_name='health_practitioner',
            name='appointments_approved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='health_practitioner',
            name='appointments_pending',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='health_practitioner',
            name='clinics',
            field=models.ManyToManyField(to='aidApp.Clinic'),
        ),
        migrations.AddField(
            model_name='health_practitioner',
            name='consultation_times',
            field=models.TextField(default='Monday - 10:00am to 11:00am', max_length=400),
        ),
        migrations.AddField(
            model_name='health_practitioner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='health_practitioner',
            name='professional_title',
            field=models.CharField(default='Dr. ', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='D_O_B',
            field=models.DateField(default=datetime.date(2021, 7, 30)),
        ),
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='health_practitioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aidApp.health_practitioner'),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='appointments_url',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='website',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='health_practitioner',
            name='health_practitioner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('health_practitioner', 'app_date', 'app_time')},
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='is_approved',
        ),
    ]
