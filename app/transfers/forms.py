from django import forms

from .models import Transfer


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['email', 'password', 'expiry_date']

    files = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )
