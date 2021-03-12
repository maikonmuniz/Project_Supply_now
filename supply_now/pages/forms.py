from .models import Empresa

class EmpresaForm(form.ModelForm):
    class Meta:
        model = Empresa
