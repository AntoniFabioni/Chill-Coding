'''
Using pygame, this program displays the 2D projection of
a rotating 4D hypercube (tesseract).
'''

import pygame
import os
import math

# Change rotation directions
rotation = '''
rotated_3d = matrix_multiplication(rotation4d_xy, point)
rotated_3d = matrix_multiplication(rotation4d_yw, point)
rotated_3d = matrix_multiplication(rotation4d_zw, rotated_3d)
'''

def matrix_multiplication(a, b):

    col_a, row_a = len(a[0]), len(a)
    col_b, row_b = len(b[0]), len(b)

    result = [[j for j in range(col_b)] for i in range(row_a)]

    if col_a == row_b:
        for x in range(row_a):
            for y in range(col_b):
                
                sum = 0

                for k in range(col_a):
                    sum += a[x][k] * b[k][y]
                result[x][y] = sum

        return result
    
    else:
        print("Error: Matrices are the incorrect sizes!") # This shouldn't happen!
        return None

os.environ["SDL_VIDEO_CENTERED"]='1'
black, white  = (20, 20, 20), (230, 230, 230)
width, height = 1920, 1080

pygame.init()
pygame.display.set_caption("4D cube Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 1.5 * 60

angle = 0
cube_position = [width//2, height//2]
scale = 2500
speed = 0.5 * 0.01

# Listing all points in the 2x2x2x2 4D Hypercube (this was a fun challenge)
points = []
for w in (-1,1):
  for z in (-1,1):
    for y in (-1,1):
      for x in (1,-1):
        points.append([[x * y], [y], [z], [w]])


def connect_point(i, j, k, offset):
    a = k[i + offset]
    b = k[j + offset]
    pygame.draw.line(screen, white, (a[0], a[1]), (b[0], b[1]), 2)


run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    index = 0
    projected_points = [j for j in range(len(points))]

    #3d matrix rotations
    rotation_x = [[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]]

    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]]

    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                  [math.sin(angle), math.cos(angle), 0],
                  [0, 0 ,1]]
    tesseract_rotation = [[1, 0, 0],
                          [0, math.cos(-math.pi/2), -math.sin(-math.pi/2)],
                          [0, math.sin(-math.pi/2), math.cos(-math.pi/2)]]
   
    #4d matrix rotations
    rotation4d_xy= [[math.cos(angle), -math.sin(angle), 0, 0],
                  [math.sin(angle), math.cos(angle), 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]]
    rotation4d_xz = [[math.cos(angle), 0, -math.sin(angle), 0],
                     [0, 1, 0, 0],
                     [math.sin(angle), 0, math.cos(angle), 0],
                     [0, 0, 0, 1]]
    rotation4d_xw = [[math.cos(angle), 0, 0, -math.sin(angle)],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [math.sin(angle), 0, 0, math.cos(angle)]]
    rotation4d_yz = [[1, 0, 0, 0],
                     [0, math.cos(angle), -math.sin(angle), 0],
                     [0, math.sin(angle), math.cos(angle), 0],
                     [0, 0, 0, 1]]
    rotation4d_yw = [[1, 0, 0, 0],
                     [0, math.cos(angle), 0, -math.sin(angle)],
                     [0, 0, 1, 0],
                     [0, math.sin(angle), 0, math.cos(angle)]]
    rotation4d_zw = [[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, math.cos(angle), -math.sin(angle)],
                     [0, 0, math.sin(angle), math.cos(angle)]]

    for point in points:

        # Code from line 10 is placed below.
        exec(rotation)

        distance = 5
        w = 1/(distance - rotated_3d[3][0])
        projection_matrix4 = [[w, 0, 0, 0],
                            [0, w, 0, 0],
                            [0, 0, w, 0],]

        projected_3d = matrix_multiplication(projection_matrix4, rotated_3d)
        rotated_2d = matrix_multiplication(tesseract_rotation, projected_3d)
        z = 1/(distance - (rotated_2d[2][0] + rotated_3d[3][0]))
        projection_matrix = [[z, 0, 0],
                            [0, z, 0 ]
                            ]

        #rotated_2d = matrix_multiplication(rotation_x, projected_3d)
        projected_2d = matrix_multiplication(projection_matrix, rotated_2d)
        x = int(projected_2d[0][0] * scale) + cube_position[0]
        y = int(projected_2d[1][0] * scale) + cube_position[1]

        projected_points[index] = [x, y]
        pygame.draw.circle(screen, white, (x, y), 10)
        index += 1
        
    #draw edges
    for m in range(4):
        connect_point(m, (m+1)%4, projected_points, 8)
        connect_point(m+4, (m+1)%4 + 4, projected_points, 8)
        connect_point(m, m+4, projected_points, 8)

    for m in range(4):
        connect_point(m, (m+1)%4, projected_points, 0)
        connect_point(m+4, (m+1)%4 + 4, projected_points, 0)
        connect_point(m, m+4, projected_points, 0)

    for m in range(8):
        connect_point(m,  m+8, projected_points, 0)

    angle += speed
    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            
            # Press "Esc" to exit.
            if event.key == K_ESCAPE:
                run = False

pygame.quit()