from django.shortcuts import render, redirect
from .models import Carro, Cliente
from .forms import CarroForm, ClienteForm
from django.contrib import messages

def cadastrar(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Carro cadastrado com sucesso!')
            return redirect('listar')
    else:
        form = CarroForm
        return render(request, 'cadastrar.html', {'form':form})


def listar(request):
    carros = Carro.objects.all()
    return render(request, 'listar.html', {'carros': carros})


def detalhar(request, id):
    carro = Carro.objects.get(id=id)
    return render(request, 'detalhar.html', {'carro': carro})


def atualizar(request, id):
    carro = Carro.objects.get(id=id)
    form = CarroForm(instance=carro)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Carro atualizado com sucesso!')
            return redirect('atualizar', id=id)
        else:
            return render(request, 'atualizar.html', {'form':form})
    else:
        return render(request, 'atualizar.html', {'form': form})


def deletar(request, id):
    carro = Carro.objects.get(id=id)
    carro.delete()
    return redirect('listar')


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente cadastrado com sucesso!')
            return redirect('listar')
    else:
        form = ClienteForm()
        return render(request, 'cadastrar_cliente.html', {'form':form})


def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_cliente.html', {'clientes': clientes})


def detalhar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'detalhar_cliente.html', {'cliente':cliente})


def atualizar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente atualizado com sucesso!')
            return redirect('listar', id=id)
        else:
            return render(request, 'atualizar.html', {'form': form})
    else:
        return render(request, 'atualizar.html', {'form': form})


def deletar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('listar')