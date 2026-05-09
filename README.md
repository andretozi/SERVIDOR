# Atividade Pratica - Arquitetura Cliente-Servidor (Servidor / API)

Este repositorio contem a aplicacao Back-end (Lado Servidor) do MVP da livraria virtual, desenvolvido para a disciplina de Engenharia de Software. O projeto evoluiu de um modelo monolitico para a **Arquitetura Cliente-Servidor**, atuando exclusivamente como uma API RESTful.

## 1. O Papel do Servidor

Nesta arquitetura, o servidor e o detentor exclusivo das regras de negocio, dos casos de uso e do acesso ao banco de dados (neste caso, a lista em memoria e o arquivo TXT do carrinho). Ele nao possui conhecimento sobre como os dados serao exibidos na tela. Sua unica funcao e receber requisicoes HTTP, processa-las utilizando os principios da Clean Architecture e devolver os dados em formato puro.

## 2. Tecnologias e Conceitos Aplicados

Para viabilizar a separacao do projeto, as seguintes adaptacoes foram feitas:

* **Retorno em JSON:** Os controladores (Controllers) da aplicacao deixaram de renderizar arquivos HTML. Em vez disso, utilizam a funcao `jsonify` do Flask para serializar os dados (livros, mensagens de sucesso) no formato JSON, que e a linguagem universal de comunicacao entre sistemas web.
* **Preservacao da Clean Architecture:** O nucleo do sistema (`domain` e `use_cases`) e a infraestrutura (`infrastructure`) permaneceram intactos. Isso comprova o sucesso do Principio de Inversao de Dependencia (DIP) implementado anteriormente: a forma de entregar os dados mudou de HTML para JSON, mas a regra de negocio nao precisou ser alterada.
* **Endpoints Estruturados:** Foram criadas rotas especificas (ex: `/api/livros`, `/api/carrinho`) utilizando metodos HTTP adequados (GET para buscar, POST para adicionar, DELETE para remover).

## 3. Como Executar

Para que o Cliente consiga consumir os dados, este servidor deve estar em execucao.

1. Instale as dependencias: `pip install Flask`
2. Execute o arquivo principal: `python app.py`
3. A API estara operando por padrao na porta 5000 (`http://127.0.0.1:5000`).

   ## Fron Conectado com o Back: 

   <img width="1023" height="489" alt="image" src="https://github.com/user-attachments/assets/a5d45807-54bb-4233-a96b-bd66fbd68028" />
