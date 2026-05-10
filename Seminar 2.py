import random
from time import sleep
# Augabe 1
print("--------- Aufgabe 1: ---------")

# liste = [x for x in range(0,random.randint(0,20))]
# print(liste)

# for i in range(len(liste)):
#     rand = random.randint(0,len(liste)-1)
#     liste[i], liste[rand] = liste[rand], liste[i]
# print(liste)

# Augabe 2
print("--------- Aufgabe 2: ---------")
def create_field(number_of_collums, number_of_rows, margin):
    field = []
    for row in range(0,number_of_rows):
        new_row = []
        for collum in range(0,number_of_collums):
            if row == margin or collum == margin or row == (number_of_rows - margin -1) or collum == (number_of_collums - margin -1):
                new_row.append("x")
            else:
                new_row.append(" ")
        field.append(new_row)
    return field

def print_field(field):
    for row in range(len(field)):
        for collum in range(len(field[row])):
            print(field[row][collum],end="")
        print(end="\n")

def flood_fill(field,start_point):
    new_points = []
    print_field(field)
    ran = False
    for i in range(len(start_point)):
        point_collum, point_row = start_point[i]
        if field[point_row][point_collum] != "x" and point_row < len(field) and point_collum < len(field[point_row]):
            field[point_row][point_collum]="x"
            if point_collum +1 <= len(field[point_row])-1:
                new_points.append((point_collum + 1,point_row))
            if point_collum -1 <= len(field[point_row])-1:
                new_points.append((point_collum - 1,point_row))
            if point_row +1 <= len(field)-1:
                new_points.append((point_collum,point_row + 1))
            if point_row -1 <= len(field)-1:
                new_points.append((point_collum,point_row - 1))
            ran = True

    if ran:
        sleep(0.01)
        flood_fill(field,new_points)
    
def file_to_map(filename):
    with open(filename,'r') as file:
        a = list(file)
        field=[]
        for row in range(len(a)):
            field.append(list(a[row]))
    return field


filename='field.txt'
start_points=[(40,16)]
#flood_fill(create_field(20,10,1),start_points)
flood_fill(file_to_map(filename),start_points)