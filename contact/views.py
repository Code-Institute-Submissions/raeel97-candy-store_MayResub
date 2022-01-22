from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactForm
from home.views import index
from django.core.mail import send_mail
from chocolate_factory.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def contact_view(request):
    """Display the contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message_body = request.POST.get('message', '')
            error = 'Did you fill in the form correctly?'
            success = (f"Thank you for your inquiry! Your contact information \
            and message was successfully submitted. A confirmation email will \
            be sent to {email}.")
            send_mail(subject, message_body,
            'chocolatefactory.customercare@gmail.com', [email])
            except Exception as e:
                messages.warning(request, error)
                return redirect(reverse(contact_view))
            print(f'this is the email: {email}')
            print(f'this is the subject: {subject}')
            print(f'this is the message_body: {message_body}')
            messages.success(request, success)
            return redirect(reverse(index))
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
