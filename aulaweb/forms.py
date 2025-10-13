from django import forms
from .models import Usuario, Evento, Inscricao

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'nome', 'tipo_evento', 'data_inicial', 'data_final',
            'horario', 'local', 'palestrante_nome', 'quantidade_participantes'
        ]
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do Evento'}),
            'tipo_evento': forms.Select(attrs={'class': 'form-control'}),
            'data_inicial': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'data_final': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'horario': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Auditório Principal'}),            
            'palestrante_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Convidado/Palestrante'}),            
            'quantidade_participantes': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
        
        labels = {
            'nome': 'Nome do Evento',
            'tipo_evento': 'Tipo',
            'data_inicial': 'Data e Hora de Início',
            'data_final': 'Data e Hora de Fim',
            'horario': 'Horário de Início',
            'local': 'Local do Evento',
            'palestrante_nome': 'Palestrante/Convidado',           
            'quantidade_participantes': 'Limite de Vagas',
        }

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'instituicao_ensino', 'perfil']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu.email@dominio.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
            'instituicao_ensino': forms.TextInput(attrs={'class': 'form-control'}),
            'perfil': forms.Select(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'nome': 'Nome Completo',
            'email': 'E-mail de Login', 
            'telefone': 'Telefone',
            'instituicao_ensino': 'Instituição de Ensino',
            'perfil': 'Perfil de Usuário',
        }

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['usuario', 'evento'] 
        
        widgets = {
            'usuario': forms.HiddenInput(),
            'evento': forms.HiddenInput(),
        }

class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail de Login',
        widget=forms.EmailInput(attrs={'class': 'form-control'}) # Use EmailInput
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
