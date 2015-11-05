from django import forms
from .models import Customer, Product
from django_countries.widgets import CountrySelectWidget
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _

import datetime

class RegistrationForm(forms.ModelForm):
    class Meta:
        this_year = datetime.date.today().year
        yr_choice = []
        for yr in range(1920, int(this_year)):
            yr_choice.append(yr)

        model = Customer
        fields = '__all__'
        exclude=['date_registered', 'cart']
        widgets = {

            'birth_date': SelectDateWidget(years=yr_choice),
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
            'country': CountrySelectWidget(),

        }

    def clean_email(self):
        email_entered = self.cleaned_data.get('email')
        if Customer.objects.filter(email=email_entered).exists():
            raise forms.ValidationError("Please use another email, that one exists")
        return email_entered

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return confirm_password


class SignInForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'password', ]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("Please first register")
        return email

    def clean_password(self):
        email_entered = self.cleaned_data.get('email')
        password_entered = self.cleaned_data.get('password')
        customers = Customer.objects.filter(email=email_entered)
        for person in customers:
            if person.email == email_entered and person.password == password_entered:
                pass
            else:
                raise forms.ValidationError("Incorrect login details")
        return password_entered

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {

            'expiry_date': SelectDateWidget(),
            'updated_at': SelectDateWidget(),
        }
