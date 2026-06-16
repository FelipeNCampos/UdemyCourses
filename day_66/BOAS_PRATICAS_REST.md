# Boas Praticas para Construir APIs REST

Este guia resume boas praticas para criar APIs REST claras, previsiveis e faceis de manter.

## 1. Use Recursos no Nome das Rotas

Rotas REST devem representar recursos, nao acoes.

Bom:

```http
GET /cafes
GET /cafes/1
POST /cafes
PATCH /cafes/1
DELETE /cafes/1
```

Evite:

```http
GET /get-cafe
POST /create-cafe
POST /delete-cafe
```

O verbo HTTP ja indica a acao.

## 2. Use os Verbos HTTP Corretos

Use cada metodo para uma finalidade clara:

| Metodo | Uso |
| --- | --- |
| `GET` | Buscar dados |
| `POST` | Criar um novo recurso |
| `PUT` | Substituir um recurso inteiro |
| `PATCH` | Atualizar parte de um recurso |
| `DELETE` | Remover um recurso |

Exemplo:

```http
PATCH /cafes/1
```

Pode atualizar apenas o preco do cafe, sem precisar reenviar todos os campos.

## 3. Retorne Status Codes Adequados

O status HTTP deve comunicar o resultado da requisicao.

| Codigo | Significado |
| --- | --- |
| `200 OK` | Requisicao bem-sucedida |
| `201 Created` | Recurso criado |
| `400 Bad Request` | Dados invalidos ou incompletos |
| `401 Unauthorized` | Falta autenticacao |
| `403 Forbidden` | Usuario autenticado, mas sem permissao |
| `404 Not Found` | Recurso nao encontrado |
| `409 Conflict` | Conflito, como registro duplicado |
| `500 Internal Server Error` | Erro inesperado no servidor |

Exemplo:

```json
{
  "error": {
    "message": "Cafe not found."
  }
}
```

## 4. Retorne JSON Consistente

Mantenha um formato previsivel para sucesso e erro.

Resposta de sucesso:

```json
{
  "data": {
    "id": 1,
    "name": "Cafe Central",
    "coffee_price": "$2.50"
  }
}
```

Resposta de erro:

```json
{
  "error": {
    "message": "Missing required field: name"
  }
}
```

Evite retornar mensagens em formatos diferentes em cada rota.

## 5. Valide os Dados de Entrada

Nunca confie nos dados enviados pelo cliente.

Valide:

- Campos obrigatorios
- Tipos de dados
- Tamanhos maximos
- Valores permitidos
- Formatos de email, URL, data e preco

Exemplo:

```python
if not request.form.get("name"):
    return jsonify(error={"message": "Missing required field: name"}), 400
```

## 6. Use Nomes de Campos Claros

Prefira nomes explicitos e consistentes.

Bom:

```json
{
  "has_wifi": true,
  "has_sockets": false,
  "coffee_price": "$2.50"
}
```

Evite:

```json
{
  "wifi": "yes",
  "plug": 0,
  "price": "cheap"
}
```

## 7. Separe Query Parameters de Body

Use query parameters para filtros, busca e paginacao.

```http
GET /cafes?location=London
GET /cafes?page=2&limit=20
```

Use o body para criar ou atualizar dados.

```http
POST /cafes
Content-Type: application/json

{
  "name": "Cafe Central",
  "location": "London"
}
```

## 8. Implemente Paginacao

Quando uma rota pode retornar muitos registros, use paginacao.

Exemplo:

```http
GET /cafes?page=1&limit=20
```

Resposta:

```json
{
  "data": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 120
  }
}
```

Isso evita respostas grandes demais e melhora a performance.

## 9. Nao Exponha Dados Sensíveis

Nunca retorne:

- Senhas
- Tokens
- Chaves de API
- Dados internos do servidor
- Stack traces em producao

Em caso de erro inesperado, retorne uma mensagem generica:

```json
{
  "error": {
    "message": "Internal server error"
  }
}
```

## 10. Use Autenticacao Quando Necessario

APIs publicas podem ter rotas abertas, mas rotas de alteracao geralmente precisam de protecao.

Exemplos:

- API key
- JWT
- OAuth
- Sessao autenticada

Operacoes como `POST`, `PATCH` e `DELETE` normalmente devem exigir permissao.

## 11. Mantenha Idempotencia Quando Fizer Sentido

Uma operacao idempotente pode ser repetida varias vezes com o mesmo resultado final.

Geralmente sao idempotentes:

- `GET`
- `PUT`
- `DELETE`

Geralmente nao e idempotente:

- `POST`

Exemplo: chamar `DELETE /cafes/1` duas vezes nao deveria criar efeitos colaterais inesperados.

## 12. Documente a API

Documente:

- Rotas disponiveis
- Metodo HTTP
- Parametros
- Corpo da requisicao
- Respostas de sucesso
- Respostas de erro
- Regras de autenticacao

Exemplo simples:

```http
PATCH /cafes/1
```

Atualiza parcialmente um cafe.

Body:

```json
{
  "coffee_price": "$3.00"
}
```

Resposta:

```json
{
  "message": "Cafe updated successfully"
}
```

## 13. Versione a API

Quando a API puder mudar com o tempo, use versionamento.

Exemplo:

```http
/api/v1/cafes
/api/v2/cafes
```

Isso evita quebrar clientes antigos quando novas versoes forem lancadas.

## 14. Evite Logica Duplicada

Se varias rotas fazem validacao, serializacao ou tratamento de erro parecido, crie funcoes auxiliares.

Exemplo:

```python
def error_response(message, status_code):
    return jsonify(error={"message": message}), status_code
```

Isso deixa o codigo mais limpo e facilita manutencao.

## 15. Teste as Rotas

Teste pelo menos:

- Requisicoes validas
- Campos obrigatorios faltando
- IDs inexistentes
- Tipos de dados invalidos
- Permissoes
- Erros esperados

Ferramentas uteis:

- Postman
- Insomnia
- curl
- Test client do Flask
- pytest

## Checklist Rapido

Antes de considerar uma API pronta, confira:

- As rotas usam substantivos no plural
- Os metodos HTTP estao corretos
- Os status codes fazem sentido
- As respostas JSON sao consistentes
- Os dados de entrada sao validados
- Erros nao vazam detalhes internos
- Rotas sensiveis usam autenticacao
- A API esta documentada
- Existem testes para os principais cenarios

## Exemplo de Estrutura REST para Cafes

```http
GET /cafes
GET /cafes/1
GET /cafes?location=London
POST /cafes
PATCH /cafes/1
DELETE /cafes/1
```

Essa estrutura e simples, previsivel e facil de entender por qualquer pessoa que va consumir a API.
