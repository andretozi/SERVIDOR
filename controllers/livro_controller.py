from flask import Blueprint, request, jsonify

from infrastructure.biblioteca_db import buscar_livros_db, buscar_por_categoria_db
from infrastructure.txt_repository import CarrinhoTXTRepository
from use_cases.carrinho_use_case import CarrinhoUseCase

repo_txt = CarrinhoTXTRepository()
carrinho_uc = CarrinhoUseCase(repo_txt)

# Blueprint limpo, sem template_folder
livro_bp = Blueprint('livro_bp', __name__)


@livro_bp.route('/api/livros', methods=['GET'])
def get_livros():
    termo = request.args.get('termo', '')
    livros = buscar_livros_db(termo)
    return jsonify(livros)


@livro_bp.route('/api/categoria/<nome_categoria>', methods=['GET'])
def get_categoria(nome_categoria):
    livros = buscar_por_categoria_db(nome_categoria)
    return jsonify(livros)


@livro_bp.route('/api/carrinho', methods=['GET', 'POST', 'DELETE'])
def gerenciar_carrinho():
    if request.method == 'GET':
        itens = carrinho_uc.listar_carrinho()
        return jsonify(itens)

    elif request.method == 'POST':
        dados = request.json
        carrinho_uc.adicionar_livro(dados['titulo'])
        return jsonify({"mensagem": "Adicionado com sucesso"}), 201

    elif request.method == 'DELETE':
        dados = request.json
        carrinho_uc.remover_livro(dados['titulo'])
        return jsonify({"mensagem": "Removido com sucesso"}), 200


@livro_bp.route('/api/carrinho/limpar', methods=['POST'])
def limpar_carrinho():
    carrinho_uc.limpar_carrinho()
    return jsonify({"mensagem": "Carrinho esvaziado"}), 200