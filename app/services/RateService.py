from ..models import Rate


def store(p_rate):
    rate = Rate(freelancer=p_rate.freelancer, rate=p_rate.rate)
    rate.save()
    return rate
