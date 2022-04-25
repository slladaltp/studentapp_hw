from django import forms


class IndexForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)


class EmailSendForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
    to_email = forms.CharField(max_length=100)
