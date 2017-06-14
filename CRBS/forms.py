from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=15)
    last_name = forms.CharField(label='Last Name', max_length=15)
    designation = forms.CharField(label='Designation', max_length=30)
    email = forms.EmailField(label='Email Address', max_length=30)
    password = forms.CharField(label='Password', max_length=20)


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email Address', max_length=30)
    password = forms.CharField(label='Password', max_length=20)