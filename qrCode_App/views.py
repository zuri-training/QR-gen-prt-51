import os
import base64
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from urllib.parse import quote
from PIL import Image
from django.contrib.auth.decorators import login_required
from qrCode_App.models import QrCode
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
# Create your views here.


class LandingPageView(TemplateView):
    template_name = "pages/landingPage.html"


class FAQPageView(TemplateView):
    template_name = 'pages/faq.html'


class CONTACTPageView(TemplateView):
    template_name = 'pages/contactus.html'


class ABOUTPageView(TemplateView):
    template_name = 'pages/aboutUs.html'


# custom views for error pages
def custom_page_not_found_view(request, exception):
    return render(request, "404.html")


def custom_error_view(request, exception=None):
    return render(request, "404.html")


def custom_permission_denied_view(request, exception=None):
    return render(request, "404.html")


def custom_bad_request_view(request, exception=None):
    return render(request, "404.html")


# A function to create input for pre-defined SMS messages
def create_sms_input(number, message=""):
    return "sms:{0}?body={1}".format(number, quote(message))


# A function to create input for pre-defined email messages
def create_email_input(email, subject="", message=""):
    return "mailto:{0}?subject={1}&body={2}".format(email, quote(subject),
                                                    quote(message))


#A python function to know whether it is morning, afternoon or evening
def get_time_of_day():
    now = datetime.datetime.now()
    if now.hour < 12:
        return "morning"
    elif 12 <= now.hour < 18:
        return "afternoon"
    else:
        return "evening"

# Convert to JPEG
def convert_to_jpeg(path):
    image = Image.open(path)
    rgb_image = image.convert('RGB')
    jpeg_image = rgb_image.save(path.replace('.png', '.jpeg'), 'JPEG')
    return path.replace('.png', '.jpeg'), os.path.basename(path.replace('.png', '.jpeg'))

# Convert to SVG
def convert_to_svg(path):
    startSvgTag = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
    "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="240px" height="240px" viewBox="0 0 240 240">"""
    endSvgTag = """</svg>"""
    pngFile = open(path, 'rb')
    base64data = base64.b64encode(pngFile.read())
    base64String = '<image xlink:href="data:image/png;base64,{0}" width="240" height="240" x="0" y="0" />'.format(base64data.decode('utf-8'))
    f = open(path.replace('.png', '.svg'), 'w')
    f.write(startSvgTag + base64String + endSvgTag)
    f.close()
    return path.replace('.png', '.svg'), os.path.basename(path.replace('.png', '.svg'))


# Convert to PDF
def convert_to_pdf(path):
    image = Image.open(path)
    rgb_image = image.convert('RGB')
    pdf_image = rgb_image.save(path.replace('.png', '.pdf'), 'PDF')
    return path.replace('.png', '.pdf'), os.path.basename(path.replace('.png', '.pdf'))




# view to generate different qr codes for different users
@login_required(login_url='/accounts/login/')
def datatype(request):
    return render(request, 'pages/datatype.html')


@login_required(login_url='/accounts/login/')
def popular(request):
    if 'website-url' in request.POST:
        qrtype = "Website URL"
    elif 'plain-text' in request.POST:
        qrtype = "Plain Text"
        request.session['urlqrtype'] = qrtype
        return redirect('texttype')
    elif 'pdf-file' in request.POST:
        qrtype = "PDF File"
    request.session['urlqrtype'] = qrtype
    return redirect('urltype')


@login_required(login_url='/accounts/login/')
def social_links(request):
    if 'youtube' in request.POST:
        qrtype = "YouTube"
    elif 'instagram' in request.POST:
        qrtype = "Instagram"
    elif 'whatsapp' in request.POST:
        qrtype = "WhatsApp"
    elif 'facebook' in request.POST:
        qrtype = "Facebook"
    elif 'linkedin' in request.POST:
        qrtype = "LinkedIn"
    elif 'twitter' in request.POST:
        qrtype = "Twitter"
    request.session['urlqrtype'] = qrtype
    return redirect('urltype')


