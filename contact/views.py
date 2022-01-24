from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactForm
from home.views import index
from django.core.mail import send_mail


def contact_view(request):
    """Display the contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message_body = request.POST.get('message', '')
            store_message = f"The following message: {message_body} was sent\
            from the contact form. Please respond to the\
            following email: {email}"
            store_subject = f"Contact form query: {subject}"
            success = (f"Thank you for your inquiry! Your contact information \
            and message was successfully submitted. A confirmation email will \
            be sent to {email}.")
            send_mail(subject, message_body,
                      'chocolatefactory.customercare@gmail.com', [email])
            send_mail(store_subject, store_message,
                      'chocolatefactory.customercare@gmail.com',
                      ['chocolatefactory.customercare@gmail.com'])
            messages.success(request, success)
            return redirect(reverse(index))
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
