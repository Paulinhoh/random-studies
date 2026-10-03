-- lista de transações como o produto "Resgatar Ponei";
SELECT *
FROM transacao_produto
WHERE IdProduto = 15;

-- 
SELECT *
FROM transacao_produto AS t1
WHERE t1.IdProduto IN (
    SELECT IdProduto
    FROM produtos
    WHERE DescNomeProduto = 'Resgatar Ponei'
);

-- dos clientes que começaram SQL no primeiro dia, quantos chegaram ao 5° dia?
SELECT count(DISTINCT IdCliente) as qtdePessoas
FROM transacoes AS t1
WHERE t1.IdCliente IN (
    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao,1,10) = '2025-08-25'
)
    AND substr(DtCriacao,1,10) = '2025-08-29';

--
SELECT *
FROM (
    SELECT *
    FROM transacoes
    WHERE DtCriacao >= '2025-01-01'
)
WHERE DtCriacao < '2026-01-01';
