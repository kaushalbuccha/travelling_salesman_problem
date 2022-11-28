from sys import maxsize
from itertools import permutations
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from tkinter import *
V = 5
root = Tk()
root.configure(bg='#F9F7F6')
x = StringVar(root)
y = StringVar(root)
def travellingSalesmanProblem(graph, s):
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:
		current_pathweight = 0
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]
		min_path = min(min_path, current_pathweight)

	return min_path

if __name__ == "__main__":
	graph = [[0, 61, 140, 106,93], [61, 0, 80, 149, 154],
			[140, 80, 0, 229, 235], [106, 149, 229, 0, 75],
            [93, 154, 235, 75, 0]]
	s = 0
	distance_matrix = np.array([
                  [0, 61, 140, 106,93],
                  [61, 0, 80, 149, 154],
		          [140, 80, 0, 229, 235],
		          [106, 149, 229, 0, 75],
                  [93, 154, 235, 75, 0]
])
print(travellingSalesmanProblem(graph, s))
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
permutation.append(0)
print(permutation)

q = str('#F9FBFF')
z = str('#F9FBFF')

def var1():
	x.set("Minimum distance is " + str(travellingSalesmanProblem(graph, s))+" Km")
	global q
	q = '#F9FBFF'
def var2():
	y.set("Path is "+str(permutation))
	global z
	z = '#F9FBFF'

root.title("Travelling Salesman Problem")
root.geometry("700x500")

frame1 =Frame(root)
Button(frame1, text = 'Distance',font=('Helvetica',12,"bold"), bg='#0078ff', padx = '20', pady = '5', width = '15', height = '2', command = var1).pack(side = 'top')
Button(frame1, text = 'Path',font=('Helvetica',12,"bold"),bg='#0078ff', padx = '20', pady = '5', width = '15', height = '2', command = var2).pack(side = 'bottom')
frame1.pack(side = 'left',padx='90',pady=(20,20))

frame2 = Frame(root,bg='#F9FBFF')
Label(frame2, textvariable = x, bg = '#F9FBFF', padx = '120', pady = '17',font='Helvetica').pack(side = 'top', padx = '20')
Label(frame2, textvariable = y, bg = '#F9FBFF', padx = '120', pady = '17',font='Helvetica').pack(side = 'bottom', padx = '20')
frame2.pack(side = 'left', padx = '20')

root.resizable(False, False)
root.mainloop()