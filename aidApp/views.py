from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .forms import CreateContactForm #,DocProfileForm, AppCreateForm, AppUpdateForm, AppRetrieveForm 


def index(request):
    return render(request, 'aidApp/contact/index.html') #, HttpResponse("<h1>Medical Aid app Homepage</h1>")


def CreateContact(request):
    
    context = {}
    submitted = False
    
    if request.method == 'POST':
         form = CreateContactForm(request.POST)
         if form.is_valid():
             
             subject = form.cleaned_data['subject']
             message = form.cleaned_data['your_message']
             sender = form.cleaned_data['your_email']
             
             administrators = []
             for admin in User.objects.filter(is_superuser=True):
                administrators.append(admin.email)
            
             con = get_connection('django.core.mail.backends.console.EmailBackend')
             send_mail(subject,
                      message,
                      sender,
                      administrators,
                      connection=con            
             )
             form.save()
             return HttpResponseRedirect('?submitted=True')
         
         else:
             
             return render(request,'aidApp/contact/contact.html',{'form': form, 'submitted': submitted})
 
    context = {'form': CreateContactForm()}
    return render(request, 'aidApp/contact/contact.html', context) 


 