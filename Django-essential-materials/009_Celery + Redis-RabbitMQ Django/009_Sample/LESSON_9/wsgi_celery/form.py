from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class TotalForm(forms.Form):
    total = forms.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(5000000)]
    )
