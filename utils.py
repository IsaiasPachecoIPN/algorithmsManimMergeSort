from manim import *
from main import *

def createElem( text, color=DEFAULT_ELEMENTS_COLOR, show_text = True ):
    result = VGroup()
    box = Rectangle(height=DEFAULT_BOX_HEIGHT, width=DEFAULT_BOX_WIDTH, fill_color=color, fill_opacity=0.5, stroke_color=color,)
    text = Text(text)
    if show_text:
        result.add(text, box)
    else:
        result.add(box)
    return result