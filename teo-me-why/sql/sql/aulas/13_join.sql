SELECT *
FROM transacao_produto AS t1
    LEFT JOIN produtos AS t2 ON t1.IdProduto = t2.IdProduto
WHERE t2.IdProduto IS NULL
LIMIT 10;

--
SELECT t1.*, t2.DescNomeProduto
FROM transacao_produto AS t1
    LEFT JOIN produtos AS t2 ON t1.IdProduto = t2.IdProduto
LIMIT 10;

-- qual categoria tem mais produtos vendidos?
SELECT t2.DescCategoriaProduto,
    count(DISTINCT t1.IdTransacao) AS qtdeTransacao

FROM transacao_produto AS t1

LEFT JOIN produtos AS t2
ON t1.IdProduto = t2.IdProduto

GROUP BY t2.DescCategoriaProduto;

-- em 2024, quantas transações de Lovers tivemos?
SELECT t3.DescCategoriaProduto,
    count(DISTINCT t1.IdTransacao) as qtdeTransacoes

FROM transacoes AS t1

LEFT JOIN transacao_produto as t2
    ON t1.IdTransacao = t2.IdTransacao
LEFT JOIN produtos as t3
    ON t2.IdProduto = t3.IdProduto

WHERE t1.dtCriacao >= '2024-01-01'
    AND t1.dtCriacao < '2025-01-01'
    -- AND t3.DescCategoriaProduto = 'lovers'

GROUP BY t3.DescCategoriaProduto
HAVING qtdeTransacoes < 1000

ORDER BY qtdeTransacoes DESC;

-- qual mês tivemos mais lista de presença assinada
SELECT t3.DescNomeProduto,
    substr(t1.dtCriacao,1,7) AS anoMes,
    count(DISTINCT t1.IdTransacao) as qtdeTransacoes
    

FROM transacoes AS t1

LEFT JOIN transacao_produto AS t2
    ON t1.IdTransacao = t2.IdTransacao
LEFT JOIN produtos as t3
    ON t2.IdProduto = t3.IdProduto

WHERE t3.DescNomeProduto = 'Lista de presença'

GROUP BY anoMes

ORDER BY qtdeTransacoes DESC;

