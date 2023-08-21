from django.db import models
from hospital.models import hospital_department, specialization, UserP,Patient

# Create your models here.


class doctor_info(models.Model):
    DOC_TYPE = (
        ('Psychiatrist','Psychiatrist'),
        ('Clinical Psychologist','Clinical Psychologist'),
        ('Therapist','Therapist'),
        ('Marriage and Family Therapist (MFT)','Marriage and Family Therapist (MFT)'),
        ('Child and Adolescent Psychiatrist','Child and Adolescent Psychiatrist'),
        ('Neuropsychologist','Neuropsychologist'),
    )

    doc_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(UserP, on_delete=models.CASCADE, null=True, blank=True,related_name='profile')
    name = models.CharField(max_length=50,null=True,blank=True)
    # check
    username = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=50,default='123')
    role = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, null=True, blank=True)
    department = models.CharField(max_length= 70, choices=DOC_TYPE, null=True, blank=True)
    department_name = models.ForeignKey(hospital_department, on_delete=models.SET_NULL, null=True, blank=True)
    specialization = models.ForeignKey(specialization, on_delete=models.SET_NULL, null=True, blank=True)

    featured_image = models.ImageField(upload_to='doctors/', default='doctors/user-default.png', null=True, blank=True)
    certificate_image = models.ImageField(upload_to='doctors_certificate/', default='doctors_certificate/default.png', null=True, blank=True)

    
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    nid = models.CharField(max_length=70, null=True, blank=True)
    visiting_hour = models.CharField(max_length=50, null=True, blank=True)
    consultation_fee = models.IntegerField(null=True, blank=True)
    report_fee = models.IntegerField(null=True, blank=True)
    dob = models.CharField(max_length=50, null=True, blank=True)
    
    # Education
    institute = models.CharField(max_length=70, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    completion_year = models.CharField(max_length=100, null=True, blank=True)
    
    # work experience
    work_place = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    start_year = models.CharField(max_length=50, null=True, blank=True)
    end_year = models.CharField(max_length=50, null=True, blank=True)
    
    # register_status = models.BooleanField(default=False) default='pending'
    register_status =  models.CharField(max_length=50, null=True, blank=True)
    
    # ForeignKey --> one to one relationship with Hospital_Information model.
    # hospital_name = models.ForeignKey(Hospital_Information, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
    
class doctorExperience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    work_place = models.CharField(max_length=200)
    from_year = models.DateField()
    to_year = models.DateField(null=True, blank=True)
    designation = models.CharField(max_length=200)
    doctor_id = models.ForeignKey(doctor_info, on_delete=models.CASCADE)

    def __str__(self):
        return f"Experience ID: {self.experience_id}, Work Place: {self.work_place}, " \
               f"Designation: {self.designation}, Doctor ID: {self.doctor_id}"
    
# experience_id is defined as the primary key with AutoField to be auto-incremented.
# work_place is a CharField with a maximum length of 200 characters.
# from_year is a DateField representing the starting year of the experience.
# to_year is a DateField representing the ending year of the experience. It's allowed to be null and blank if the experience is ongoing.
# designation is a CharField with a maximum length of 200 characters.
# doctor_id is defined as a foreign key that references the DoctorInformation model, and it uses on_delete=models.CASCADE to enforce cascading deletion. It's not allowed to be null.

class DoctorEducation(models.Model):
    education_id = models.AutoField(primary_key=True)
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year_of_completion = models.DateField()
    doctor_id = models.ForeignKey(doctor_info, on_delete=models.CASCADE)

    def __str__(self):
        return f"Education ID: {self.education_id}, Degree: {self.degree}, " \
               f"Institute: {self.institute}, Doctor ID: {self.doctor_id}"

# education_id is defined as the primary key with AutoField to be auto-incremented.
# degree is a CharField with a maximum length of 200 characters.
# institute is a CharField with a maximum length of 200 characters.
# year_of_completion is a DateField representing the year of completion for the education.
# doctor_id is defined as a foreign key that references the DoctorInformation model, and it uses on_delete=models.CASCADE to enforce cascading deletion.