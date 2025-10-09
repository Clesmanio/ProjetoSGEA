from django.db import models
from django.contrib.auth.models import User

PERFIS_USUARIO = (
    ('ALUNO', 'Aluno'),
    ('PROFESSOR', 'Professor'),
    ('ORGANIZADOR', 'Organizador'),
)

class Usuario(models.Model):
    nome = models.CharField(max_length=150, db_column='nome')
    telefone = models.CharField(max_length=15, blank=True, null=True)
    instituicao_ensino = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Obrigatório para alunos e professores'
    )

    perfil = models.CharField(max_length=15, choices=PERFIS_USUARIO)
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "usuario"
        ordering = ["nome"]
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.nome} ({self.perfil})"

TIPOS_EVENTO = (
    ('SEMINARIO', 'Seminário'),
    ('PALESTRA', 'Palestra'),
    ('MINICURSO', 'Minicurso'),
    ('SEMANA_ACADEMICA', 'Semana Acadêmica'),
    ('OUTRO', 'Outro'),
)

class Evento(models.Model):
    tipo_evento = models.CharField(max_length=20, choices=TIPOS_EVENTO)
    nome = models.CharField(max_length=200, db_column='nome')
    
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    horario = models.TimeField()
    local = models.CharField(max_length=100)
    palestrante_nome = models.CharField(max_length=150, blank=True, null=True, help_text='Nome do Palestrante ou Convidado')
    
    quantidade_participantes = models.PositiveIntegerField(
        help_text='Limite de inscrições para o evento'
    )
    
    organizador_responsavel = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        related_name='eventos_organizados',
        null=True
    )
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "evento"
        ordering = ["data_inicial", "horario"]
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return f"[{self.get_tipo_evento_display()}] {self.nome} em {self.local}"

class Inscricao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscricoes')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')   
    data_inscricao = models.DateTimeField(auto_now_add=True)
    certificado_emitido = models.BooleanField(default=False)

    class Meta:
        db_table = "inscricao"
        unique_together = ('usuario', 'evento') 
        ordering = ["-data_inscricao"]
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"

    def __str__(self):
        return f"Inscrição de {self.usuario.nome} no evento {self.evento.nome}"