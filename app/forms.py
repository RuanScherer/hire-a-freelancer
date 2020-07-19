from django import forms
from .models import Freelancer, Contact


class FreelancerForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=150, min_length=3, empty_value=False, required=True)
    username = forms.CharField(label='Username', max_length=45, min_length=3, empty_value=False, required=True,
                               help_text='People will be able to find you directly by your username.')
    biography = forms.CharField(label='Biography', widget=forms.Textarea(attrs={'rows': 3}), max_length=400,
                                empty_value=False, required=True, help_text='Speak objectively about yourself and your '
                                                                            'work. (Max. 400 characters)')
    email = forms.EmailField(label='Email', max_length=200, empty_value=False, required=True)

    class Meta:
        model = Freelancer
        fields = ['name', 'username', 'biography', 'email']


class FreelancerSearchForm(forms.ModelForm):
    search = forms.CharField(empty_value=False, required=True)

    class Meta:
        model = Freelancer
        fields = ['search']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['freelancer']
