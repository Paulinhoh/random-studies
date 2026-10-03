WITH tb_sumario_dias AS (
    SELECT  substr(DtCriacao,1,10) as dtDia,
            count(DISTINCT IdTransacao) as qtdeTransacao
    FROM transacoes 
    WHERE DtCriacao >= '2025-08-25'
        AND DtCriacao < '2025-08-30'
    GROUP BY dtDia
)

SELECT  *,
        sum(qtdeTransacao) OVER (ORDER BY dtDia) as qtdeTransacoesAcumuladas
FROM tb_sumario_dias;

--
WITH td_cliente_dia AS (
    SELECT  IdCliente,
            substr(DtCriacao,1,10) as dtDia,
            count(DISTINCT IdTransacao) as qtdeTransacao
    FROM transacoes 
    WHERE DtCriacao >= '2025-08-25'
        AND DtCriacao < '2025-08-30'
    GROUP BY IdCliente, dtDia
),

tb_lag AS (
    SELECT  *,
            sum(qtdeTransacao) OVER (PARTITION BY IdCliente ORDER   BY dtDia) as acum,
            lag(qtdeTransacao) OVER (PARTITION BY IdCliente ORDER BY dtDia) as lagTransacao
    FROM td_cliente_dia
    LIMIT 10
)

SELECT  *,
        1.* qtdeTransacao / lagTransacao
FROM tb_lag;

--

WITH tb_cliente_dia AS (
    SELECT  DISTINCT IdCliente,
            substr(DtCriacao,1,10) AS dtDia
    FROM transacoes
    WHERE substr(DtCriacao,1,4) = '2025'
    ORDER BY IdCliente, dtDia
),

tb_lag AS (
    SELECT  *,
            lag(dtDia) OVER (PARTITION BY IdCliente ORDER BY dtDia) AS lagDIa
    FROM tb_cliente_dia
),

tb_diff_dt AS (
    SELECT  *,
            julianday(dtDia) - julianday(lagDIa) AS dtDiff
    FROM tb_lag
),

tb_avg_cientes AS (
    SELECT IdCliente, avg(dtDiff) AS avgDia
    FROM tb_diff_dt
    GROUP BY IdCliente
)

SELECT avg(avgDia) FROM tb_avg_cientes;



