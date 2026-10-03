SELECT DISTINCT flTwitch, flEmail
FROM clientes
LIMIT 10;

--

SELECT count(DISTINCT idCliente)
FROM clientes;

--

SELECT count(DISTINCT IdCliente)
FROM transacoes
WHERE DtCriacao >= '2025-07-01'
    AND DtCriacao < '2025-08-01'
LIMIT 10;