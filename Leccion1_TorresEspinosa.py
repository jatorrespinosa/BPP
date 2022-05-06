# --- Ejercicio Leccion 1 - BPP - TorresEspinosa,JoseAntonio ---
import pandas as pd
import matplotlib.pyplot as plt

# Excepción creada para los meses vacíos
class Faltan_datos(Exception):
    def __init__(self, param1):
        self.param1 = param1

# Función comprueba si el archivo exite, intentando abrirlo
def existe(file):
    try:
        with open(file, 'r') as f:
            return True
    except FileNotFoundError:
        return False
    else:
        f.close()

# Función para agrupar los datos de cada mes
def add(val):
    global ingreso, gasto
    if val > 0:
        ingreso += val
    else:
        gasto += val

# Función para buscar los meses con máximos
def encuentra_meses(data):
    m_gasto = ''
    m_ahorro = ''
    max_gasto = 0
    max_ahorro = 0
    for (mes, valores) in data.iteritems():
        # GASTO
        if valores[1] < max_gasto:
            m_gasto = mes
            max_gasto = valores[1]
        # AHORRO
        if valores[2] > max_ahorro:
            m_ahorro = mes
            max_ahorro = valores[2]
    return m_gasto, m_ahorro

# Función para obtener datos anuales
def balance(data):
    gasto = 0
    ingreso = 0
    for mes in data:
        ingreso += data[mes].values[0]
        gasto += data[mes].values[1]
    return gasto, ingreso


# -------------------------------------------------------------
# ---------------------- MAIN ---------------------------------
# -------------------------------------------------------------

file = "finanzas2020.csv" # Path archivo

# --- Comprueba si existe archivo ---
if not existe(file):
    print(f"\t->El archivo {file} no es correcto o no existe")
else:
    # --- Si existe continúa el programa ---
    # Lectura datos
    df = pd.read_csv(file, sep='\t')
    
    try:
        # --- Comprueba numero de meses correcto ---
        assert(len(df.columns.values) == 12)

        # --- Comprueba meses sin datos ---
        df_check = df.isnull() # Crea dataframe con valores booleanos, True si valor NaN
        for m, val in df_check.iteritems():
            vacio = True
            for v in val:  # Recorre todos los valores bool del mes
                vacio &= v  # Si todos los valores del mes son NaN vacío seguirá a True
            if vacio:
                raise Faltan_datos(m)  # Si el mes no tiene datos lanza excepción
    except AssertionError:
        print(f"\t->Solo se encuentran {len(df.columns.values)} meses en los datos")
    except Faltan_datos as e:
        p1 = e.args  # Devuelve tupla
        for x in p1:
            print(f"\t->El mes {x} no contiene datos")
    else:
        # --- Si no hay excepciones hace los cálculos ---
        # Obtención ingresos, gastos y balance por mes
        data = pd.DataFrame()
        for (mes, valores) in df.iteritems():
            gasto = 0
            ingreso = 0
            for aux in valores:
                try:
                    add(int(aux))
                except ValueError as err:
                    try:
                        # --- Comprueba si la excepción saltó debido a estar un número entre comillas ---
                        aux = aux.replace("'", '')
                        add(int(aux))
                    # --- Para datos no correctos ---
                    except ValueError:
                        print(f"\t-> {aux} no es un dato correcto.")
                    except AttributeError:
                        print(f"\t-> {aux} no es un dato correcto.")
            # Añade mes y valores al dataframe 'data'
            data[mes] = [ingreso, gasto, ingreso + gasto]
        print('')  # Separa las salidas de excepción de los datos obtenidos

        # --- Mes con mas gasto y mes con mas ahorro ---
        mes_gasto, mes_ahorro = encuentra_meses(data)
        print(f"El mes con mas gasto es {mes_gasto} con {data[mes_gasto].values[1]}")
        print(f"El mes con mas ahorro es {mes_ahorro} con {data[mes_ahorro].values[2]}")

        # --- Balance anual ---
        total_gasto, total_ingreso = balance(data)
        print(f"La media de gastos al año es de {total_gasto/12:.3f}")
        print(f"El gasto total del año es de {total_gasto}")
        print(f"Los ingresos anuales son de {total_ingreso}")

        # --- Gráfica de evolucion ---
        x = list(data.columns.values)  # Lista de meses
        plt.plot(x, data.iloc[0], label='Ingresos')  # Línea de ingresos
        plt.plot(x, abs(data.iloc[1]), label='Gastos')  # Línea de gastos en valores absolutos
        plt.ylabel('Euros (€)')
        plt.xlabel('Meses')
        plt.legend()
        plt.grid(True)

        plt.show()  # Muestra gráfica