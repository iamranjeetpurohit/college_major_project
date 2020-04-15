from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .forms import PostForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def physics(request):
    return render(request, 'phy.html')


def chemistry(request):
    return render(request, 'chem.html')


def maths(request):
    return render(request, 'maths.html')


def it(request):
    return render(request, 'it.html')


def mechanical(request):
    return render(request, 'mecha.html')


def civil(request):
    return render(request, 'civil.html')


def etc(request):
    return render(request, 'etc.html')


def pei(request):
    return render(request, 'pei.html')


def library(request):
    return render(request, 'library.html')


def bus(request):
    title = 'Bus'
    bus_facility = 'As the College is situated on the outskirt of Jorhat Town (approximately 10km.), there are two college buses for students and staff for transportation.'
    bus = True
    para = {'facility': bus_facility, 'title_name': title, 'bus': bus}

    return render(request, 'facility.html', para)


def hostels(request):
    title = 'Hostel'
    hostels = True
    hostel_facility = 'Hostel facilities are available within the campus for both boys and girls students. There is one Girls‘ Hostel and two Boy‘s Hostels. Different types of room sharing modes are available in the college hostel such as room can accommodate either one-two or three students. A bed, a table, a chair and a plug point is provided to each student. Round the clock running water supply in the bathrooms, toilets and electricity is provided to the students at the hostel. The mess facility is arranged and maintained by the students themselves with each hostels having their own cooking utensils, kitchen and dining space. Cleanliness and hygiene is maintained by the adequate number of supporting hostel staff. Both in-door games and out-door games are available for the students in the hostel for recreation of the students.'

    para = {'facility': hostel_facility,
            'title_name': title, 'hostels': hostels}

    return render(request, 'facility.html', para)


def internet(request):
    title = 'Internet'
    internet = True
    internet_facility = 'The Campus and all the hostels and faculty quarters are connected with Lan and Wireless Internet facilities provided by NKN, India.'
    para = {'facility': internet_facility,
            'title_name': title, 'internet': internet}
    return render(request, 'facility.html', para)


def guesthouse(request):
    title = 'Guest House'
    guest = True
    guesthouse = 'JIST, has a very good guest house facility having 2 bed rooms with attached kitchen. It is surrounded by a eco bio-diversity having a pond and botanical garden.'

    para = {'facility': guesthouse, 'title_name': title, 'guest': guest}
    return render(request, 'facility.html', para)


def healthcenter(request):
    title = 'Health Center'
    health = True
    healthcenter = 'The college has a Dispensary with a Doctor (presently vacant), a nurse and a pharmacist within the campus for First-Aid and emergency treatment.'

    para = {'facility': healthcenter, 'title_name': title, 'health': health}
    return render(request, 'facility.html', para)


def notice(request):
    no_details = False
    notice = models.Notice.objects.all()
    if len(notice) == 0:
        no_details = True

    para = {'notice': notice, 'noDetails': no_details}
    return render(request, 'notice.html', para)


def feedback(request):
    no_feedback = False
    feedbacks = models.Feedback.objects.all()
    if len(feedbacks) == 0:
        no_feedback = True
    error = False
    if request.method == 'POST':
        name = request.POST.get('name')
        feedback_desc = request.POST.get('feedback_desc')
        if name == '' or feedback_desc == '':
            error = True
        else:
            error = False
            feedback_details = models.Feedback(
                name=name, feedback=feedback_desc)
            feedback_details.save()
            return HttpResponseRedirect("/feedback")

    para = {'feedbacks': feedbacks, 'noFeedback': no_feedback,
            'error': error}
    return render(request, 'feedback.html', para)


def admindashboard(request):

    registration = models.Student.objects.all()
    registration_number = len(registration)
    notice = models.Notice.objects.all()
    notice_number = len(notice)
    feedback = models.Feedback.objects.all()
    feedback_number = len(feedback)

    para = {'registration_number': registration_number, 'notice_number': notice_number,
            'feedback_number': feedback_number}
    return render(request, 'admindashboard.html', para)


def adminstudents(request):
    no_details = False
    student_details = models.Student.objects.all()
    if len(student_details) == 0:
        no_details = True

    para = {'student': student_details, 'noDetails': no_details}
    return render(request, 'adminstudent.html', para)


def details(request, email):
    error = False
    details = models.Student.objects.filter(email=email)

    if request.method == 'POST':
        details.delete()
        return HttpResponseRedirect('/admindashboard/students')

    para = {'details': details[0], 'error': error}
    return render(request, 'details.html', para)


def adminfeedbacks(request):
    no_details = False
    feedback_details = models.Feedback.objects.all()
    if len(feedback_details) == 0:
        no_details = True

    para = {'feedback_details': feedback_details, 'noDetails': no_details}
    return render(request, 'adminfeedback.html', para)


def adminnotices(request):
    no_details = False
    notice_details = models.Notice.objects.all()
    if len(notice_details) == 0:
        no_details = True

    para = {'notice_details': notice_details, 'noDetails': no_details}
    return render(request, 'adminnotice.html', para)


def addnotice(request):
    success = False
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None,
                        request.FILES or None,)
        if form.is_valid():
            form.save()
            success = True
            # return HttpResponseRedirect('/admindashboard/notices')
    else:
        form = PostForm()

    para = {'form': form, 'success': success}
    return render(request, 'addnotice.html', para)


