from django.shortcuts import render
import os
from django.conf import settings
from .models import Resume
import pdfkit
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def accept(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name","")
        last_name = request.POST.get("last_name","")
        #image = request.POST.get("image","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        address = request.POST.get("address","")
        pin_code = request.POST.get("pin_code","")
        city = request.POST.get("city","")
        dob = request.POST.get("dob","")
        gender = request.POST.get("gender","")
        nationality = request.POST.get("nationality","")
        marital_status = request.POST.get("marital_status","")
        linked_in = request.POST.get("linked_in","")
        website = request.POST.get("website","")
        description = request.POST.get("description","")

        job_profile = request.POST.get("job_profile","")
        job_profile_description = request.POST.get("job_profile_description","")

        job_title = request.POST.get("job_title","")
        job_city = request.POST.get("job_city","")
        job_company = request.POST.get("job_company","")
        job_start_month = request.POST.get("job_start_month","")
        job_start_year = request.POST.get("job_start_year","")
        job_end_month = request.POST.get("job_end_month","")
        job_end_year = request.POST.get("job_end_year","")
        job_description = request.POST.get("job_description","")

        job_title2 = request.POST.get("job_title2", "")
        job_city2 = request.POST.get("job_city2", "")
        job_company2 = request.POST.get("job_company2", "")
        job_start_month2 = request.POST.get("job_start_month2", "")
        job_start_year2 = request.POST.get("job_start_year2", "")
        job_end_month2 = request.POST.get("job_end_month2", "")
        job_end_year2 = request.POST.get("job_end_year2", "")
        job_description2 = request.POST.get("job_description2", "")

        edu_degree = request.POST.get("edu_degree","")
        edu_degree_college_name = request.POST.get("edu_degree_college_name","")
        edu_city = request.POST.get("edu_city","")
        edu_university = request.POST.get("edu_university","")
        edu_school = request.POST.get("edu_school","")
        edu_school_city = request.POST.get("edu_school_city","")
        edu_school_board = request.POST.get("edu_school_board","")
        edu_degree_end_month = request.POST.get("edu_degree_end_month","Currently Working")
        edu_degree_end_year = request.POST.get("edu_degree_end_year","")
        edu_degree_description = request.POST.get("edu_degree_description","")

        project1 = request.POST.get("project1","")
        project1_description = request.POST.get("project1_description","")
        project2 = request.POST.get("project2","")
        project2_description = request.POST.get("project2_description","")

        skills = request.POST.get("skills","")

        hobby = request.POST.get("hobby","")

        resume = Resume(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address,pin_code=pin_code,city=city,dob=dob,gender=gender,nationality=nationality,marital_status=marital_status,linked_in=linked_in,website=website,description=description,job_profile=job_profile,job_profile_description=job_profile_description,job_title=job_title,job_city=job_city,job_company=job_company,job_start_month=job_start_month,job_start_year=job_start_year,job_end_month=job_end_month,job_end_year=job_end_year,job_description=job_description,job_title2=job_title2,job_city2=job_city2,job_company2=job_company2,job_start_month2=job_start_month2,job_start_year2=job_start_year2,job_end_month2=job_end_month2,job_end_year2=job_end_year2,job_description2=job_description2,edu_degree=edu_degree,edu_degree_college_name=edu_degree_college_name,edu_city=edu_city,edu_university=edu_university,edu_school=edu_school,edu_school_city=edu_school_city,edu_school_board=edu_school_board,edu_degree_end_month=edu_degree_end_month,edu_degree_end_year=edu_degree_end_year,edu_degree_description=edu_degree_description,project1=project1,project1_description=project1_description,project2=project2,project2_description=project2_description,skills=skills,hobby=hobby)
        resume.save()

    return render(request,'pdf/accept.html')

def cv(request,id):
    user_profile = Resume.objects.get(pk=id)
    # return render(request,'pdf/cv.html',{'user_profile':user_profile})
    template = loader.get_template('pdf/cv.html')
    html = template.render({'user_profile':user_profile})
    options ={
        'page-size' : 'Letter',
        'encoding' : "UTF-8",
        "enable-local-file-access": ""
    }
    # config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "cv.pdf"
    return response

def list(request):
    profiles = Resume.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})


def resume_cv(request,id):
    user_profile = Resume.objects.get(pk=id)
    return render(request,'pdf/design1.html',{'user_profile':user_profile})



