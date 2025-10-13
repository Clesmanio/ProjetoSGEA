from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from .models import Evento, Usuario, Inscricao
from .forms import EventoForm, UsuarioForm, LoginForm, InscricaoForm

def index(request):
    if 'usuario_id' not in request.session:
        messages.info(request, "Acesso restrito. Por favor, faça login.")
        return redirect('login_usuario')
        
    lista_eventos = Evento.objects.all().order_by('data_inicial')
    lista_eventos = lista_eventos[0: (3 if len(lista_eventos) >= 3 else len(lista_eventos))]
    
    return render(request, 'aulaweb/index.html', {'list_eventos': lista_eventos})

def sobre(request):
    parametros = {
        'title': 'Sobre o Sistema de Gestão de Eventos Acadêmicos (SGEA)',
        'professor': 'Felippe Pires'
    }
    return render(request, 'aulaweb/sobre.html', parametros)

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect('login_usuario')
        else:
            messages.error(request, "Erro ao cadastrar. Verifique os dados.")
    else:
        form = UsuarioForm()
    
    return render(request, 'aulaweb/auth/cadastro.html', {'form': form}) 

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                usuario = Usuario.objects.get(nome=form.cleaned_data['username']) 
                
                messages.success(request, f"Bem-vindo(a), {usuario.nome}!")
                
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nome'] = usuario.nome
                request.session['usuario_perfil'] = usuario.perfil
                
                return redirect('index') 
            except Usuario.DoesNotExist:
                messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = LoginForm()
    
    return render(request, 'aulaweb/auth/login.html', {'form': form})

def logout_usuario(request):
    
    if request.session.pop('usuario_id', None): 
        request.session.pop('usuario_nome', None)
        request.session.pop('usuario_perfil', None)
        
        messages.info(request, "Você foi desconectado(a).")
    else:
        messages.info(request, "Sessão encerrada.")
        
    return redirect('login_usuario')

def list_eventos(request):
    lista_eventos = Evento.objects.all()
    return render(request, 'aulaweb/evento/list_eventos.html', 
                  {'lista_eventos': lista_eventos})

def detalhar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    inscricoes = Inscricao.objects.filter(evento=evento)
    return render(request, 'aulaweb/evento/detail_evento.html', 
                  {'evento': evento, 'inscricoes': inscricoes})

def create_evento(request):
    usuario_id = request.session.get('usuario_id')
    
    if not usuario_id:
        messages.warning(request, "Acesso negado. Faça login.")
        return redirect('login_usuario')
        
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    
    if usuario.perfil != 'ORGANIZADOR':
        messages.error(request, "Permissão negada. Apenas organizadores podem criar eventos.")
        return redirect('list_eventos')
        
    if request.method == 'POST':
        form = EventoForm(request.POST) 
        if form.is_valid():           
            novo_evento = form.save(commit=False)
            novo_evento.organizador_responsavel = usuario 
            novo_evento.save()
            
            messages.success(request, "Evento cadastrado com sucesso! Você é o responsável por ele.")
            return redirect('list_eventos')
        else:
            messages.error(request, "Erro ao cadastrar o evento. Verifique os dados informados.")
    else:
        form = EventoForm()
           
    return render(request, 'aulaweb/evento/create_evento.html', {'form': form})

def update_evento(request, id):
    usuario_id = request.session.get('usuario_id')
    
    if not usuario_id:
        messages.warning(request, "Acesso negado. Faça login.")
        return redirect('login_usuario')
        
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    
    if usuario.perfil != 'ORGANIZADOR':
        messages.error(request, "Permissão negada. Apenas organizadores podem editar eventos.")
        return redirect('list_eventos')
        
    evento = get_object_or_404(Evento, pk=id)
    
    if evento.organizador_responsavel != usuario:
        messages.error(request, "Permissão negada. Você só pode editar eventos que você criou.")
        return redirect('list_eventos')
        
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento) 
        if form.is_valid():
            form.save()
            messages.success(request, "Evento alterado com sucesso!")
            return redirect('list_eventos')
        else:
            messages.error(request, "Erro ao alterar o evento.")
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'aulaweb/evento/create_evento.html', {'form': form, 'editar': True})

def delete_evento(request, id):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        messages.warning(request, "Acesso negado. Faça login.")
        return redirect('login_usuario')

    usuario = get_object_or_404(Usuario, pk=usuario_id)

    if usuario.perfil != 'ORGANIZADOR':
        messages.error(request, "Permissão negada. Apenas organizadores podem deletar eventos.")
        return redirect('list_eventos')

    evento = get_object_or_404(Evento, pk=id)

    if evento.organizador_responsavel != usuario:
        messages.error(request, "Permissão negada. Você só pode deletar eventos que você criou.")
        return redirect('list_eventos')

    if request.method == 'POST':
        evento.delete()
        messages.success(request, "Evento deletado com sucesso!")
        return redirect('list_eventos')
        
    return render(request, 'aulaweb/evento/delete_evento.html', {'evento': evento})

def list_inscricoes(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        messages.warning(request, "Faça login para ver suas inscrições.")
        return redirect('login_usuario')
        
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    minhas_inscricoes = Inscricao.objects.filter(usuario=usuario)
    
    return render(request, "aulaweb/inscricao/list_inscricoes.html", {"inscricoes": minhas_inscricoes})


def inscrever_evento(request, evento_id):

    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        messages.warning(request, "Faça login para se inscrever.")
        return redirect('login_usuario')
        
    evento = get_object_or_404(Evento, pk=evento_id)
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    
    if Inscricao.objects.filter(usuario=usuario, evento=evento).exists():
        messages.warning(request, "Você já está inscrito neste evento.")
        return redirect('detalhar_evento', id=evento.pk)

    total_inscritos = Inscricao.objects.filter(evento=evento).count()
    if total_inscritos >= evento.quantidade_participantes:
        messages.error(request, "Vagas esgotadas para este evento!")
        return redirect('detalhar_evento', id=evento.pk)
        
    Inscricao.objects.create(usuario=usuario, evento=evento)
    messages.success(request, f"Inscrição realizada com sucesso no evento: {evento.nome}!")
    return redirect('list_inscricoes')

def emitir_certificado(request, inscricao_id):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login_usuario')
        
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if usuario.perfil != 'ORGANIZADOR':
        messages.error(request, "Permissão negada. Apenas organizadores podem emitir certificados.")
        return redirect('list_eventos')

    inscricao = get_object_or_404(Inscricao, pk=inscricao_id)
    
    if request.method == 'POST':
        inscricao.certificado_emitido = True
        inscricao.save()
        
        messages.success(request, f"Certificado de {inscricao.evento.nome} emitido para {inscricao.usuario.nome}.")
        
        return redirect('detalhar_evento', id=inscricao.evento.pk)
    
    return render(request, 'aulaweb/inscricao/emitir_certificado.html', {'inscricao': inscricao})

def cancelar_inscricao(request, inscricao_id):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        messages.warning(request, "Acesso negado. Faça login.")
        return redirect('login_usuario')
        
    inscricao = get_object_or_404(Inscricao, pk=inscricao_id, usuario_id=usuario_id) 
    
    if request.method == "POST":
        inscricao.delete()
        messages.success(request, f"Inscrição no evento '{inscricao.evento.nome}' cancelada com sucesso.")
        return redirect("list_inscricoes")
        
    return render(request, "aulaweb/inscricao/cancelar_inscricao.html", {"inscricao": inscricao})
