from django import forms
from .models import Cliente
from django.core.exceptions import ValidationError

class ClienteForm(forms.ModelForm):
    """
    Formulario para crear y editar clientes
    """
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'cedula', 'correo', 'telefono', 'direccion', 'notas', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre completo',
                'required': True
            }),
            'cedula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de cédula o DNI',
                'required': True
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com (opcional)'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 300 123 4567',
                'required': True
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección completa (opcional)',
                'rows': 3
            }),
            'notas': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notas u observaciones sobre el cliente',
                'rows': 3
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'nombre': 'Nombre Completo *',
            'cedula': 'Cédula/DNI *',
            'correo': 'Correo Electrónico',
            'telefono': 'Teléfono *',
            'direccion': 'Dirección',
            'notas': 'Notas',
            'activo': 'Cliente Activo'
        }
    
    def clean_cedula(self):
        """Validación personalizada para la cédula"""
        cedula = self.cleaned_data.get('cedula')
        
        # Validar que solo contenga números
        if not cedula.isdigit():
            raise ValidationError('La cédula debe contener solo números')
        
        # Validar longitud mínima
        if len(cedula) < 6:
            raise ValidationError('La cédula debe tener al menos 6 dígitos')
        
        # Validar que no exista otra cédula igual (excepto en edición)
        if self.instance.pk:  # Si estamos editando
            if Cliente.objects.exclude(pk=self.instance.pk).filter(cedula=cedula).exists():
                raise ValidationError('Ya existe un cliente con esta cédula')
        else:  # Si estamos creando
            if Cliente.objects.filter(cedula=cedula).exists():
                raise ValidationError('Ya existe un cliente con esta cédula')
        
        return cedula
    
    def clean_correo(self):
        """Validación personalizada para el correo"""
        correo = self.cleaned_data.get('correo')
        
        if correo:  # Si se proporcionó un correo
            # Validar que no exista otro correo igual (excepto en edición)
            if self.instance.pk:  # Si estamos editando
                if Cliente.objects.exclude(pk=self.instance.pk).filter(correo=correo).exists():
                    raise ValidationError('Ya existe un cliente con este correo')
            else:  # Si estamos creando
                if Cliente.objects.filter(correo=correo).exists():
                    raise ValidationError('Ya existe un cliente con este correo')
        
        return correo
    
    def clean_telefono(self):
        """Validación personalizada para el teléfono"""
        telefono = self.cleaned_data.get('telefono')
        
        # Limpiar espacios y caracteres especiales
        telefono_limpio = ''.join(filter(str.isdigit, telefono))
        
        # Validar longitud
        if len(telefono_limpio) < 7:
            raise ValidationError('El teléfono debe tener al menos 7 dígitos')
        
        return telefono
    
    def clean_nombre(self):
        """Validación personalizada para el nombre"""
        nombre = self.cleaned_data.get('nombre')
        
        # Capitalizar nombre
        nombre = nombre.strip().title()
        
        # Validar que tenga al menos 3 caracteres
        if len(nombre) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres')
        
        return nombre


class BuscarClienteForm(forms.Form):
    """
    Formulario para buscar clientes
    """
    busqueda = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre, cédula o teléfono...',
            'autocomplete': 'off'
        }),
        label=''
    )
    
    ESTADOS = [
        ('', 'Todos los estados'),
        ('activos', 'Solo activos'),
        ('inactivos', 'Solo inactivos'),
    ]
    
    estado = forms.ChoiceField(
        choices=ESTADOS,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Estado'
    )
    
    ORDENAR = [
        ('-fecha_registro', 'Más recientes'),
        ('fecha_registro', 'Más antiguos'),
        ('nombre', 'Nombre (A-Z)'),
        ('-nombre', 'Nombre (Z-A)'),
        ('-total_compras', 'Mayor gasto'),
        ('total_compras', 'Menor gasto'),
    ]
    
    ordenar = forms.ChoiceField(
        choices=ORDENAR,
        required=False,
        initial='-fecha_registro',
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Ordenar por'
    )