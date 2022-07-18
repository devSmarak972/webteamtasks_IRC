# import the standard Django Forms
# from built-in library
from django.forms.forms import Form
from django.forms.fields import EmailField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

# creating a form


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['Username', 'Email', 'profileimg']
    def save(self,id, commit=True):
        # user = super(CustomUserCreationForm, self).save(commit=False)
        # user.Username = self.cleaned_data['username']
        # user.Email = self.cleaned_data["email"]
        # cleaned_data = super(CustomUserCreationForm, self)
        print(id,"saving")
        user = Profile.objects.get(id=id)
        user.Username = self.cleaned_data['Username']
        user.Email = self.cleaned_data['Email']
        if self.cleaned_data['profileimg'] is not None:
            profileimg=self.cleaned_data['profileimg'] 
        user.save()
        
    
    




class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=250)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)
    image = forms.FileField(
        label="Image", required=False, widget=forms.ClearableFileInput)

    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2',)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = Profile.objects.filter(Username=username)
        if new.count():
            raise forms.ValidationError("User Already Exist")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = Profile.objects.filter(Email=email)
        if new.count():
            raise forms.ValidationError(" Email Already Exist")
        return email

    def clean_image(self):

        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

        uploaded_image = self.cleaned_data.get("image",  False)

        extension = str(uploaded_image).split('.')[-1]

        file_type = extension.lower()

        # if not uploaded_image:
        #     # handle empty image
        #     raise ValidationError("please upload an Image")

        # if file_type not in IMAGE_FILE_TYPES:
        #     raise ValidationError("File is not image.")

        return uploaded_image

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password dont match")
        return password2

    
    # def clean(self):

    #     cleaned_data = super(CustomUserCreationForm, self).clean()
    #     if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
    #         if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #             raise forms.ValidationError(
    #                 "Passwords don't match. Please try again!")
    #     return self.cleaned_data

    def save(self, commit=True):
        # user = super(CustomUserCreationForm, self).save(commit=False)
        # user.Username = self.cleaned_data['username']
        # user.Email = self.cleaned_data["email"]
        # cleaned_data = super(CustomUserCreationForm, self)
        print(self.cleaned_data['image'])
        print("  username input cleaned")
        user = Profile.objects.create_user(
            Username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            Email=self.cleaned_data['email'],
            profileimg=self.cleaned_data['image'] if self.cleaned_data['image'] is not None else "/images/users/profile.png"
        )
        print(user)
        return user
