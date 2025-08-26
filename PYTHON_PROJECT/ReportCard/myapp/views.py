from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Paginator is a class that provides pagination functionality for a queryset, allowing you to split large datasets 
# into smaller, manageable pages.  link: https://docs.djangoproject.com/en/5.2/topics/pagination/
from django.core.paginator import Paginator

from django.db.models import Sum

# Create your views here.

def index(request):
    allstudent = Student.objects.all()
    # return render(request, 'index.html', {"students":allstudent})

    
    # Paginator takes two arguments: the queryset to paginate and the number of items per page.
    # In this case, we are paginating the 'allstudent' queryset and displaying 5 students per page.
    # The 'page_number' variable retrieves the current page number from the request's GET parameters    
    paginator = Paginator(allstudent, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {"students":page_obj})

def marksheet(request):
    studentid = int(request.GET['id'])
    # print(studentid)
    allstudent = Marks.objects.filter(student_id=studentid)
    # print(allstudent)
    # sum=0
    # for st in allstudent:
    #     # print(st.marks)
    #     sum += st.marks
    # # print(sum)


    
    sum = allstudent.aggregate(total = Sum("marks"))
    # print(sum)
    rankstudents = Student.objects.annotate(total = Sum('marks__marks')).order_by("-total")
    count = 0
    for ranks in rankstudents:
        count += 1
        if ranks.id == studentid:
            # print(ranks.total, ranks.id, count)
            break
            
    return render(request, 'marksheet.html', {"students":allstudent, "sum":sum, "count":count})


# Gmail sending code 
# link:- https://www.geeksforgeeks.org/python/setup-sending-email-in-django-project/
def send_mail_page(request):
    context = {}

    if request.method == 'GET':
        # address = request.POST.get('address')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')

        address = "drashtimodi33@gmail.com" 
        subject = "Test Email from Django"
        message = "This is a test email sent from a Django application."

        # print(settings.EMAIL_HOST_USER)
        
        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return HttpResponse(context['result'])