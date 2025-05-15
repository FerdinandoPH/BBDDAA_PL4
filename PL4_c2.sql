\c telpark

\o PL4_c2_salida.txt
EXPLAIN SELECT provincia, COUNT(*) AS total
FROM (
    SELECT provincia
    FROM reservas
    JOIN clientes ON reservas.clienteid_clientes = clientes.clienteid
    
    UNION
    
    SELECT provincia
    FROM telpark_foraneo.reservas
    JOIN telpark_foraneo.clientes ON reservas.clienteid_clientes = clientes.clienteid
) AS todos_los_datos
GROUP BY provincia;
\o