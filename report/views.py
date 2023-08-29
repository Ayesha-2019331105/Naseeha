from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt
from hospital.models import *
from doctors.models import *
from interactions.models import *
from .models import *
from django.core.files.base import ContentFile

# Create your views here.


def report_info(request):
    email = request.GET['name']
    p = Patient.objects.get(email=email)
    print(p.name)
    stories = p.history.split('\n')
    myP = {
        'pid': p.Patient_id,
        'name': p.name,
        'story': stories
    }
    print(myP.get('story'))
    return render(request, "createpdf/reportinfo.html", {'myP': myP})


@csrf_exempt
def pdf_report_create(request):

    if request.method == "POST":
        doc_name = request.POST.get("doc_name")
        doc_email = request.POST.get("doc_email")
        doc_model = doctor_info.objects.get(email=doc_email)
        pres_id = request.POST.get("pres_id")
        pid = request.POST.get("pid")
        p_model = Patient.objects.get(Patient_id=pid)
        p_name = request.POST.get("name")
        med_name = request.POST.get("med_name")
        med_quantity_per_day = request.POST.get("med_quantity_per_day")
        duration = request.POST.get("duration")
        med_frequency = request.POST.get("med_frequency")
        med_test = request.POST.get("med_test")
        instruction = request.POST.get("instruction")
        report = Report.objects.create(
            doc_id=doc_model,
            patient_id=p_model,
        )
        context = {
            'doc_name': doc_name,
            'clinic': doc_model.work_place,
            "doc_email": doc_email,
            "pres_id": pres_id,
            "pid": pid,
            "p_name": p_name,
            "med_name": med_name,
            "med_quantity": med_quantity_per_day,
            "duration": duration,
            "med_frequency": med_frequency,
            "med_test": med_test,
            "instruction": instruction,
            "age": p_model.age,
            "pemail": p_model.email
        }

        template_path = 'createpdf/reportpdf.html'

        response = HttpResponse(content_type='application/pdf')
        report_pdf_name = f"report_{pid}.pdf"

        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        template = get_template(template_path)

        html = template.render(context)

        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)

        # create a pdf
        # pisa_status = pisa.CreatePDF(
        #     html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        # Save the PDF content into the report_pdf field
        # Choose an appropriate filename
        report.report_pdf.save(
            report_pdf_name, ContentFile(pdf_buffer.getvalue()))
        # report.report_pdf.save('report.pdf', response)
        return response


def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reportlist.html', {'reports': reports})
