from django import forms
from django.forms import ModelForm, CharField, Form, PasswordInput
from django.contrib.auth.models import User, Group

from .models import AppRequest
from .models import Candidate



class CandidateForm(ModelForm):
	class Meta:
		model = Candidate
		fields = '__all__'

class GroupForm(ModelForm):
	class Meta:
		model = Group
		fields = '__all__'

class AppRequestForm(ModelForm):
	class Meta:
		model = AppRequest
		fields = ['vendor', 'app', 'version', 'os', 'package_type', 'complexity', 'priority', 'status', 'assigned', 'attachment', 'comments']

class UserForm1(ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class UserForm(forms.ModelForm):
    username = forms.EmailField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserForm3(ModelForm):
    password = forms.CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': ("A user with that username already exists."),
        'password_mismatch': ("The two password fields didn't match."),
    }
    username = forms.RegexField(label=("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))
    email = forms.EmailField(label=("Email"))
    first_name = forms.CharField(label=("First Name"))
    last_name = forms.CharField(label=("Last Name"))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "groups")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        email = super(UserCreationForm, self).save(commit=False)
        first_name = super(UserCreationForm, self).save(commit=False)
        last_name = super(UserCreationForm, self).save(commit=False)
        groups = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
			user.groups.add(Global-admin)
			user.save()
        return user