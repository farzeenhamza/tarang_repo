from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    place = forms.CharField()
    college = forms.CharField()
    mobile_number = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'age', 'gender', 'place', 'college', 'mobile_number')
