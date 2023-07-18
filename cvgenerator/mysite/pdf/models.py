from django.db import models

# Create your models here.
class Resume(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,default='')
    image = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=15)
    marital_status = models.CharField(max_length=40)
    linked_in = models.CharField(max_length=20,default='')
    website = models.CharField(max_length=20,default='')
    description = models.TextField(max_length=1000)

    job_profile = models.CharField(max_length=50,default='')
    job_profile_description = models.TextField(max_length=1000,default='')

    job_title = models.CharField(max_length=100)
    job_city = models.CharField(max_length=50)
    job_company = models.CharField(max_length=50)
    job_start_month = models.CharField(max_length=15)
    job_start_year = models.CharField(max_length=4)
    job_end_month = models.CharField(max_length=25)
    job_end_year = models.CharField(max_length=4,default='')
    job_description = models.TextField(max_length=400)

    job_title2 = models.CharField(max_length=100,default='')
    job_city2 = models.CharField(max_length=50,default='')
    job_company2 = models.CharField(max_length=50,default='')
    job_start_month2 = models.CharField(max_length=15,default='')
    job_start_year2 = models.CharField(max_length=4,default='')
    job_end_month2 = models.CharField(max_length=25, default='Currently Working')
    job_end_year2 = models.CharField(max_length=4, default='')
    job_description2 = models.TextField(max_length=400,default='')

    edu_degree = models.CharField(max_length=50)
    edu_degree_college_name = models.CharField(max_length=50,default='')
    edu_city = models.CharField(max_length=15)
    edu_university = models.CharField(max_length=100)
    edu_school = models.CharField(max_length=25)
    edu_school_city = models.CharField(max_length=25,default='')
    edu_school_board = models.CharField(max_length=25,default='')
    edu_degree_end_month = models.CharField(max_length=15,default='')
    edu_degree_end_year = models.CharField(max_length=4,default='')
    edu_degree_description = models.TextField(max_length=500)

    project1 = models.CharField(max_length=50,default='')
    project1_description = models.TextField(max_length=1000,default='')
    project2 = models.CharField(max_length=50,default='')
    project2_description = models.TextField(max_length=1000,default='')

    skills = models.TextField(max_length=1000)

    hobby = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name





