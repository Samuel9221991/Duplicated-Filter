import threading



#_______________________#
#        CODIGO         #
#                       #
#    (No modificar)     #
#_______________________#



#___________#
# VARIABLES #
#___________#

archivo_1 = input("1 File > ")
archivo_2 = input("2 File > ")
resultado = input("Result > ")

mal = 0
archivo_txt_1 = open(archivo_1)
archivo_txt_2 = open(archivo_2)
resultado_txt = open(resultado, "a")
archivo_txt_1_array = archivo_txt_1.readlines()
archivo_txt_2_array = archivo_txt_2.readlines()


#________#
# INICIO #
#________#


# FUNCIONES EXTRA

def contador(numero: int, total: int, valor: str):
    global mal
    mal += 1

    print(f"[{mal} (❌)] | Line: {numero}/{total} | Text: {valor}")


# FUNCIONES PRINCIPALES

def revisar():
    contador_1 = 0
    contador_2 = 0
    len_archivo_1 = len(archivo_txt_1_array)
    len_archivo_2 = len(archivo_txt_2_array)

    while contador_1 < len_archivo_1:
        while contador_2 < len_archivo_2:

            if archivo_txt_1_array[contador_1] == archivo_txt_2_array[contador_2]:
                contador(contador_1, len(archivo_txt_1_array), archivo_txt_2_array[contador_2])
                del archivo_txt_2_array[contador_2]
                len_archivo_2 = len(archivo_txt_2_array)

            else:
                contador_2 += 1
            
        contador_1 += 1
        contador_2 = 0


def crear1():
    contador_3 = 0

    while contador_3 < len(archivo_txt_1_array):
        resultado_txt.write(archivo_txt_1_array[contador_3])
        contador_3 += 1

    print(f"[✅] Writing finished of \"{archivo_1}\".")
    resultado_txt.write("\n")


def crear2():
    contador_4 = 0

    while contador_4 < len(archivo_txt_2_array):
        resultado_txt.write(archivo_txt_2_array[contador_4])
        contador_4 += 1

    print(f"[✅] Writing finished of \"{archivo_2}\".")




if __name__ == "__main__":


    print("")
    print("________________________")
    print("    Duplicated Filter   ")
    print("  samuel9221991 v1.0.0  ")
    print("________________________")
    print("")


    Crear1T = threading.Thread(target=crear1, args=())
    Crear2T = threading.Thread(target=crear2, args=())

    revisar()
    Crear1T.start()
    Crear2T.start()

    resultado_txt.close()
    print(f"[✅] The result has been saved with the name \"{resultado}\"")