@login_required(login_url='/accounts/login/')
def business_links(request):
    if 'phone-number' in request.POST:
        qrtype = "Phone Number"
        request.session['urlqrtype'] = qrtype
        return redirect('phonetype')
    elif 'email-address' in request.POST:
        qrtype = "Email Address"
        request.session['urlqrtype'] = qrtype
        return redirect('emailtype')


@login_required(login_url='/accounts/login/')
def predefined_message(request):
    if 'pre-sms' in request.POST:
        qrtype = "Predefined SMS"
        request.session['urlqrtype'] = qrtype
        return redirect('presmstype')
    elif 'pre-email' in request.POST:
        qrtype = "Predefined Email"
        request.session['urlqrtype'] = qrtype
        return redirect('preemailtype')


@login_required(login_url='/accounts/login/')
def urltype(request):
    if request.method == 'POST':
        qr_code_text = request.POST['url-for-code']
        qrtype = request.session.get('urlqrtype')
        qr_msg = "Link to a {0}".format(qrtype)
        QrCode.objects.create(user=request.user,
                              qr_code_text=qr_code_text,
                              qr_msg=qr_msg,
                              qr_type=qrtype)
        qr_content = QrCode.objects.filter(
            user=request.user).order_by('-id')[0].qr_code_text
        request.session['qr_code'] = qr_content
        return redirect('success')
    return render(request, 'components/urltype.html')


@login_required(login_url='/accounts/login/')
def texttype(request):
    if request.method == 'POST':
        qr_code_text = request.POST['text-for-code']
        qrtype = request.session.get('urlqrtype')
        qr_msg = "Link to a {0}".format(qrtype)
        QrCode.objects.create(user=request.user,
                              qr_code_text=qr_code_text,
                              qr_msg=qr_msg,
                              qr_type=qrtype)
        qr_content = QrCode.objects.filter(
            user=request.user).order_by('-id')[0].qr_code_text
        request.session['qr_code'] = qr_content
        return redirect('success')
    return render(request, 'components/texttype.html')


@login_required(login_url='/accounts/login/')
def phonetype(request):
    if request.method == 'POST':
        qr_code_text = request.POST['phone-for-code']
        qrtype = request.session.get('urlqrtype')
        qr_msg = "Business link to a {0}".format(qrtype)
        QrCode.objects.create(user=request.user,
                              qr_code_text=qr_code_text,
                              qr_msg=qr_msg,
                              qr_type=qrtype)
        qr_content = QrCode.objects.filter(
            user=request.user).order_by('-id')[0].qr_code_text
        request.session['qr_code'] = qr_content
        return redirect('success')
    return render(request, 'components/phonetype.html')


@login_required(login_url='/accounts/login/')
def emailtype(request):
    if request.method == 'POST':
        qr_code_text = request.POST['email-for-code']
        qrtype = request.session.get('urlqrtype')
        qr_msg = "Business link to {0}".format(qrtype)
        QrCode.objects.create(user=request.user,
                              qr_code_text=qr_code_text,
                              qr_msg=qr_msg,
                              qr_type=qrtype)
        qr_content = QrCode.objects.filter(
            user=request.user).order_by('-id')[0].qr_code_text
        request.session['qr_code'] = qr_content
        return redirect('success')
    return render(request, 'components/emailtype.html')


@login_required(login_url='/accounts/login/')
def preemailtype(request):
    if request.method == 'POST':
        email_address = request.POST['preemail-for-code']
        email_subject = request.POST['email-subject']
        email_message = request.POST['email-message']
        qr_code_text = create_email_input(email_address, email_subject,
                                          email_message)
        qrtype = request.session.get('urlqrtype')
        qr_msg = "Predefined Email"
        QrCode.objects.create(user=request.user,
                              qr_code_text=qr_code_text,
                              qr_msg=qr_msg,
                              qr_type=qrtype)
        qr_content = QrCode.objects.filter(
            user=request.user).order_by('-id')[0].qr_code_text
        request.session['qr_code'] = qr_content
        return redirect('success')
    return render(request, 'components/preemailtype.html')


