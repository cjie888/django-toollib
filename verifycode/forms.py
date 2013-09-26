from django import forms
from toollib.verificationcode  import VerificationCodeField, VerificationCodeTextInput

class CaptchaForm(forms.Form):
    captcha = VerificationCodeField(widget=VerificationCodeTextInput({"class": "test"}))
