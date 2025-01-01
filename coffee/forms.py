from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

# Signup form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required')
    mobile_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your contact number'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address', 'mobile_number')
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            
            # Save the profile details
            Profile.objects.create(
                user=user,
                address=self.cleaned_data['address'],
                mobile_number=self.cleaned_data['mobile_number']
            )
        return user
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'mobile_number', 'email', 'profile_picture']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        
    