def print_adjacency_matrix(matrix):
    for row in matrix:
        print(row)


def get_permutations(arr, r, result, perm=[]):
    '''
    Function to calculate all permutations of an arr, given r places
    like n P r 
    '''
    if r == 0:
        result.append([x for x in perm])
        return
    for i in range(len(arr)):
        if arr[i] is not None:
            val = arr[i]
            perm.append(val)
            arr[i] = None
            get_permutations(arr, r-1, result, perm)
            perm.pop()
            arr[i] = val


def min_colors_graph_coloring(matrix, num_vertices, source):
    '''
    This fucntion will return the smallest number of colors required for coloring graph (chromatic number)
    along with the color group the node belongs to.
    '''
    colors = [-1 for _ in range(num_vertices)]
    min_colors_required = 0

    # for nodes whose all neighbours are visited
    visited = [False for _ in range(num_vertices)]

    # Queue for bfs
    q = [source]

    # to check which are added to the queue
    added = [False for _ in range(num_vertices)]

    added[source] = True
    colors[source] = 0

    while len(q) != 0:
        cur = q.pop(0)

        for i in range(num_vertices):
            if matrix[cur][i]:
                if not added[i]:
                    q.append(i)
                    added[i] = True
                if colors[i] == -1:
                    colors[i] = 0
                if colors[cur] == colors[i]:
                    if not visited[i]:
                        colors[i] += 1
                    else:
                        colors[cur] += 1
                    min_colors_required = max(
                        min_colors_required, colors[cur], colors[i])

        visited[source] = True

    return colors, min_colors_required+1


def graph_coloring(adjacency_matrix, num_vertices, available_colors, source):
    '''
    Gives all possible colors of nodes from the available colors
    '''
    color_groups, min_colors_req = min_colors_graph_coloring(
        adjacency_matrix, num_vertices, source)
    all_graph_colors = []
    if len(available_colors) < min_colors_req:
        print("Not possible to color the graph")
        print(f"Minimun Colors Required is {min_colors_req}")
        print(f"Available Colors are {len(available_colors)}")
    else:
        all_perm = []
        get_permutations(available_colors, min_colors_req, all_perm)

        for perm in all_perm:
            all_graph_colors.append([perm[i] for i in color_groups])
    return all_graph_colors


if __name__ == '__main__':
    num_vertices = int(input("Enter Number of vertices: "))
    source = int(input("Enter Source vertex: "))
    num_edges = int(input("Enter number of edges: "))

    adjacency_matrix = [[0 for _ in range(num_vertices)]
                        for __ in range(num_vertices)]

    for i in range(num_edges):
        s, d = (int(x) for x in input("Enter edge (s,d): ").split(" "))
        adjacency_matrix[s][d] = 1
        adjacency_matrix[d][s] = 1

    available_colors = input("Enter available colors: ").split(" ")

    print("The Adjacnecy Matrix: ")
    print_adjacency_matrix(adjacency_matrix)

    print("\nAll possible valid colors for the given graph: ")
    graph_colors = graph_coloring(
        adjacency_matrix, num_vertices, available_colors, source)
    for color in graph_colors:
        print(color)
