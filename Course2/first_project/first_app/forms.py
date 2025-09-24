from django import forms
from .models import Author

class AuthorForm(forms.ModelForm) :
    # name = forms.CharField(max_length=100)
    class Meta:
        model = Author
        fields = ["name"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name[0] == name[0].upper() :
            raise forms.ValidationError("the start is not capital")
        return name