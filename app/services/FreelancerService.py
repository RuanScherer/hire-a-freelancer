from ..models import Freelancer
from django.db.models import Q


def store(p_freelancer):
    freelancer = Freelancer(name=p_freelancer.name, username=p_freelancer.username, biography=p_freelancer.biography,
                            email=p_freelancer.email, password=p_freelancer.password)
    freelancer.save()


def last_registered():
    return Freelancer.objects.order_by('-id')


def show(search):
    return Freelancer.objects.filter(Q(name__contains=search) | Q(username__contains=search) |
                                     Q(biography__contains=search))
