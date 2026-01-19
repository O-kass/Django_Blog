from django import forms

class GuessForm(forms.Form):
    guess = forms.CharField(
        label="Guess",
        max_length=5,
        min_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter 5-letter word"
        })
    )