from django.shortcuts import render, redirect
from .forms import FreelancerForm, FreelancerSearchForm
from .models import Freelancer
from .services import FreelancerService


# Create your views here.

def show_landing(request):
    last_registered = FreelancerService.last_registered()
    return render(request, 'landing/index.html', {'last_registered': last_registered})


def show_register(request):
    if request.method == "POST":
        freelancer_form = FreelancerForm(request.POST)
        if freelancer_form.is_valid():
            name = freelancer_form.cleaned_data["name"]
            username = freelancer_form.cleaned_data["username"]
            biography = freelancer_form.cleaned_data["biography"]
            email = freelancer_form.cleaned_data["email"]
            password = freelancer_form.cleaned_data["password"]
            new_freelancer = Freelancer(name=name, username=username, biography=biography, email=email,
                                        password=password)
            FreelancerService.store(new_freelancer)
            return redirect('login')
    else:
        freelancer_form = FreelancerForm()
    return render(request, 'register/index.html', {'freelancer_form': freelancer_form})


def show_freelancers(request):
    if request.method == "GET":
        freelancer_search_form = FreelancerSearchForm(request.GET)
        if freelancer_search_form.is_valid():
            search = freelancer_search_form.cleaned_data["search"]
            freelancers = FreelancerService.show(search)
            return render(request, 'search-freelancers/index.html', {'freelancers': freelancers})
