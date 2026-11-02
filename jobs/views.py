from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import JobForm
from .models import Job


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})


def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})


@require_POST
def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return redirect('home')
