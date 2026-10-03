-- ORDER BY ordena a coluna
-- ASC crescente
-- DESC decrescente

-- listar clientes com mais pontos
SELECT *
FROM clientes
ORDER BY qtdePontos DESC
LIMIT 10;

-- listar clientes mais antigos
SELECT *
FROM clientes
ORDER BY DtCriacao
LIMIT 10;

-- listar clientes mais antigos do que tem mais pontos pro que tem menos
SELECT *
FROM clientes
ORDER BY DtCriacao ASC, qtdePontos DESC
LIMIT 10;

-- listar clientes mais antigos do que tem mais pontos pro que tem menos (só trazer quem tem twitch)
SELECT *
FROM clientes
WHERE flTwitch = 1
ORDER BY DtCriacao ASC, qtdePontos DESC
LIMIT 10;