\c telpark

SELECT provincia, COUNT(*) AS total
FROM (
    SELECT provincia
    FROM reservas
    JOIN clientes ON reservas.clienteid_clientes = clientes.clienteid
    
    UNION
    
    SELECT provincia
    FROM telpark_foraneo.reservas
    JOIN telpark_foraneo.clientes ON reservas.clienteid_clientes = clientes.clienteid
) AS subquery
GROUP BY provincia;