SELECT idCliente,
    -- QtdePontos, 
    -- QtdePontos + 10 AS QtdePontosPlus10, 
    -- QtdePontos * 2 AS QtdePontosDouble,
    DtCriacao,
    datetime(DtCriacao) AS dtCriacaoNova,
    datetime(substr(DtCriacao, 1, 19)) AS dtCriacaoNovaSub,
    -- outra forma de fazer caso desse erro a de cima
    strftime('%w', datetime(DtCriacao)) AS diaSemana
FROM clientes
LIMIT 10; 