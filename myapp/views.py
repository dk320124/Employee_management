from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    isActive=True
    if request.method=="POST":
        check=request.POST['check']
        print(check)

        if check is None: isActive=False
        else: isActive=True

    date=datetime.datetime.now()
    
    name="deepak kumar"
    list_of_programs=[
        'wap to check even or odd',
        'wap to check prime number',
        'wap to print all prime number from 0 to 100',
        'wap to print pascals tringle'
    ]
    student={
        'student_name':"rahul",
        'student_college':"rits",
        'student_city':"darbhanga"

    }
    # return HttpResponse("<h1>this is index page</h1>"+str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student

    }
    return render(request, "home.html", data)

# def about(request):
#     # return HttpResponse("<h1>this is a about page</h1>")
#     return render(request, "about.html")

# def services(request):
#     #return HttpResponse("<h1>this is a services page</h1>")
#     return render(request, "services.html")