@login_required(login_url='/accounts/login/')
def presmstype(request):
    if request.method == 'POST':
        phone_number = request.POST['number-for-code']
        sms_message = request.POST['sms-message']
        qr_code_text = create_sms_input(phone_number, sms_message)
        qrtype = request.session.get('urlqrtype')
        qr_msg = "Predefined SMS to {0}".format(phone_number)
        QrCode.objects.create(user=request.user,
                              qr_code_text=qr_code_text,
                              qr_msg=qr_msg,
                              qr_type=qrtype)
        qr_content = QrCode.objects.filter(
            user=request.user).order_by('-id')[0].qr_code_text
        request.session['qr_code'] = qr_content
        return redirect('success')
    return render(request, 'components/presmstype.html')


@login_required(login_url='/accounts/login/')
def dashboard(request):
    day = get_time_of_day()
    first_name = request.user.full_name.split(" ")[0]

    qr_code = QrCode.objects.filter(user=request.user).order_by('-id')
    return render(request, 'pages/dashboard.html', {
        'qr_code': qr_code,
        'first_name': first_name,
        'day': day
    })

@login_required(login_url='/accounts/login/')
def code_detail(request, pk):
    day = get_time_of_day()
    first_name = request.user.full_name.split(" ")[0]
    qr_code_selected = get_object_or_404(QrCode.objects.filter(user=request.user), pk=pk)
    qr_code = QrCode.objects.filter(user=request.user).order_by('-id')
    return render(request, 'pages/code_detail.html', {
        'qr_code_selected': qr_code_selected,
        'qr_code': qr_code,
        'first_name': first_name,
        'day': day
    })

@login_required(login_url='/accounts/login/')
def code_download_png(request, pk):
    obj = get_object_or_404(QrCode.objects.filter(user=request.user), pk=pk)
    filepath = obj.qr_code.path
    filename = obj.qr_code.name
    response = HttpResponse(open(filepath, 'rb').read(), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

@login_required(login_url='/accounts/login/')
def code_download_svg(request, pk):
    obj = get_object_or_404(QrCode.objects.filter(user=request.user), pk=pk)
    filepath, filename = convert_to_svg(obj.qr_code.path)
    response = HttpResponse(open(filepath, 'rb').read(), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

@login_required(login_url='/accounts/login/')
def code_download_jpeg(request, pk):
    obj = get_object_or_404(QrCode.objects.filter(user=request.user), pk=pk)
    filepath, filename = convert_to_jpeg(obj.qr_code.path)
    response = HttpResponse(open(filepath, 'rb').read(), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

@login_required(login_url='/accounts/login/')
def code_download_pdf(request, pk):
    obj = get_object_or_404(QrCode.objects.filter(user=request.user), pk=pk)
    filepath, filename = convert_to_pdf(obj.qr_code.path)
    response = HttpResponse(open(filepath, 'rb').read(), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

@login_required(login_url='/accounts/login/')
def code_edit(request,pk):
    qr_code_selected = get_object_or_404(QrCode.objects.filter(user=request.user), pk=pk)
    return render(request, 'pages/customizeqr.html', {'qr_code_selected': qr_code_selected})

@login_required(login_url='/accounts/login/')
def success(request):
    latest_qr_code = QrCode.objects.filter(user=request.user).order_by('-id')[0]
    return render(request, 'components/successPage.html', {'latest_qr_code': latest_qr_code})


@login_required(login_url='/accounts/login/')
def resetall(request):
    QrCode.objects.filter(user=request.user).delete()
    return redirect('dashboard')

# django contact form 
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'],
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())
			try:
				send_mail(subject, message, 'petsamuel4@example.com', ['bieefilled@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("index")
	form = ContactForm()
	return render(request, "pages/contactus.html", {'form':form})
