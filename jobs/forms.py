from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)
    
class RegisterFormEmployer(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=2)
    zip = forms.IntegerField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    