from manim import *
from main import *
from PIL import Image

def createElem( text, color=DEFAULT_ELEMENTS_COLOR, show_text = True, is_marge_sort = False , max_value = None, unsorted_arr = None):

    global DEFAULT_BOX_WIDTH
    global DEFAULT_BOX_HEIGHT

    if not is_marge_sort:
        result = VGroup()
    else:
        result = Group()

    if is_marge_sort:
        box = Rectangle(height=DEFAULT_BOX_HEIGHT, width=DEFAULT_BOX_WIDTH, fill_color=GRAY, fill_opacity=0.1, stroke_color=GRAY,)
    else:
        box = Rectangle(height=DEFAULT_BOX_HEIGHT, width=DEFAULT_BOX_WIDTH, fill_color=color, fill_opacity=0.5, stroke_color=color,)


    if is_marge_sort:
        image = ImageMobject("./marge.png")
        image.set_stroke(GRAY)
        image.scale_to_fit_height(DEFAULT_BOX_HEIGHT)
        scale_factor = int(text) / (DEFAULT_BOX_HEIGHT * max_value)
        image.scale(scale_factor)

    text = Text(text)

    if not is_marge_sort:
        if show_text:
            result.add(text, box)
        else:
            result.add(box)
    else:
        result.add(box, image)
    return result