from django import forms

from .models import Critic

from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class CriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        fields = ["criticText"]

    def __init__(self, *args, **kwargs):
        super(CriticForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

class MovieNameForm(forms.Form):
    MovieID = forms.CharField(label="IMdb key", max_length=10)

    def __init__(self, *args, **kwargs):
        super(MovieNameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
