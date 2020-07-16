from django import forms
from .models import Freelancer


class FreelancerForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=150, min_length=3, empty_value=False, required=True)
    username = forms.CharField(label='Username', max_length=45, min_length=3, empty_value=False, required=True,
                               help_text='People will be able to find you directly by your username.', error_messages=
                               {'required': 'Erro'})
    biography = forms.CharField(label='Biography', widget=forms.Textarea(attrs={'rows': 3}), max_length=400,
                                empty_value=False, required=True)
    email = forms.EmailField(label='Email', max_length=200, empty_value=False, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=50, min_length=8,
                               empty_value=False, required=True)

    class Meta:
        model = Freelancer
        fields = ['name', 'username', 'biography', 'email', 'password']
