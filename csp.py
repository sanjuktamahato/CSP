
V = 4



graph = [
    [0, 1, 1, 0],  
    [1, 0, 1, 1],  
    [1, 1, 0, 1],  
    [0, 1, 1, 0]  
]


m = 3  


colors = [-1] * V  


def is_safe(vertex, color, colors, graph):
   
    for i in range(V):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring(graph, m, colors, vertex):
    
    if vertex == V:
        return True

    
    for color in range(m):
        if is_safe(vertex, color, colors, graph):
            colors[vertex] = color  
           
            if graph_coloring(graph, m, colors, vertex + 1):
                return True
            
            colors[vertex] = -1

    return False  


if graph_coloring(graph, m, colors, 0):
    
    print("Solution found:")
    for vertex in range(V):
        print(f"Vertex {vertex} -> Color {colors[vertex]}")
else:
    print("No solution exists.")
