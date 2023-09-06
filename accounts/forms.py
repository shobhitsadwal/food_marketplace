from django.forms import ModelForm
from django import forms
from .models import User




class UserRegisterationForm(ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput())
    confirm_password = forms.CharField(
            label='Confirm Password',
            widget=forms.PasswordInput()
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name' , 'email' , 'phone_number' , "username" , "password"]



    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     repeat_password = self.cleaned_data.get('repeat_password')
    #     if password != repeat_password:
    #         raise forms.ValidationError("passwords doesnt match")
    
    #     return password 
    

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get("phone_number")
    #     if User.objects.filter(phone_number = phone_number ).exists():
    #         raise  forms.ValidationError("this phone number is already registered")
        
    #     return phone_number
        

    def clean(self):
        cleaned_data = super(UserRegisterationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )


