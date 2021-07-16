from django import forms


class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(label="Contact_info", required=True, widget=forms.TextInput)
