from django.shortcuts import render

# Create your views here.


def updates_view(request):
    """ A view to return the index page """

    return render(request, 'updates/updates.html')