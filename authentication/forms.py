from authentication.models import User
from django import forms


class CreateUserForm(forms.ModelForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.required = True

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "type",
            "profile_image",
            "password1",
            "password2"
            ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
                }),
            "last_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
                }),
            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
                }),
            "password1": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
                }),
            "password2": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
                }),
            "type": forms.Select(attrs={
                'class': 'btn btn-outline-secondary dropdown-toggle-split'
                }),
            "profile_image": forms.FileInput(attrs={
                'class': 'form-control',
                'enctype': 'multipart/form-data'
                }),
        }
