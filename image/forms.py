from django import forms


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=140)
    picture = forms.ImageField()