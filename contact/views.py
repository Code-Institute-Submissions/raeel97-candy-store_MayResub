from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactForm
from home.views import index


def contact_view(request):
    """Display the contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email', '')
            success = (f"Thank you for your inquiry! Your contact information \
            and message was successfully submitted. A confirmation email will \
            be sent to {email}.")
            messages.success(request, success)
            return redirect(reverse(index))
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
