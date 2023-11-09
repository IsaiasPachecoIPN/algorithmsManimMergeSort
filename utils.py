from manim import *
from main import *

def createElem( text ):
    result = VGroup()
    
    box = Rectangle(height=DEFAULT_BOX_HEIGHT, width=DEFAULT_BOX_WIDTH, fill_color=BLUE, fill_opacity=0.5, stroke_color=BLUE,)
    text = Text(text)
    result.add(text, box)
    return result