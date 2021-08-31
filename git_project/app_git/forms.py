from django import forms

class DataForm(forms.Form):
    user_name=forms.CharField(max_length=255)