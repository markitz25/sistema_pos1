from django import forms
from .models import Venta, DetalleVenta
from clientes.models import Cliente
from inventario.models import Producto

class VentaForm(forms.ModelForm):
    """
    Formulario para crear una venta
    """
    class Meta:
        model = Venta
        fields = ['cliente', 'metodo_pago', 'descuento', 'notas']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'metodo_pago': forms.Select(attrs={
                'class': 'form-select'
            }),
            'descuento': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01',
                'value': '0'
            }),
            'notas': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Notas u observaciones sobre la venta (opcional)'
            })
        }
        labels = {
            'cliente': 'Cliente',
            'metodo_pago': 'Método de Pago',
            'descuento': 'Descuento',
            'notas': 'Notas'
        }


class BuscarVentaForm(forms.Form):
    """
    Formulario para buscar ventas
    """
    busqueda = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por cliente o número de venta...'
        }),
        label=''
    )
    
    fecha_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        label='Desde'
    )
    
    fecha_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        label='Hasta'
    )
    
    metodo_pago = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los métodos')] + Venta.METODOS_PAGO,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Método de Pago'
    )
    
    estado = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los estados')] + Venta.ESTADOS,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Estado'
    )