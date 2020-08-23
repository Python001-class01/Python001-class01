from django import forms

class LoginForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput,
                                 min_length=8)