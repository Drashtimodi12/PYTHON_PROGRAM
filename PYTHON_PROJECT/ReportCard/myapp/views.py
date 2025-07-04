from django.shortcuts import render
from myapp.models import *

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