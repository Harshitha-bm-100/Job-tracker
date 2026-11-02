import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='applied_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(
                choices=[
                    ('not_applied', 'Not Applied'),
                    ('pending', 'Pending'),
                    ('applied', 'Applied'),
                    ('shortlisted', 'Shortlisted'),
                    ('interview_scheduled', 'Interview Scheduled'),
                    ('offer_received', 'Offer Received'),
                    ('accepted', 'Accepted'),
                    ('rejected', 'Rejected'),
                ],
                default='applied',
                max_length=200,
            ),
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-applied_date']},
        ),
    ]
