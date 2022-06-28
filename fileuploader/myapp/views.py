from django.http import HttpResponse
from django.shortcuts import render

from .models import Candidate

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        job_title = request.POST['job_title']
        applicants_cv = request.POST['applicants_cv']

        cand_obj  = Candidate(name = name,email=email, job_title=job_title,applicants_cv=applicants_cv)
        cand_obj.save()


    candidates = Candidate.objects.all()
    dict = {
        'title' : 'File Uploader',
        'candidates' : candidates

    }
    print(candidates)

    return render(request,'index.html',context = dict)
