from django.shortcuts import render
from .models import *

# Create your views here.
def show_contact(request):
    context = {}
    all_contacts = Contact.objects.all()
    context['all_contacts'] = all_contacts
    return render (request, 'contacts.html', context)