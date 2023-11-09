
#Default values
DEFAULT_BUFF = 0.25
Y_DEFAULT_COORD = DEFAULT_BUFF * 3
DEFAULT_BOX_HEIGHT = 1
DEFAULT_BOX_WIDTH = 3
DEFAULT_FRAME_WIDTH = 30

from manim import *
from utils import *

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


def createMObjectsArr( arr ):
    """
        Funcion  to create scene mobjects from an array
    """
    mobject_arr = []
    for i in range(len(arr)):
        arr[i] = createElem(str(arr[i]))
        #dic_mobjects[i] = arr[i]
        mobject_arr.append(arr[i])

    return mobject_arr

def createStepsMobjects( steps_dic ):
    mobjects_key = {}

    for key in steps_dic:
        mobj_arr = createMObjectsArr( steps_dic[key][0] )
        mobjects_key[key] = mobj_arr

    return mobjects_key


def getTreeLevel( unsorted_arr ):
    """
        Function to get the level of the tree
    """
    level = 1
    while 2**level < len(unsorted_arr):
        level += 1

    return level

def getTreeLevelNumberOfElements( unsoreted_arr ):
    """
        Function to get the number of elements in the tree level
    """
    return 2**getTreeLevel( unsoreted_arr )

def animateMergeSortSteps( scene, steps_dic, unsorted_arr ):

    tree_level = getTreeLevel( unsorted_arr )
    tree_mobjects_dic = createStepsMobjects( steps_dic )

    for i in range(1, tree_level+1):
        if i == 1:
            #Se agregan los primero mobjects
            mobj_arr = tree_mobjects_dic[1]
            print("mobj_arr: ", mobj_arr)
            for i in range(len(mobj_arr)-1):
                mobj_arr[i+1].next_to(mobj_arr[i], RIGHT, buff=DEFAULT_BUFF)
            
            scene.play(
                AnimationGroup(
                    *[
                        Write(mobj_arr[i]) for i in range(len(mobj_arr))
                    ]
                )
            )

        #if the number is even then the direction of the new mobjects is down right fron the parent key
        elif i % 2 == 0:
            #Se agregan los mobjects
            mobj_arr = tree_mobjects_dic[i]
            print("mobj_arr: ", mobj_arr)
            for i in range(len(mobj_arr)-1):
                mobj_arr[i+1].next_to(mobj_arr[i], RIGHT, buff=DEFAULT_BUFF)
                #Move objects to down
                mobj_arr[i+1].shift(DOWN*(DEFAULT_BOX_HEIGHT + DEFAULT_BUFF))
            
            scene.play(
                AnimationGroup(
                    *[
                        Write(mobj_arr[i]) for i in range(len(mobj_arr))
                    ]
                )
            )

    # #Arreglo de mobjects
    # mobjects_arr = create_scene_mobjects( 1, steps_dic[1][0] )

    # for i in range(len(mobjects_arr)-1):
    #     mobjects_arr[i+1].next_to(mobjects_arr[i], RIGHT, buff=DEFAULT_BUFF)

    # #Se anima la escena
    # scene.play(
    #     AnimationGroup(
    #         *[
    #             Write(mobjects_arr[i]) for i in range(len(mobjects_arr))
    #         ]
    #     )
    # )

    #print( "Monjects_res: ", createStepsMobjects( steps_dic ) )

class CreateScene(MovingCameraScene):
    def construct(self):

            readInitData("initdata")
            self.camera.frame.set(width = DEFAULT_FRAME_WIDTH)
            self.camera.frame.shift(RIGHT * (DEFAULT_FRAME_WIDTH/2) - (DEFAULT_BOX_WIDTH))
            self.camera.frame.shift(DOWN* (self.camera.frame.get_height()/4) + DEFAULT_BOX_HEIGHT) 
            print( createMergeSortSteps( unsorted_arr ) )
            animateMergeSortSteps( self, merge_sort_steps_dic, unsorted_arr)
            #print(merge_sort_steps_dic)
            #print( create_scene_mobjects( 1, merge_sort_steps_dic[1][0] ) )
            #print(merge_arr_steps)
            self.wait(1)
            #print(merge_sort_steps_dic)
            #print(merge_counter_steps_dic)
