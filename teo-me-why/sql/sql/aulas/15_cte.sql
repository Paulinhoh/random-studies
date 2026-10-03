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
WITH tb_cliente_primeiro_dia AS (
    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao,1,10) = '2025-08-25'
),

tb_cliente_ultimo_dia AS (
    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao,1,10) = '2025-08-29'
),

tb_join AS (
    SELECT  t1.IdCliente as primCliente,
            t2.IdCliente as ultCliente
    FROM tb_cliente_primeiro_dia AS t1
    LEFT JOIN tb_cliente_ultimo_dia AS t2
        ON t1.IdCliente = t2.IdCliente
)

SELECT  count(DISTINCT primCliente),
        count(DISTINCT ultCliente),
        1. * count(DISTINCT ultCliente) / count(DISTINCT primCliente)
FROM tb_join;


-- quem iniciou o curso no primeiro dia, em media assistiu quantas aulas?
WITH tb_primeiro_dia AS (
    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao,1,10) = '2025-08-25'
),

tb_dias_curso AS (
    SELECT  DISTINCT IdCliente,
            substr(DtCriacao,1,10) as presenteDia
    FROM transacoes
    WHERE DtCriacao >= '2025-08-25'
        AND DtCriacao < '2025-08-30'
    
    ORDER BY IdCliente, presenteDia
),

tb_clientes_dias AS (
    SELECT  t1.IdCliente,
            count(DISTINCT t2.presenteDia) as qtdeDias
    from tb_primeiro_dia AS t1
    LEFT JOIN tb_dias_curso AS t2
        ON t1.IdCliente = t2.IdCliente
    GROUP BY t1.IdCliente
)

SELECT avg(qtdeDias) FROM tb_clientes_dias;
