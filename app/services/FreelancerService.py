from ..models import Freelancer, Contact, Rate
from django.db.models import Q, Avg
from .ContactService import store_freelancer_contact
from math import ceil


def store(p_freelancer, p_contact):
    freelancer = Freelancer(name=p_freelancer.name, username=p_freelancer.username, biography=p_freelancer.biography,
                            email=p_freelancer.email)
    freelancer.save()
    store_freelancer_contact(freelancer, p_contact)


def last_registered():
    freelancers = Freelancer.objects.order_by('-id')[:6]
    for freelancer in freelancers:
        rate = Rate.objects.filter(freelancer=freelancer.id).aggregate(Avg('rate'))
        if rate["rate__avg"] is not None:
            freelancer.rate = ceil(rate["rate__avg"])
        else:
            freelancer.rate = 0
    return freelancers


def show(search):
    freelancers = Freelancer.objects.filter(Q(name__contains=search) | Q(username__contains=search) |
                                            Q(biography__contains=search))
    for freelancer in freelancers:
        rate = Rate.objects.filter(freelancer=freelancer.id).aggregate(Avg('rate'))
        if rate["rate__avg"] is not None:
            freelancer.rate = ceil(rate["rate__avg"])
        else:
            freelancer.rate = 0
    return freelancers


def get_details(id):
    try:
        freelancer = Freelancer.objects.get(id=id)
        try:
            freelancer_contact = Contact.objects.get(freelancer=id)
            freelancer_data = {'freelancer': freelancer, 'contact': freelancer_contact}
        except Contact.DoesNotExist:
            freelancer_data = {'freelancer': freelancer, 'contact': False}
    except Freelancer.DoesNotExist:
        return False
    return freelancer_data
