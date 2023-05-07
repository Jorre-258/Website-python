from django import forms

class Create_New_List(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField()

