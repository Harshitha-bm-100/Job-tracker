from django.db import models


class Job(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    applied_date = models.DateField()
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='applied')

    class Meta:
        ordering = ['-applied_date']

    def __str__(self):
        return f'{self.role} at {self.company}'

