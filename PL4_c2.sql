\c telpark

SELECT provincia, COUNT(*) AS total
FROM (telpark.reservas JOIN telpark.clientes ON reservas.clienteid_clientes = clientes.clineteid) UNION (telpark_foraneo.reservas JOIN telpark_foraneo.clientes ON reservas.clienteid_clientes = clientes.clineteid)
GROUP BY provincia;