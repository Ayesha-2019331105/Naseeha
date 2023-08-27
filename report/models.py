from django.db import models
from django.db import models
# Import the DoctorInformation model if it's in a separate file
from doctors.models import doctor_info
# Import the Patient model if it's in a separate file
from hospital.models import Patient

# Create your models here.


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    doc_id = models.ForeignKey(doctor_info, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_pdf = models.FileField(upload_to='reports/')

    def __str__(self):
        return f"Report ID: {self.id}, Doctor ID: {self.doc_id}, Patient ID: {self.patient_id}"

# id is defined as the primary key with AutoField to be auto-incremented.
# doc_id is defined as a foreign key that references the DoctorInformation model, and it uses on_delete=models.CASCADE to enforce cascading deletion.
# patient_id is defined as a foreign key that references the Patient model, and it uses on_delete=models.CASCADE to enforce cascading deletion.
# report_pdf is a FileField used to upload and store the report PDF files. The upload_to parameter specifies the directory where the files will be stored.
# Make sure to import the DoctorInformation and Patient models using the appropriate paths to your models.


class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, null=True, blank=True)
    medicine_id = models.CharField(max_length=50)
    medicine_name = models.CharField(max_length=200)
    quantity_per_day = models.PositiveIntegerField()
    duration = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    relation_with_meal = models.CharField(max_length=50)
    instruction = models.TextField()

    def __str__(self):
        return f"Prescription ID: {self.id}, Medicine: {self.medicine_name}, Report ID: {self.report_id}"

# id is defined as the primary key with AutoField to be auto-incremented.
# report is defined as a foreign key that references the Report model, and it uses on_delete=models.CASCADE to enforce cascading deletion.
# medicine_id is a CharField with a maximum length of 50 characters.
# medicine_name is a CharField with a maximum length of 200 characters.
# quantity_per_day is a PositiveIntegerField to store the quantity of medicine per day.
# duration is a CharField with a maximum length of 50 characters.
# frequency is a CharField with a maximum length of 50 characters.
# relation_with_meal is a CharField with a maximum length of 50 characters.
# instruction is a TextField to store any instructions.
# Remember to replace Report with the actual name of the model for the report if it's named differently in your project.
