\c telpark

DELETE FROM pagos;
DELETE FROM incidencias;
DELETE FROM reservas;
DELETE FROM vehiculos;
DELETE FROM plazas;
DELETE FROM clientes;

\COPY clientes FROM 'clientes_1.csv' DELIMITER ',';
\COPY plazas FROM 'plazas_1.csv' DELIMITER ',';
\COPY vehiculos FROM 'vehiculos_1.csv' DELIMITER ',';
\COPY reservas FROM 'reservas_1.csv' DELIMITER ',';
\COPY incidencias FROM 'incidencias_1.csv' DELIMITER ',';
\COPY pagos FROM 'pagos_1.csv' DELIMITER ',';