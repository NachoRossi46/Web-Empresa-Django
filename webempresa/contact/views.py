from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Se envia correo y redirecciona
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["nachorossi121@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()            
                return redirect(reverse('contact')+ "?ok")
            except:
                # Algo no ha salido bien, redirecciona a FAIL
                return redirect(reverse('contact')+ "?fail")             
    return render(request, "contact/contact.html", {'form': contact_form})
