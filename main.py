from display import *
from draw import *
from parse import *
from matrix import *
import math

screen = new_screen()
color = [ 0,255,255 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

parse_file( 'script', edges, polygons, csystems, screen, color )