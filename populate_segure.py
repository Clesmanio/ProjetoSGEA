import os
import django
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError, transaction

# ------------------------------------------------------------------
# ESTE CÓDIGO DEVE SER RODADO VIA 'python populate_secure.py'
# Ele força o carregamento do ambiente Django para usar make_password
# ------------------------------------------------------------------

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjetoAula.settings')
django.setup()

from aulaweb.models import Usuario, Evento, Inscricao 

SENHA_PADRAO = '123456'
HASH_PADRAO = make_password(SENHA_PADRAO)

def populate_database_secure():
    """Limpa o banco e popula com dados, gerando hashes de senha e e-mails corretos."""
    
    print("--- INICIANDO POPULAÇÃO SEGURA DO SGEA ---")
    
    try:
        with transaction.atomic():
            # 1. Limpeza Total das Tabelas
            Inscricao.objects.all().delete()
            Evento.objects.all().delete()
            Usuario.objects.all().delete()
            print("Banco limpo (Usuários, Eventos, Inscrições).")

            # 2. Usuários Chave (8 Usuários)
            # NOVO FORMATO: (nome, email, telefone, instituicao, perfil)
            usuarios_chave = [
                ('Ana Organizadora Líder', 'ana@ceub.edu', '61987654321', 'Universidade CEUB', 'ORGANIZADOR'),
                ('Bruno Gerente Eventos', 'bruno@faculdadetec.com', '61911112222', 'Faculdade de Tecnologia', 'ORGANIZADOR'),
                ('Carlos Organizador', 'carlos@ceub.edu', '61933334444', 'Universidade CEUB', 'ORGANIZADOR'),
                ('Profa. Denise Matematicas', 'denise@ceub.edu', '61955556666', 'Universidade CEUB', 'PROFESSOR'),
                ('Prof. Eduardo Web', 'eduardo@ceub.edu', '61977778888', 'Universidade CEUB', 'PROFESSOR'),
                ('Felipe Aluno ADS', 'felipe@aluno.com', '61912345678', 'Universidade CEUB', 'ALUNO'),
                ('Gabriela Aluna Design', 'gabriela@artes.com', '61987654321', 'Faculdade de Artes', 'ALUNO'),
                ('Henrique Testador', 'henrique@teste.com', '61910102020', 'Universidade CEUB', 'ALUNO'),
            ]
            
            for nome, email, telefone, instituicao, perfil in usuarios_chave:
                Usuario.objects.create(
                    nome=nome,
                    email=email, # NOVO CAMPO
                    telefone=telefone,
                    instituicao_ensino=instituicao,
                    perfil=perfil,
                    senha_hash=HASH_PADRAO
                )
            print(f"8 Usuários Chave inseridos. Senha: {SENHA_PADRAO}")

            # 3. Usuários de Teste (50 Alunos Adicionais)
            for i in range(9, 59): # IDs 9 a 58
                Usuario.objects.create(
                    nome=f'Aluno Teste {i:02d}',
                    email=f'aluno{i:02d}@teste.com', # NOVO CAMPO: Email único
                    telefone=f'619100000{i:02d}',
                    instituicao_ensino='Universidade Teste',
                    perfil='ALUNO',
                    senha_hash=HASH_PADRAO
                )
            print("50 Alunos de Teste inseridos.")
            
            
            # 4. População de Eventos (Eventos 1 a 4) - Lógica de Eventos permanece a mesma
            ana = Usuario.objects.get(email='ana@ceub.edu')
            bruno = Usuario.objects.get(email='bruno@faculdadetec.com')
            carlos = Usuario.objects.get(email='carlos@ceub.edu')
            
            # ... (Criação dos Eventos permanece a mesma) ...
            
            evento1 = Evento.objects.create(
                nome='Palestra: O Futuro da I.A. no Desenvolvimento', tipo_evento='PALESTRA', palestrante_nome='Dr. Alencar Smith',
                data_inicial='2025-11-10 14:00:00', data_final='2025-11-10 16:00:00', horario='14:00:00', local='Auditório Principal',
                quantidade_participantes=50, organizador_responsavel=ana
            ) # ID 1
            
            evento2 = Evento.objects.create(
                nome='Seminário de Boas Práticas de Código', tipo_evento='SEMINARIO', palestrante_nome='Equipe Tec.',
                data_inicial='2025-11-15 09:00:00', data_final='2025-11-15 12:00:00', horario='09:00:00', local='Sala de Reuniões 10B',
                quantidade_participantes=2, organizador_responsavel=bruno
            ) # ID 2
            
            evento3 = Evento.objects.create(
                nome='Minicurso: Introdução ao Framework Django', tipo_evento='MINICURSO', palestrante_nome='Prof. Eduardo Web',
                data_inicial='2025-12-01 09:00:00', data_final='2025-12-05 12:00:00', horario='09:00:00', local='Laboratório 301',
                quantidade_participantes=30, organizador_responsavel=carlos
            ) # ID 3
            
            evento4 = Evento.objects.create(
                nome='Semana de Inovação e Startups', tipo_evento='SEMANA_ACADEMICA', palestrante_nome='Vários Convidados',
                data_inicial='2026-03-20 08:00:00', data_final='2026-03-24 18:00:00', horario='08:00:00', local='Bloco Principal',
                quantidade_participantes=200, organizador_responsavel=ana
            ) # ID 4
            print("4 Eventos inseridos.")
            
            
            # 5. Inscrição em Massa e Teste de Limite
            
            # Buscando usuários pelo novo campo EMAIL
            felipe = Usuario.objects.get(email='felipe@aluno.com')
            gabriela = Usuario.objects.get(email='gabriela@artes.com')
            denise = Usuario.objects.get(email='denise@ceub.edu')

            # Cenário 1: Vagas Esgotadas (Lotando o Seminário - ID 2)
            Inscricao.objects.create(usuario=felipe, evento=evento2) 
            Inscricao.objects.create(usuario=gabriela, evento=evento2) 
            print("Seminário lotado (2 inscrições).")
            
            # Cenário 2: Inscrição em Massa (Lotando o Evento 1 - Palestra I.A.)
            for i in range(9, 59): 
                Inscricao.objects.create(usuario=Usuario.objects.get(email=f'aluno{i:02d}@teste.com'), evento=evento1)
            
            Inscricao.objects.create(usuario=denise, evento=evento1, certificado_emitido=False) # Adiciona Profa. Denise como 50ª vaga
            print(f"Palestra (ID 1) lotada com 51 inscrições (falha de lógica proposital para testar exceção).") # Ajustei a contagem
            
            # Cenário 3: Inscrições Normais
            Inscricao.objects.create(usuario=Usuario.objects.get(email='eduardo@ceub.edu'), evento=evento3)
            Inscricao.objects.create(usuario=Usuario.objects.get(email='henrique@teste.com'), evento=evento4)
            
            print("\nSUCESSO! O Banco de Dados foi populado de forma segura.")
            
    except IntegrityError as e:
        print(f"\nERRO DE INTEGRIDADE: Você provavelmente tem um e-mail duplicado.")
        print(f"Detalhe: {e}")
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a população: {e}")


if __name__ == '__main__':
    # Este script deve ser rodado APÓS o 'migrate'
    populate_database_secure()
