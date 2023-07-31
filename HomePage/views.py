from django.shortcuts import render
from HomePage.models import Contact,AboutUs

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    context ={}
    if request.method == "POST":
        title1 = request.POST.GET("title1")
        desc1 = request.POST.GET("desc1")

        title2 = request.POST.GET("title2")
        desc2 = request.POST.GET("desc2")

        title3 = request.POST.GET("title3")
        desc3 = request.POST.GET("desc3")

        ceo_name = request.POST.GET("ceo_name")
        ceo_desc = request.POST.GET("ceo_desc")

        about = AboutUs(title1=title1,desc1=desc1,title2=title2,desc2=desc2,title3=title3,desc3=desc3,ceo_name=ceo_name,ceo_desc=ceo_desc)
        about.save()

        context = {'about':about}

    return render(request, 'about.html', context)

def contact_us(request):
    context = {}
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        em = request.POST.get("email")
        ph = request.POST.get("phone")
        sub = request.POST.get("subject")
        mess = request.POST.get("message")
        obj = Contact(fname=fname, lname=lname, email=em,phone=ph, subject=sub, message=mess)
        
        obj.save()
        context['message'] = f"Dear {fname}, Thank you for your time !"

    return render(request, 'contact.html', context)


def service(request):
    return render(request, 'service.html')


def menu(request):
    return render(request, 'menu.html')


def advice(request):
    return render(request, 'advice.html')
