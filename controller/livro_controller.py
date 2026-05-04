from flask import Blueprint, render_template, request, redirect, url_for

from infrastructure.biblioteca_db import buscar_livros_db, buscar_por_categoria_db
from infrastructure.txt_repository import CarrinhoTXTRepository
from use_cases.carrinho_use_case import CarrinhoUseCase

repo_txt = CarrinhoTXTRepository()
carrinho_uc = CarrinhoUseCase(repo_txt)

livro_bp = Blueprint('livro_bp', __name__, template_folder='../views')

@livro_bp.route('/', methods=['GET', 'POST'])
def index():
    termo = request.form.get('termo_busca', '') if request.method == 'POST' else ""
    livros_filtrados = buscar_livros_db(termo)
    total_itens = len(carrinho_uc.listar_carrinho())
    return render_template('index.html', livros=livros_filtrados, termo_pesquisado=termo, total_carrinho=total_itens)

@livro_bp.route('/categoria/<nome_categoria>')
def filtro_categoria(nome_categoria):
    livros_filtrados = buscar_por_categoria_db(nome_categoria)
    total_itens = len(carrinho_uc.listar_carrinho())
    mensagem = f"Categoria: {nome_categoria.capitalize()}"
    return render_template('index.html', livros=livros_filtrados, termo_pesquisado=mensagem, total_carrinho=total_itens)

@livro_bp.route('/adicionar/<titulo>', methods=['POST'])
def adicionar(titulo):
    carrinho_uc.adicionar_livro(titulo)
    return redirect(url_for('livro_bp.index'))

@livro_bp.route('/carrinho')
def carrinho():
    itens = carrinho_uc.listar_carrinho()
    return render_template('carrinho.html', livros_carrinho=itens, total_carrinho=len(itens))

@livro_bp.route('/remover/<titulo>', methods=['POST'])
def remover(titulo):
    carrinho_uc.remover_livro(titulo)
    return redirect(url_for('livro_bp.carrinho'))


@livro_bp.route('/checkout')
def checkout():
    itens = carrinho_uc.listar_carrinho()
    if not itens:
        return redirect(url_for('livro_bp.carrinho')) # Volta se o carrinho estiver vazio
    return render_template('checkout.html', total_itens=len(itens))

@livro_bp.route('/pagamento', methods=['POST'])
def pagamento():
    metodo = request.form.get('metodo_pagamento')
    carrinho_uc.limpar_carrinho() # Limpa o TXT após a compra
    return render_template('sucesso.html', metodo=metodo)