def notices_edit(request, notice_id):
    error = False
    details = models.Notice.objects.filter(id=notice_id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            details.delete()
            return HttpResponseRedirect('/admindashboard/notices')

        if 'update' in request.POST:
            # details = models.Notice.objects.filter(id=notice_id)
            new_notice = request.POST.get('notice')
            if new_notice == '':
                error = True
            else:
                error = False
                details.update(notice=new_notice)
                return HttpResponseRedirect("/admindashboard/notices")

    para = {'details': details[0], 'error': error}
    return render(request, 'notice_edit.html', para)


def account_sign(request):
    error = False
    error_match = False
    error_exist = False
    error_length = False
    if request.method == 'POST':
        email = request.POST.get('sign-email')
        password = request.POST.get('sign-password')
        con_password = request.POST.get('sign-conpassword')
        if email == '' or password == '' or con_password == '':
            error = True

        if password != con_password:
            error_match = True
        if len(password) < 6:
            error_length = True
        else:
            error = False
            pre_email = models.Account.objects.filter(email=email)

            if len(pre_email) != 0:
                error_exist = True
            else:
                create_acc = models.Account(email=email, password=password)
                create_acc.save()
                return HttpResponseRedirect('/registration/'+email)

    para = {'error': error, 'error_match': error_match,
            'error_exist': error_exist, 'error_length': error_length}
    return render(request, 'account_sign.html', para)


def account_log(request):
    error = False
    error_exist = False
    if request.method == 'POST':
        email = request.POST.get('log-email')
        password = request.POST.get('log-password')

        if email == '' or password == '':
            error = True
        else:
            error = False
            pre_email = models.Account.objects.filter(
                email=email, password=password)

            if len(pre_email) == 0:
                error_exist = True
            else:
                return HttpResponseRedirect('/userdetails/'+email)

    para = {'error': error, 'error_exist': error_exist}
    return render(request, 'account_log.html', para)


def registration(request, email):
    error = False
    error_phone = False
    error_pin = False
    if request.method == 'POST':
        name = request.POST.get('name')
        f_name = request.POST.get('f_name')
        m_name = request.POST.get('m_name')
        user_email = request.POST.get('email')
        gender_num = request.POST.get('gender')
        if gender_num == '1':
            gender = 'Male'
        elif gender_num == '2':
            gender = 'Female'
        else:
            gender = 'Others'
        number = request.POST.get('number')
        address = request.POST.get('address')
        pincode = request.POST.get('pin')

        if name == '' or f_name == '' or m_name == '' or user_email == '' or gender == '' or number == '' or number == '' or address == '' or pincode == '':
            error = True
        else:
            error = False
            if len(number) != 10:
                error_phone = True
            else:
                if len(pincode) != 6:
                    error_pin = True
                else:
                    if email == 'null':
                        student_details = models.Student(name=name, father_name=f_name, mother_name=m_name,
                                                         email=user_email, gender=gender, phone_number=number, address=address, pincode=pincode)
                        student_details.save()
                        return HttpResponseRedirect("/admindashboard/students")
                    else:
                        student_details = models.Student(name=name, father_name=f_name, mother_name=m_name,
                                                         email=email, gender=gender, phone_number=number, address=address, pincode=pincode)
                        student_details.save()
                        
                        return HttpResponseRedirect("/userdetails/"+email)

    para = {'error': error, 'error_phone': error_phone,
            'error_pin': error_pin, 'email': email}
    return render(request, 'registration.html', para)


def account_admin(request):
    error = False
    error_match = False
    if request.method == 'POST':
        name = request.POST.get('admin-email')
        password = request.POST.get('admin-password')
        if name == '' or password == '':
            error = True
        else:
            error = False
            admin_person = models.Admin.objects.filter(
                name=name, password=password)
            if len(admin_person) != 0:
                return HttpResponseRedirect('/admindashboard')
            else:
                error_match = True

    para = {'error': error, 'error_match': error_match}
    return render(request, 'account_admin.html', para)


def userdetails(request, email):
    no_details = False
    data = models.Student.objects.filter(email=email)
    if len(data) == 0:
        no_details = True
        para = {'noDetails': no_details, 'email': email}
    else:
        para = {'data': data[0], 'details': details}

    return render(request, 'userdetails.html', para)


def edituserdetails(request, editemail):
    data = models.Student.objects.filter(email=editemail)
    error = False
    error_phone = False
    error_pin = False
    if request.method == 'POST':
        name = request.POST.get('name')
        f_name = request.POST.get('f_name')
        m_name = request.POST.get('m_name')
        gender_num = request.POST.get('gender')
        if gender_num == '1':
            gender = 'Male'
        elif gender_num == '2':
            gender = 'Female'
        else:
            gender = 'Others'
        number = request.POST.get('number')

        address = request.POST.get('address')
        pincode = request.POST.get('pin')

        if name == '' or f_name == '' or m_name == '' or gender == '' or number == '' or number == '' or address == '' or pincode == '':
            error = True
        else:
            error = False
            if len(number) != 10:
                error_phone = True
            else:
                if len(pincode) != 6:
                    error_pin = True
                else:
                    data.update(name=name, father_name=f_name, mother_name=m_name,
                                email=editemail, gender=gender, phone_number=number, address=address, pincode=pincode)

                    return HttpResponseRedirect("/admindashboard/students")

    para = {'error': error, 'error_phone': error_phone,
            'error_pin': error_pin, 'data': data[0]}

    return render(request, 'edituserdetails.html', para)
