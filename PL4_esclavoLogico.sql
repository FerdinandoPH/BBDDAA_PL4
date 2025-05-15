\c telpark


DELETE FROM pagos;
DELETE FROM incidencias;
DELETE FROM reservas;
DELETE FROM vehiculos;
DELETE FROM plazas;
DELETE FROM clientes;

CREATE SUBSCRIPTION telpark_sub
    CONNECTION 'host=localhost port=5433 dbname=telpark user=postgres password=postgres'
    PUBLICATION telpark_pub
