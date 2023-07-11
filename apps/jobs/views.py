from django.shortcuts import render


def jobs(request):
    ctx = {

    }
    return render(request, 'jobs/borwse_job.html', ctx)
