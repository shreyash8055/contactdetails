
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            email = EmailMessage(
                subject=f"New Contact Form Submission from {contact.name}",
                body=f"Message:\n{contact.message}\n\nReply to: {contact.email}",
                from_email=settings.EMAIL_HOST_USER,  # must match Mailtrap config
                to=[settings.EMAIL_HOST_USER,'shreyash1833@gmail.com'],         # where you want to receive mail
                reply_to=[settings.EMAIL_HOST_USER]            # allows you to reply directly to user
            )
            email.send(fail_silently=False)

            return render(request, 'contact/thank_you.html')

    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})
