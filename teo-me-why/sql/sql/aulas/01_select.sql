-- limit ajudar a n popular a memoria nesse caso que é só para ver quais colunas tem nesta tabela
SELECT *
FROM clientes
LIMIT 10;
-----------------------------------------------------
SELECT IdCliente,
    qtdePontos,
    DtCriacao
FROM clientes;
-----------------------------------------------------
SELECT IdCliente,
    DtCriacao,
    DtAtualizacao
FROM clientes;
