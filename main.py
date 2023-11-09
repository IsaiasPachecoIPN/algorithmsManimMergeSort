from manim import *

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

merge_counter = 0
merge_counter_steps_dic = {}
def merge(lista_izquierda, lista_derecha):

    global merge_counter
    global merge_counter_steps_dic

    merge_counter += 1
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

    #print("resultado: ", resultado)
    merge_counter_steps_dic[merge_counter] = resultado
    return resultado

step_counter = 0
merge_sort_steps_dic = {}

def createMergeSortSteps( lista ):
    """
    Function to divide the array using merge-sort algorithm and store the steps in a list
    """
    # if direction != None:
    #     print("direction: ", direction)

    global step_counter
    global merge_sort_steps_dic
    step_counter += 1

    merge_sort_steps_dic[step_counter] = [lista]

    if len(lista)<=1:
        return lista
    
    L = createMergeSortSteps( lista[:len(lista)//2])
    R = createMergeSortSteps( lista[len(lista)//2:])

    return merge(L, R)

def animateMergeSortSteps( scene, steps_dic ):

    first_elem = steps_dic[1]
    print("first_elem: ", first_elem)

    mobjects_arr = []
    for i in steps_dic[1][0]:
       result = VGroup( Text(str(i)) )
       box = Rectangle(  # create a box
       height=0.5, width=0.8, fill_color=BLUE, 
       fill_opacity=0.5, stroke_color=BLUE,)
       text = Text(str(i))

       result.add(text, box)
       mobjects_arr.append(result)

    for i in range(len(mobjects_arr)-1):
        mobjects_arr[i+1].next_to(mobjects_arr[i], RIGHT)

    scene.play(
        AnimationGroup(
            *[
                Write(mobjects_arr[i]) for i in range(len(mobjects_arr))
            ]
        )
    )
class CreateScene(MovingCameraScene):
    def construct(self):

            readInitData("initdata")
            print( createMergeSortSteps( unsorted_arr ) )
            animateMergeSortSteps( self, merge_sort_steps_dic )
            #print(merge_sort_steps_dic)
            #print(merge_counter_steps_dic)
