import random
from datetime import datetime, timedelta
import csv

#No se cuentan Ceuta y Melilla (nos lo ha permitido el profesor)
provincias = ['Alava','Albacete','Alicante','Almeria','Asturias','Avila','Badajoz','Barcelona','Burgos','Caceres','Cadiz','Cantabria','Castellon','Ciudad Real','Cordoba','La Coruña','Cuenca','Gerona','Granada','Guadalajara','Guipuzcoa','Huelva','Huesca','Islas Baleares','Jaen','Leon','Lerida','Lugo','Madrid','Malaga','Murcia','Navarra','Orense','Palencia','Las Palmas','Pontevedra','La Rioja','Salamanca','Segovia','Sevilla','Soria','Tarragona','Santa Cruz de Tenerife','Teruel','Toledo','Valencia','Valladolid','Vizcaya','Zamora','Zaragoza']


colores = ["Rojo", "Azul", "Verde", "Amarillo", "Blanco", "Negro", "Gris"]
diccionario_propiedades_vehiculos = {}

def generar_matricula(numero):
    """ Genera una matrícula de vehículo en el formato español (1234 ABC) a partir de un número entero
    """
    letras = "BCDFGHJKLMNPRSTVWXYZ"
    numero_matricula = str(numero % 10000).zfill(4)
    numero = numero // 10000
    letra3 = numero % 20
    numero = numero // 20
    letra2 = numero % 20
    numero = numero // 20
    letra1 = numero % 20
    return f"{numero_matricula}{letras[letra1]}{letras[letra2]}{letras[letra3]}"

def gen_fecha_rand():
    """ Genera una fecha aleatoria entre el 1 de enero de 2024 y el 31 de diciembre de 2024.
    Devuelve una tupla con la fecha de inicio y la fecha de fin, que es entre 1 hora y 10 días después de la fecha de inicio
    """
    inicio = datetime(2024,1,1)
    fin = datetime(2024,12,31)
    diff = fin-inicio

    aumento_rand = random.randrange(diff.days)
    aumento_rand_horas = random.randrange(24)

    f_inicio = inicio + timedelta(days = aumento_rand) + timedelta(hours = aumento_rand_horas)

    return (f_inicio, f_inicio+timedelta(hours=random.randint(1, 240)))

def gen_clientes_csv(inicio=1):
    """ Genera un archivo .csv con 3.000.000 de clientes con el formato

    {clienteid, nombre, apellido, email, telefono, provincia}
    """
    with open(f"clientes_{(inicio//100)+1}.csv", "w") as f:
        for i in range(inicio, inicio+30):
            f.write(f"{i},cliente_{i},apellido_{i},cliente_{i}@example.ex,{600_000_000 + i},{random.choice(provincias)}\n")
    print("Clientes hecho")

def gen_vehiculos_csv(inicio=1):
    """ Genera un archivo .csv con 5.000.000 de vehiculos con el formato

    {vehiculoid, matricula, marca, modelo, color, clienteid_clientes}

    Además, se usa un diccionario para almacenar las propiedades de los vehiculos, donde la clave es el id_cliente y el valor es una lista con los id_vehiculo que tiene ese cliente para usar en la generación de reservas.csv
    """
    with open(f"vehiculos_{(inicio//100)+1}.csv", "w") as f:
        for i in range(inicio, inicio+50):
            propietario = random.randint(inicio, inicio+29)
            if propietario in diccionario_propiedades_vehiculos:
                diccionario_propiedades_vehiculos[propietario].append(i)
            else:
                diccionario_propiedades_vehiculos[propietario] = [i]
            f.write(f"{i},{generar_matricula(i)},marca_{random.randint(1,500)},modelo_{random.randint(1,20)},{random.choice(colores)},{propietario}\n")
    print("Vehiculos hecho")

def gen_plazas_csv(inicio=1):
    """ Genera un archivo .csv con 200.000 plazas con el formato

    {plazaid, numero, nivel, seccion}
    """
    with open(f"plazas_{(inicio//100)+1}.csv", "w") as f:
        for i in range(1, inicio+40):
            f.write(f"{i},{i%((40//66)+1)},{random.randint(-10,0)},{random.choice(['A','B','C','D','E','F'])}\n")
    print("Plazas hecho")

