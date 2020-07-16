from ..models import Contact


def store_freelancer_contact(freelancer, contact):
    Contact.objects.create(freelancer=freelancer, facebook=contact.facebook, instagram=contact.instagram,
                           whatsapp=contact.whatsapp)
