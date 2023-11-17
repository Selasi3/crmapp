from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"email-address"}))

    class Meta:
        model = User
        fields = ('username',"first_name","last_name","email","password1","password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"]='User Name'
        self.fields["username"].label = ''
        self.fields['username'].help_text = '<span class="form_text text-muted"><small>Required. 150 characters </small></span>'

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"]='Password'
        self.fields["password1"].label = ''
        self.fields['password1'].help_text = '<span class="form_text text-muted"><small>Your password must have a minimum of 8 characters</small></span>'


        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"]=''
        self.fields["password2"].label = ''
        self.fields['password2'].help_text = '<span class="form_text text-muted"><small>Your password must be the same</small></span>'

class AddRecordForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}))
    last_name =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}))
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}))
    location = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}))
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    # phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attr={"placeholder":"Phone", "class":"form-control"}))

    class Meta:
        model = Record
        exclude = ('user',)