def gen_reservas_y_pagos_csv(inicio=1):
    """ Genera un archivo .csv con 40.000.000 de reservas y pagos con los formatos

    {reservaid, fechainicio, fechafin, vehiculoid_vehiculos, plazaid_plazas, clienteid_clientes}
    {pagoid, cantidad, fechapago, metodopago, reservaid_reservas}

    Se hace uso del diccionario de propietarios de vehículos para mantener la integridad referencial de los datos. Si la función se llama sin haber generado el diccionario, se generará a partir del archivo vehiculos.csv
    """
    if len(diccionario_propiedades_vehiculos) == 0:
        try:
            with open(f"vehiculos_{(inicio//100)+1}.csv", "r") as fvehiculos:
                lector_csv = csv.reader(fvehiculos, skipinitialspace=True, lineterminator="\n")
                for fila in lector_csv:
                    try:
                        diccionario_propiedades_vehiculos[int(fila[-1])].append(int(fila[0]))
                    except KeyError:
                        diccionario_propiedades_vehiculos[int(fila[-1])] = [int(fila[0])]
        except FileNotFoundError:
            print("No se ha encontrado el archivo vehiculos.csv. Genera vehiculos primero.")
            return
    with open(f"reservas_{(inicio//100)+1}.csv", "w") as fres:
        with open(f"pagos_{(inicio//100)+1}.csv", "w") as fpag:
            propietarios = list(diccionario_propiedades_vehiculos.keys())
            for i in range(inicio, inicio+40):
                f_ini, f_fin = gen_fecha_rand()
                cliente = random.choice(propietarios)
                vehiculo = random.choice(diccionario_propiedades_vehiculos[cliente])
                fres.write(f"{i},{f_ini.strftime('%Y-%m-%d %H:%M:%S')},{f_fin.strftime('%Y-%m-%d %H:%M:%S')},{vehiculo},{random.randint(inicio, inicio+39)},{cliente}\n")
                f_pago = f_ini - timedelta(days = random.randint(1,10), hours = random.randint(1,23))
                fpag.write(f"{i},{3*(f_fin - f_ini).total_seconds()/3600},{f_pago.strftime('%Y-%m-%d %H:%M:%S')},{random.choice(['Efectivo', 'Tarjeta de credito', 'Tarjeta de debito', 'PayPal', 'Bizum', 'Transferencia'])},{i}\n")
    print("Reservas y pagos hecho")

def gen_incidencias_csv(inicio=1):
    """ Genera un archivo .csv con 4.000.000 de incidencias con el formato

    {incidenciaid, descripcion, fechaincidencia, estado, reservaid_reservas}
    """
    with open(f"incidencias_{(inicio//100)+1}.csv", "w") as f:
        for i in range(inicio, inicio+40):
            f.write(f"{i},incidencia_{i},{gen_fecha_rand()[1].strftime('%Y-%m-%d %H:%M:%S')},{random.choice(["Nueva","Abierta","En proceso","Resuelta","Cerrada"])},{random.randint(inicio,inicio+39)}\n")
    print("Incidencias hecho")

def gen_telpark(inicio=1):
    """ Genera todos los archivos necesarios para la base de datos de Telepark
    """
    # Se llama a gen_vehiculos_csv() para generar el diccionario de propietarios de vehículos antes de generar reservas y pagos
    gen_clientes_csv(inicio)
    gen_vehiculos_csv(inicio)
    gen_plazas_csv(inicio)
    gen_reservas_y_pagos_csv(inicio)
    gen_incidencias_csv(inicio)

if __name__ == "__main__":
    # gen_telpark()
    # res = gen_fecha_rand()
    # print(res[0].strftime("%Y-%m-%d %H:%M:%S"), res[1].strftime("%Y-%m-%d %H:%M:%S"))
    # gen_clientes_csv()
    gen_telpark(101)