import django.forms as forms
from .models import Decks, Cards

class CreateForm(forms.ModelForm):
    class Meta:
        model = Decks
        fields = ["name", "description"]

    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance

class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ["deck", "type", "front", "back", "detailed_info", "tags"]
