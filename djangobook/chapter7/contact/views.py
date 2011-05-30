#coding:utf8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from chapter7.contact.forms import ContactForm

def contact(request):
    errors = []
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            """
            実際に使用するためにはDjangoでmailに関する設定をする
            必要があるため使用しない
            send_mail(
                    cd["subject"],
                    cd["message"],
                    cd.get("email","noreply@example.com"),
                    ['siteowner@exsample.com'],
                    )
            """
            return HttpResponseRedirect("/contact/thanks/")
    else:
        form = ContactForm(
                initial={"subject":"I love your site!"})
    return render_to_response("contact_form.html",{"form":form})

def thanks4Contact(request):
    return HttpResponse("Thank you!!")
