from ..models import Freelancer


def store(p_freelancer):
    freelancer = Freelancer(name=p_freelancer.name, username=p_freelancer.username, biography=p_freelancer.biography,
                            email=p_freelancer.email, password=p_freelancer.password)
    freelancer.save()
