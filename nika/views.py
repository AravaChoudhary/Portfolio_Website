from django.shortcuts import render,get_object_or_404
from .models import cp,Projects
from django.http import JsonResponse


def all_nika(request):
    return render(request, 'nika/all_nika.html')

def skills(request):
    return render(request, 'nika/skills.html')

def projects(request):
    nikass = Projects.objects.all()
    return render(request, 'nika/projects.html', {'nikass':nikass})

def project_details(request,project_id):
    pros = get_object_or_404(Projects, pk=project_id)
    return render(request, 'nika/project_details.html',{'pros':pros})

def cultivated_pursuits(request):
    nikas = cp.objects.all()
    return render(request, 'nika/cultivated_pursuits.html',{'nikas':nikas})

def interests_details(request,nika_id):
    nika = get_object_or_404(cp, pk=nika_id)
    return render(request, 'nika/interests_details.html',{'nika':nika})

def contact_me(request):
    return render(request, 'nika/contact_me.html')

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not subject or not message:
            return JsonResponse({'success': False, 'message': 'Please fill out all required fields.'})

        return JsonResponse({'success': True, 'message': 'Your message has been successfully sent!'})

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})