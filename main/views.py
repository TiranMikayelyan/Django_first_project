from django.shortcuts import render
from . models import Main, Testimonials,Gall,Gallery,Contact,last

# Create your views here.


def index(request):
    main_list = Main.objects.all().first()
    Testimonials_list = Testimonials.objects.all()
    gall_list = Gall.objects.all().first()
    gallery_list = Gallery.objects.all()
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        Contact.objects.create(name = user_name, email = user_email, message = user_message)
    last_list = last.objects.all().first()
    return render(request, 'main/index.html', context={
     'main_list':main_list,
     'Testimonials_list':Testimonials_list,
     'gall_list':gall_list,
     'gallery_list': gallery_list,
     'last_list':last_list
             })