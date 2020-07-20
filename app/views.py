from django.shortcuts import render, redirect
from .forms import FreelancerForm, FreelancerSearchForm, ContactForm, RateForm
from .models import Freelancer, Contact, Rate
from .services import FreelancerService, RateService


# Create your views here.

def show_landing(request):
    last_registered = FreelancerService.last_registered()
    print(last_registered)
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
            registered_freelancer = FreelancerService.store(new_freelancer, new_contact)
            return redirect(f'{registered_freelancer.id}/freelancer')
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


def show_freelancer_details(request, id):
    freelancer = FreelancerService.get_details(id)
    return render(request, 'freelancer-details/index.html', {'freelancer': freelancer})


def show_rate_a_freelancer(request, id):
    freelancer = FreelancerService.get_details(id)
    if request.method == "POST":
        post = request.POST.copy()
        post["freelancer"] = freelancer["freelancer"]
        rate_form = RateForm(post)
        if rate_form.is_valid():
            freelancer = freelancer["freelancer"]
            rate = rate_form.cleaned_data["rate"]
            new_rate = Rate(freelancer=freelancer, rate=rate)
            RateService.store(new_rate)
            return redirect('app:success')
        else:
            return render(request, 'rate-a-freelancer/index.html', {'freelancer': freelancer, 'error': True})
    return render(request, 'rate-a-freelancer/index.html', {'freelancer': freelancer})


def show_rate_success(request):
    return render(request, 'rate-success/index.html')
