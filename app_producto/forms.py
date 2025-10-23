from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'foto_producto', 'categoria', 'precio', 'stock', 'id_proveedor']