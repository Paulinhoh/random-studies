## Fundamentos basicos MongoDB

```shell
# para se conectar no mongoshell
mongosh

# mostra os databases criados
show databases

# mostra as collections no database
show collections

# criar um novo database ou troca de database
use teste2

# quando se cria um database é necessario criar tb uma collection
db.createCollection("collection")

# deleta a collection
# OBS: databases sem collections nenhuma são excluidos
db.<nomeDaCollection>.drop()

# deleta o database
db.dropDatabase()

# insere um na colection
db.<nomeDaCollection>.insertOne({jsonDocument})

# insere varios dados na collection
db.<nomeDaCollection>.insertMany({jsonDocument},{jsonDocument},...)

# busca os dados adicionados
db.<nomeDaCollection>.find()
db.<nomeDaCollection>.find().pretty()

# busca um dado especifico
db.<nomeDaCollection>.find({ nome: "Paulo Henrique" })

# busca o primeiro dado (pode-se colocar filtro tb)
db.<nomeDaCollection>.findOne()

# atualiza um dado
db.<nomeDaCollection>.updateOne({ nome: "João" }, { $set: { game: "r6" } })

# atualiza varios ou todos (tb se pode inserir um dado pelo update)
db.<nomeDaCollection>.updateMany(
    {}, { $set: { stats: 0 }
)

# no mongo as "tabelas não necessaria mente precisam ser todas iguais"
# alterando somente o joão
db.<nomeDaCollection>.updateOne({ nome: "João" }, { $set: { achievements: 2 } })

# deleta um dado
db.<nomeDaCollection>.deleteOne({ nome: "João" })

# deleta varios (se n colocar um filtro deleta todos)
db.<nomeDaCollection>.deleteMany()

# Operadores

# exemplo
db.<nomeDaCollection>.find({ money: { $gt: 30}})

$gt # maior que
$gte # maior ou igual que
$lt # menor que
$lte # menor ou igual que

# operadores de update
$inc # incremento (positovo ou negativo)

de.<nomeDaCollection>.insertOne({
    nome: "Ana", # string
    idade: 22, # int
    hobbies: ["Correr", "Ler", "Trilhas"], # array
    esta_trabalhando = true, # bool
    data_cadastro = new Date(), # date
    caracteristicas: { # json
        cor_dos_olhos: "azuis",
        altura: 1.82, # double/float
        perfil: "extrovertida"
    }
})

# indices
# criar um index
db.<nomeDaCollection>.createIndex({ "nome": 1 })

# lista os index
db.<nomeDaCollection>.getIndexes()

# 
db.<nomeDaCollection>.explain.find()

# deletar um index
db.<nomeDaCollection>.dropIndex("nome_1")
```

<!-- jsonDocument -->

```json
{
    "nome": "Paulo Henrique",
    "email": "phtest@test.com",
    "password": "secret",
    "avatar": "",
    "game": "Zelda",
    "highscore": 0,
    "money": 0,
    "hp": 0,
    "xp": 0,
    "nivel": 0
},

{
    "nome": "João",
    "email": "jota@test.com",
    "password": "12345678",
    "avatar": "",
    "game": "Lol",
    "highscore": 0,
    "money": 0,
    "hp": 0,
    "xp": 0,
    "nivel": 0
}


// após o update
{
    "nome": "Paulo Henrique",
    "email": "phtest@test.com",
    "password": "secret",
    "avatar": "",
    "game": "Zelda",
    "highscore": 0,
    "money": 0,
    "hp": 0,
    "xp": 0,
    "nivel": 0,
    "stats": 0
},

{
    "nome": "João",
    "email": "jota@test.com",
    "password": "12345678",
    "avatar": "",
    "game": "r6",
    "highscore": 0,
    "money": 0,
    "hp": 0,
    "xp": 0,
    "nivel": 0,
    "stats": 0,
    "achievements": 2
}
```
