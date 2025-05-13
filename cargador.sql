\c telpark

DELETE FROM pagos;
DELETE FROM incidencias;
DELETE FROM reservas;
DELETE FROM vehiculos;
DELETE FROM plazas;
DELETE FROM clientes;

\COPY clientes FROM 'clientes_2.csv' DELIMITER ',';
\COPY plazas FROM 'plazas_2.csv' DELIMITER ',';
\COPY vehiculos FROM 'vehiculos_2.csv' DELIMITER ',';
\COPY reservas FROM 'reservas_2.csv' DELIMITER ',';
\COPY incidencias FROM 'incidencias_2.csv' DELIMITER ',';
\COPY pagos FROM 'pagos_2.csv' DELIMITER ',';