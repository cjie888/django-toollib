from django import forms
from toollib.verificationcode  import VerificationCodeField, VerificationCodeTextInput

class VerificationCodeForm(forms.Form):
    verificationcode = VerificationCodeField(widget=VerificationCodeTextInput({"class": "test"}))
