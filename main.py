

#Default values
unsorted_arr = []
merge_arr_steps = []

def readInitData( file ):
    """
    Function to read the initial data from a file
    (param) file: File
    """
    global unsorted_arr

    with open(file, "r") as f:
        data = f.readlines()
        counter = 0
        for line in data:
            line = line.strip()
            if "unsorted_arr" in line:
                arr = line.split(":")
                unsorted_arr = arr[1].split(",")
                unsorted_arr = [ int(x) for x in unsorted_arr  ]

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    #print("lista: ", lista)

    izquierda = merge_sort(lista[:len(lista) // 2])
    derecha = merge_sort(lista[len(lista) // 2:])

    return merge(izquierda, derecha)

def merge(lista_izquierda, lista_derecha):
    resultado = []

    #mostrar las listas en la misma linea
    #print("lista_izquierda: {} lista_derecha: {}".format(lista_izquierda, lista_derecha))
    merge_arr_steps.insert(0, [lista_izquierda, lista_derecha])

    #print("lista_izquierda: ", lista_izquierda)
    #print("lista_derecha: ", lista_derecha)

    i = 0
    j = 0

    while i < len(lista_izquierda) and j < len(lista_derecha):
        if lista_izquierda[i] < lista_derecha[j]:
            resultado.append(lista_izquierda[i])
            i += 1
        else:
            resultado.append(lista_derecha[j])
            j += 1

    resultado += lista_izquierda[i:]
    resultado += lista_derecha[j:]

    return resultado

counter = 0
a_izq_arr = []
a_der_arr = []
def createMergeSortSteps( lista ):
    """
    Function to divide the array using merge-sort algorithm and store the steps in a list
    """

    global counter

    #print("counter: ", counter) 

    if counter == 0:
        a_izq_arr.append(lista)
    else:
        a_der_arr.append(lista)

    if len(lista)<=1:
        return lista
    
    createMergeSortSteps( lista[:len(lista)//2] )
    createMergeSortSteps( lista[len(lista)//2:] )

    counter += 1

def main():
    global counter
    global a_izq_arr
    global a_der_arr
    readInitData("initdata")
    print(unsorted_arr)
    #print( merge_sort(unsorted_arr) )
    createMergeSortSteps( unsorted_arr[:len(unsorted_arr)//2] )
    print(a_izq_arr)
    print(a_der_arr)
    counter = 0
    a_izq_arr = []
    a_der_arr = []
    createMergeSortSteps( unsorted_arr[len(unsorted_arr)//2:] )
    print(a_izq_arr)
    print(a_der_arr)
if __name__ == "__main__":
    main()