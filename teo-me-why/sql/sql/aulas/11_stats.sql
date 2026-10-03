-- avg - calcula a média

SELECT  round(avg(qtdePontos), 3) AS mediaCarteira,
        1. * sum(qtdePontos) / count(qtdePontos) AS mediaCarteiraAlt,

        min(qtdePontos) AS minCarteira,
        max(qtdePontos) AS maxCarteira,
        
        sum(flTwitch) as temTwitch,
        sum(flEmail) AS temEmail
FROM    clientes;
