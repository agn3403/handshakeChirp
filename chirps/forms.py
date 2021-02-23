from django import forms


class ChirpForm(forms.Form):
    text = forms.CharField(max_length=140)
    # id = forms.IntegerField()

