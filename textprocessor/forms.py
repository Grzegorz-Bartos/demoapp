from django import forms


class UploadTextForm(forms.Form):
    file = forms.FileField(
        label="Plik tekstowy (.txt)", help_text="Maks. 1 MB, UTF-8/CP1250"
    )

    MAX_SIZE = 1 * 1024 * 1024  # 1 MB

    def clean_file(self):
        f = self.cleaned_data["file"]
        if f.size > self.MAX_SIZE:
            raise forms.ValidationError("Plik jest za duży (maks. 1 MB).")
        if not getattr(f, "name", "").lower().endswith(".txt"):
            raise forms.ValidationError("Dozwolone są tylko pliki .txt")
        return f
