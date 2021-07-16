from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth import get_user_model


User = get_user_model()
username_validator = UnicodeUsernameValidator()

#
# def tel_validator(value):
#     if value != "+375123456789":
#         raise ValidationError
#     pass


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Username")
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': "new-password"}),
        help_text="Enter the same password as before"
    )
    tel = forms.CharField(max_length=24, required=True, label="tel number", help_text="+375123456789")

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "Что-то пошло не так ... может введены разные пороли?",
                code='password_mismatch'
            )
        try:
            validate_password(password2, User)
        except ValidationError as error:
            self.add_error('password2', error)
        return password2
