from display import *
from draw import *
from parse import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'script.txt', edges, polygons, transform, screen, color )
