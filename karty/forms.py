from django import forms
from .models import KartaQSL

class KartaQSLForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['znak'].widget.attrs = {
                'class': 'form-control'
                }

    class Meta:
        model = KartaQSL
        fields = ('znak', 'qso_data', 'wyslana', 'odebrana')
