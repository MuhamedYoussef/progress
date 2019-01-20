from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Progress


@login_required
def progress(request):
    context = {
        'progress_list': Progress.objects.order_by('-id')
    }

    return render(request, 'progress/progress.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        details = request.POST['details']

        Progress.objects.create(
            owner=request.user, title=title, details=details)
        return redirect('progress')

    return render(request, 'progress/add.html')


@login_required
def remove(request, id):
    Progress.objects.filter(id=id).delete()
    return redirect('progress')
