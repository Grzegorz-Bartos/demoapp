from django import forms


class PeselForm(forms.Form):
    pesel = forms.CharField(
        label="Numer PESEL",
        min_length=11,
        max_length=11,
        widget=forms.TextInput(attrs={"pattern": "[0-9]{11}", "inputmode": "numeric"}),
        help_text="Wpisz 11 cyfr bez spacji",
    )

    def clean_pesel(self):
        value = self.cleaned_data["pesel"]
        if not value.isdigit():
            raise forms.ValidationError("PESEL powinien zawierać tylko cyfry")
        return value
