from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  
            send_mail(
                subject=f"New Contact Form Submission from {contact.name}",
                message=contact.message,
                from_email=contact.email,
                recipient_list=[settings.ADMIN_EMAIL],
            )
            return render(request, 'contact/thank_you.html') 
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})
