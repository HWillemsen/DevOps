from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_registration.forms import RegistrationForm

from AuthApp.models import User

# Inherit Django's default RegistrationForm
class MovieRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=50) # Required
    last_name = forms.CharField(max_length=50) # Required
    # All fields you re-define here will become required fields in the form


    class Meta(RegistrationForm.Meta):
        model = User
        fields = (
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2',
		    )

    def __init__(self, *args, **kwargs):
        super(MovieRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))
