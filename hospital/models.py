from django.db import models
from django.contrib.auth.models import AbstractUser
# NameError handling
from django.utils.translation import gettext_lazy as _


"""
null=True --> don't require a value when inserting into the database
blank=True --> allow blank value when submitting a form
auto_now_add --> automatically set the value to the current date and time
unique=True --> prevent duplicate values
primary_key=True --> set this field as the primary key
editable=False --> prevent the user from editing this field

django field types --> google it  # every field types has field options
Django automatically creates id field for each model class which will be a PK # primary_key=True --> if u want to set manual
"""

# Create your models here.

class UserP(AbstractUser):
    class Meta:
        # Add the related_name argument for groups and user_permissions
        # to prevent clashes with the built-in User model
        permissions = []

    # Override the default user_permissions and groups fields
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        help_text=_('Specific permissions for this user.'),
        blank=True,
        related_name='user_q_set',  # New related_name to avoid conflict
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name='user_q_set',  # New related_name to avoid conflict
    )
    demo = models.CharField(max_length=50, null= True)
    role = models.IntegerField(default=0)
    login_status = models.BooleanField(default=False)

    
class Patient(models.Model):
    Patient_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(UserP,on_delete=models.CASCADE,null=True,blank=True,related_name='patient')
    name = models.CharField(max_length=50,null=True,blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=50,default='123')
    role = models.IntegerField(default=0)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    sex = models.BooleanField(default=False)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    featured_image = models.ImageField(upload_to='edit_profile/', default='static/image/profile_default.svg', null=True, blank=True)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    history = models.CharField(max_length=200, null=True, blank=True)
    dob = models.CharField(max_length=200, null=True, blank=True)
    nid = models.CharField(max_length=200, null=True, blank=True)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    # Chat
    login_status = models.CharField(max_length=200, null=True, blank=True, default="offline")

    def __str__(self):
        return str(self.user.username)

class Hospital_Information(models.Model):
    # ('database value', 'display_name')
    HOSPITAL_TYPE = (
        ('private', 'Private hospital'),
        ('public', 'Public hospital'),
    )

    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    featured_image = models.ImageField(upload_to='hospitals/', default='hospitals/default.png', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    hospital_type = models.CharField(max_length=200, choices=HOSPITAL_TYPE)
    general_bed_no = models.IntegerField(null=True, blank=True)
    available_icu_no = models.IntegerField(null=True, blank=True)
    regular_cabin_no = models.IntegerField(null=True, blank=True)
    emergency_cabin_no = models.IntegerField(null=True, blank=True)
    vip_cabin_no = models.IntegerField(null=True, blank=True)

    # String representation of object
    def __str__(self):
        return str(self.name)
    

class hospital_department(models.Model):
    hospital_department_id = models.AutoField(primary_key=True)
    hospital_department_name = models.CharField(max_length=200, null=True, blank=True)
    # doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    hospital = models.ForeignKey(Hospital_Information, on_delete=models.CASCADE, null=True, blank=True)
    featured_image = models.ImageField(upload_to='departments/', default='departments/default.png', null=True, blank=True)

    def __str__(self):
        val1 = str(self.hospital_department_name)
        val2 = str(self.hospital)
        val3 = val1 + ' - ' + val2
        return str(val3)     

class specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    specialization_name = models.CharField(max_length=200, null=True, blank=True)
    # doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    hospital = models.ForeignKey(Hospital_Information, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        val1 = str(self.specialization_name)
        val2 = str(self.hospital)
        val3 = val1 + ' - ' + val2
        return str(val3)
    
    # def __str__(self):
    #     return str(self.specialization_name)