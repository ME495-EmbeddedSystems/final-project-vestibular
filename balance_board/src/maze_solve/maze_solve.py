from re import X
import numpy as np
import matplotlib.pyplot as plt

class Solver():

    def __init__(self, maze):
        self.maze = maze
        self.x_list = []
        self.y_list = []
        self.neighbors = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]


    def gen_cost(self, goal):
        queue = [(goal[0], goal[1])]
        self.cost_function = np.zeros(np.shape(self.maze))-1
        self.cost_function[goal[1]][goal[0]] = 0
        
        while len(queue) > 0:

            index = queue.pop(0)
            try:
                cost = self.cost_function[index[1]][index[0]]
            except:
                continue
            
            for shift in self.neighbors:
                try:
                    if self.cost_function[index[1]+shift[1]][index[0]+shift[0]] == -1 and self.maze[index[1]+shift[1]][index[0]+shift[0]] == 0:
                        self.cost_function[index[1]+shift[1]][index[0]+shift[0]] = cost + 1
                        queue.append((index[0]+shift[0], index[1]+shift[1]))
                except:
                    pass
            

    def descend(self, cur):
        x = cur[0]
        y = cur[1]
        print(x)
        print(y)
        cost = self.cost_function[y][x]
        
        while not self.cost_function[y][x] == 0:
            print(x, y)
            lastx=x
            lasty=y
            self.x_list.append(x)
            self.y_list.append(y)
            for shift in self.neighbors:
                if y+shift[1]<0 or x+shift[0]<0:
                    continue
                try:
                    n_cost = self.cost_function[y+shift[1]][x+shift[0]]
                    if n_cost < cost and n_cost > 0:
                        cost = n_cost
                        n_x = x+shift[0]
                        n_y = y+shift[1]
                except:
                    pass
            x = n_x
            y = n_y
            if lastx == x and lasty == y:
                break
        self.x_list.append(x)
        self.y_list.append(y)
        self.path = np.zeros(np.shape(self.maze))
        for i in range(len(self.x_list)):
            self.path[self.y_list[i]][self.x_list[i]] = 255

    def get(self, start, end):
        self.gen_cost(end)
        print(self.maze)
        print(self.cost_function)
        self.descend(start)
        return (self.x_list, self.y_list)

# maze = np.array([[0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 1, 0, 0],
#     [0, 1, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1, 0]
# ])

# maze = np.loadtxt("test_values.txt", delimiter=",")



# solver = Solver(maze)
# print(solver.get((555,429), (339,356)))
# print(solver.cost_function)
# print(solver.maze)
# plt.imshow(solver.cost_function)
# plt.show()
# plt.spy(solver.path)
# plt.show()
# plt.spy(solver.maze)
# plt.show()




            


                    
                