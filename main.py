from manim import *
from utils import *
import math

#Default values
DEFAULT_BUFF = 0.25
Y_DEFAULT_COORD = DEFAULT_BUFF * 3
DEFAULT_BOX_HEIGHT = 1
DEFAULT_BOX_WIDTH = 2
DEFAULT_FRAME_WIDTH =30
DEFAULT_ELEMENTS_COLOR = BLUE
DEFAULT_INDICATE_COLOR = YELLOW
DEFAULT_INDICATE_L_COLOR = YELLOW
#Merge elements
DEFAULT_MERGE_COLOR = PURPLE
DEFAULT_MERGE_PARENT_INDICATE_COLOR = BLUE_A
DEFAULT_MERGE_INDICATE_COLOR = YELLOW
DEFAULT_IS_MARGE_SORT = False

def readInitData( file ):
    """
    Function to read the initial data from a file
    (param) file: File
    """
    global unsorted_arr
    global DEFAULT_IS_MARGE_SORT

    with open(file, "r") as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            if "unsorted_arr" in line:
                arr = line.split(":")
                unsorted_arr = arr[1].split(",")
                unsorted_arr = [ int(x) for x in unsorted_arr  ]
            if "is_marge_sort" in line:
                bool_str = line.split(":")[1]
                if bool_str == "True":
                    DEFAULT_IS_MARGE_SORT = True

    print("Is marge sort: ", DEFAULT_IS_MARGE_SORT)

def merge(lista_izquierda, lista_derecha, scene=None, parent=None):
    resultado = []

    # Shows the elements to merge
    mobj_L = createMObjectsArr( lista_izquierda, show_text=False )
    mobr_R = createMObjectsArr( lista_derecha , show_text=False)

    mobj_L.next_to(parent, DOWN, buff=DEFAULT_BUFF)
    mobj_L.shift(LEFT * (parent.get_width() /2))

    mobr_R.next_to(parent, DOWN, buff=DEFAULT_BUFF)
    mobr_R.shift(RIGHT * (parent.get_width() /2))

    scene.play(
            Indicate(mobj_L, color=DEFAULT_MERGE_PARENT_INDICATE_COLOR),
            Indicate(mobr_R, color=DEFAULT_MERGE_PARENT_INDICATE_COLOR),
    )

    #Remove the elements from the scene
    scene.remove(mobj_L)
    scene.remove(mobr_R)

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

    #Last mobject in the scene
    last_mobj = scene.mobjects[-1]

    #Shows the result of the merge
    mobj_res = createMObjectsArr( resultado, color=DEFAULT_MERGE_COLOR)
    mobj_res.next_to(last_mobj, DOWN, buff=DEFAULT_BUFF)
    mobj_res.shift(LEFT * (last_mobj.get_width()))

    scene.play(
            Indicate(mobj_res, color=DEFAULT_MERGE_INDICATE_COLOR),
    )

    return resultado

def treeLevel( unsorted_arr ):
    """
    Function to calculate the tree level
    """
    return int(math.log(len(unsorted_arr), 2))

def getMaxValue( unsorted_arr ):
    """
    Function to get the max value of the array
    """
    return max(unsorted_arr)

def createMergeSortAnimation( lista, scene, parent = None, direction=None):
    """
    Function to divide the array using merge-sort algorithm and store the steps in a list
    """
    global unsorted_arr
    global DEFAULT_BOX_HEIGHT
    global DEFAULT_BOX_WIDTH

    m_objects_vg = createMObjectsArr( lista )

    if direction == None:
        #scene.add(m_objects_vg)
        scene.camera.frame.set(width = (m_objects_vg.get_width() + DEFAULT_BUFF*2)*2)
        scene.camera.frame.shift(RIGHT * (m_objects_vg.get_width()/2) + (DEFAULT_BOX_WIDTH/2))        
        scene.camera.frame.shift( DOWN * (scene.camera.frame.get_height() - (2**treeLevel(unsorted_arr) * (DEFAULT_BOX_HEIGHT + DEFAULT_BUFF) + DEFAULT_BUFF*2)) /2 )

        if not DEFAULT_IS_MARGE_SORT:
            text = Text("Merge Sort Algorithm")
        else:
            text = Text("Marge Sort Algorithm")
        text.next_to(m_objects_vg, UP, buff=DEFAULT_BUFF)

        if not DEFAULT_IS_MARGE_SORT:
            scene.play(
                AnimationGroup(
                    Write(text),
                    Write(m_objects_vg),
                )
            )
        else:
            scene.add(text)
            scene.add(m_objects_vg)
   
    elif direction == "L":
        m_objects_vg.next_to(parent, DOWN, buff=DEFAULT_BUFF)
        m_objects_vg.shift(LEFT * (parent.get_width() /2))

        scene.play(
                Indicate(m_objects_vg, color=DEFAULT_INDICATE_COLOR),
        )

    elif direction == "R":
        m_objects_vg.next_to(parent, DOWN, buff=DEFAULT_BUFF)
        m_objects_vg.shift(RIGHT * (parent.get_width() /2))
        scene.play(
                Indicate(m_objects_vg, color=DEFAULT_INDICATE_COLOR),
        )

    if len(lista)<=1:
        return lista
    
    L = createMergeSortAnimation( lista[:len(lista)//2], scene=scene, parent=m_objects_vg, direction="L")
    R = createMergeSortAnimation( lista[len(lista)//2:], scene=scene, parent=m_objects_vg, direction="R")

    return merge(L, R, scene=scene, parent=m_objects_vg)


def createMObjectsArr( arr, color=DEFAULT_ELEMENTS_COLOR, show_text=True ):
    """
        Funcion  to create a vgroup with the elements of the array
    """
    if not DEFAULT_IS_MARGE_SORT:
        vg = VGroup()
    else:
        vg = Group()
    
    for i in range(len(arr)):
        obj = createElem(str(arr[i]), color=color, show_text=show_text, is_marge_sort=DEFAULT_IS_MARGE_SORT, max_value=getMaxValue(unsorted_arr), unsorted_arr=unsorted_arr)
        obj.shift(RIGHT * (DEFAULT_BOX_WIDTH + DEFAULT_BUFF) * i)
        vg.add(obj)

    return vg


class CreateScene(MovingCameraScene):
    def construct(self):


        readInitData("initdata")
        self.camera.frame.set(width = DEFAULT_FRAME_WIDTH)
        # numberplane = NumberPlane()
        # self.add(numberplane)
        createMergeSortAnimation( unsorted_arr, self )
        self.wait(1)
