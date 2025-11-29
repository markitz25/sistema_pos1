"""
Formularios para el módulo de trabajadores
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Trabajador


class TrabajadorForm(forms.ModelForm):
    """Formulario para crear/editar trabajador"""
    
    # Campos del User
    username = forms.CharField(
        label='Usuario',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
    )
    
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    
    password = forms.CharField(
        label='Contraseña',
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        }),
        help_text='Dejar en blanco para mantener la contraseña actual (solo edición)'
    )
    
    password_confirm = forms.CharField(
        label='Confirmar Contraseña',
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        })
    )
    
    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellido', 'telefono', 'direccion', 'rol', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 300 123 4567'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección completa'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-select'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
    
    def __init__(self, *args, **kwargs):
        self.instance_user = kwargs.pop('instance_user', None)
        self.is_new = kwargs.pop('is_new', True)
        super().__init__(*args, **kwargs)
        
        # Si es edición, llenar campos del usuario
        if self.instance_user:
            self.fields['username'].initial = self.instance_user.username
            self.fields['email'].initial = self.instance_user.email
            self.fields['password'].required = False
            self.fields['password_confirm'].required = False
        else:
            self.fields['password'].required = True
            self.fields['password_confirm'].required = True
    
    def clean_username(self):
        username = self.cleaned_data['username']
        
        # Verificar si el username ya existe (excepto el actual)
        if self.instance_user:
            if User.objects.exclude(pk=self.instance_user.pk).filter(username=username).exists():
                raise forms.ValidationError('Este nombre de usuario ya está en uso')
        else:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Este nombre de usuario ya está en uso')
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        
        # Verificar si el email ya existe (excepto el actual)
        if self.instance_user:
            if User.objects.exclude(pk=self.instance_user.pk).filter(email=email).exists():
                raise forms.ValidationError('Este correo electrónico ya está en uso')
        else:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Este correo electrónico ya está en uso')
        
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        # Validar contraseñas solo si se proporcionaron
        if password or password_confirm:
            if password != password_confirm:
                raise forms.ValidationError({
                    'password_confirm': 'Las contraseñas no coinciden'
                })
            
            if len(password) < 6:
                raise forms.ValidationError({
                    'password': 'La contraseña debe tener al menos 6 caracteres'
                })
        
        return cleaned_data


class PerfilForm(forms.ModelForm):
    """Formulario para editar perfil propio"""
    
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    
    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellido', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 300 123 4567'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección completa'
            })
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email


class CambiarContraseñaForm(PasswordChangeForm):
    """Formulario para cambiar contraseña"""
    
    old_password = forms.CharField(
        label='Contraseña Actual',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        })
    )
    
    new_password1 = forms.CharField(
        label='Nueva Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        }),
        help_text='Mínimo 6 caracteres'
    )
    
    new_password2 = forms.CharField(
        label='Confirmar Nueva Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        })
    )