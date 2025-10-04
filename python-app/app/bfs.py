from collections import deque

def prepare_graph_data(graph):
    """
    Prepara os dados do grafo lido pelo pydot para serem usados pelos algoritmos de busca.

    Args:
        graph (pydot.Dot): O objeto do grafo lido de um arquivo .dot.

    Returns:
        tuple: Uma tupla contendo:
            - matriz_adjacencia (list[list[int]]): A matriz de adjacência do grafo.
            - vertices_ordenados (list[str]): Uma lista com os nomes dos vértices ordenados.
            - mapa_indices (dict[str, int]): Um dicionário mapeando nomes de vértices para seus índices.
    """
    # 1. Pegar os Vértices e Ordenar
    # A forma mais robusta de obter todos os vértices é iterar sobre as arestas
    # e também sobre os nós (para pegar nós isolados).
    all_vertices = set()
    for edge in graph.get_edges():
        all_vertices.add(edge.get_source().strip('"'))
        all_vertices.add(edge.get_destination().strip('"'))
    for node in graph.get_nodes():
        all_vertices.add(node.get_name().strip('"'))
    vertices_ordenados = sorted(list(all_vertices))
    
    num_vertices = len(vertices_ordenados)

    # 2. Criar o Dicionário de "Tradução" (Mapa)
    # Mapeia cada nome de vértice para um índice numérico (0, 1, 2, ...).
    mapa_indices = {nome: i for i, nome in enumerate(vertices_ordenados)}

    # 3. Preencher a Matriz de Adjacência
    # Cria uma matriz NxN preenchida com zeros.
    matriz_adjacencia = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Percorre todas as arestas do grafo.
    for edge in graph.get_edges():
        u, v = edge.get_source().strip('"'), edge.get_destination().strip('"')
        
        # Obtém os índices correspondentes aos vértices da aresta.
        idx_u, idx_v = mapa_indices[u], mapa_indices[v]

        # Marca a conexão na matriz.
        matriz_adjacencia[idx_u][idx_v] = 1
        
        # Se o grafo não for direcionado, marca a conexão de volta também.
        if graph.get_type() == 'graph':
            matriz_adjacencia[idx_v][idx_u] = 1
            
    return matriz_adjacencia, vertices_ordenados, mapa_indices

def bfs(matriz_adjacencia, vertices_ordenados, mapa_indices):
    """
    Executa a Busca em Largura (BFS) a partir do primeiro vértice em ordem lexicográfica.

    Args:
        matriz_adjacencia (list[list[int]]): A matriz de adjacência do grafo.
        vertices_ordenados (list[str]): Lista com os nomes dos vértices ordenados.
        mapa_indices (dict[str, int]): Dicionário que mapeia nomes de vértices para índices.
    """
    if not vertices_ordenados:
        print("BFS: Grafo vazio.")
        return

    num_vertices = len(vertices_ordenados)
    visitados = [False] * num_vertices
    fila = deque()

    # Vértice inicial é o primeiro da lista ordenada
    vertice_inicial = vertices_ordenados[0]
    idx_inicial = mapa_indices[vertice_inicial]

    fila.append(idx_inicial)
    visitados[idx_inicial] = True
    
    print("Resultado da Busca em Largura (BFS):")
    ordem_visitacao = []

    while fila:
        idx_u = fila.popleft()
        ordem_visitacao.append(vertices_ordenados[idx_u])

        # Itera sobre os vizinhos em ordem lexicográfica (pois a matriz e os vértices estão ordenados)
        for idx_v in range(num_vertices):
            if matriz_adjacencia[idx_u][idx_v] == 1 and not visitados[idx_v]:
                visitados[idx_v] = True
                fila.append(idx_v)
    
    print(" -> ".join(ordem_visitacao))
