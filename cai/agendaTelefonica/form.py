from django.forms import ModelForm
from .models import Persona

class PersonaForm(ModelForm):
    
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido','telefono']

    def clean(self):
        form_data = self.cleaned_data
        if form_data['telefono'] == '123':
            self._errors["telefono"] = ["Tiene que ser numerico"] # Will raise a error message
            del form_data['telefono']
        return form_data

