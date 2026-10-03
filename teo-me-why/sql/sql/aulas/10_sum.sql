SELECT sum(qtdePontos)
FROM transacoes
WHERE dtCriacao >= '2025-07-01' 
    AND dtCriacao < '2025-08-01'
    AND qtdePontos > 0
LIMIT 10;

--

SELECT  sum(QtdePontos),

        sum(CASE
            WHEN QtdePontos > 0 THEN QtdePontos
        END) AS qtdePontosPositivos,

        sum(CASE
            WHEN QtdePontos < 0 THEN QtdePontos
        END) AS qtdePontosNegativos
FROM    transacoes
WHERE   dtCriacao >= '2025-07-01' 
    AND dtCriacao < '2025-08-01'
LIMIT   10;