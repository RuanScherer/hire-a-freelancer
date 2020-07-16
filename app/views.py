from django.shortcuts import render, redirect
from .forms import FreelancerForm, FreelancerSearchForm, ContactForm
from .models import Freelancer, Contact
from .services import FreelancerService


# Create your views here.

def show_landing(request):
    last_registered = FreelancerService.last_registered()
    return render(request, 'landing/index.html', {'last_registered': last_registered})


def show_register(request):
    if request.method == "POST":
        freelancer_form = FreelancerForm(request.POST)
        contact_form = ContactForm(request.POST)
        if freelancer_form.is_valid() and contact_form.is_valid():
            name = freelancer_form.cleaned_data["name"]
            username = freelancer_form.cleaned_data["username"]
            biography = freelancer_form.cleaned_data["biography"]
            email = freelancer_form.cleaned_data["email"]
            new_freelancer = Freelancer(name=name, username=username, biography=biography, email=email)
            facebook = contact_form.cleaned_data["facebook"]
            instagram = contact_form.cleaned_data["instagram"]
            whatsapp = contact_form.cleaned_data["whatsapp"]
            new_contact = Contact(facebook=facebook, instagram=instagram, whatsapp=whatsapp)
            FreelancerService.store(new_freelancer, new_contact)
            return redirect('landing')
    else:
        freelancer_form = FreelancerForm()
        contact_form = ContactForm()
    return render(request, 'register/index.html', {'freelancer_form': freelancer_form, 'contact_form': contact_form})


def show_freelancers(request):
    if request.method == "GET":
        freelancer_search_form = FreelancerSearchForm(request.GET)
        if freelancer_search_form.is_valid():
            search = freelancer_search_form.cleaned_data["search"]
            freelancers = FreelancerService.show(search)
            return render(request, 'search-freelancers/index.html', {'freelancers': freelancers})
