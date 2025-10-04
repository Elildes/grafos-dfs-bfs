def prepare_adj_list(graph):
    """
    Prepara uma lista de adjacência para o grafo, com vizinhos ordenados lexicograficamente.

    Args:
        graph (pydot.Dot): O objeto do grafo lido de um arquivo .dot.

    Returns:
        tuple: Uma tupla contendo:
            - adj_list (dict[str, list[str]]): A lista de adjacência do grafo.
            - vertices_ordenados (list[str]): Uma lista com os nomes dos vértices ordenados.
    """
    # A forma mais robusta de obter todos os vértices é iterar sobre as arestas
    # e também sobre os nós (para pegar nós isolados).
    all_vertices = set()
    for edge in graph.get_edges():
        all_vertices.add(edge.get_source().strip('"'))
        all_vertices.add(edge.get_destination().strip('"'))
    for node in graph.get_nodes():
        all_vertices.add(node.get_name().strip('"'))
    vertices_ordenados = sorted(list(all_vertices))
    adj_list = {vertice: [] for vertice in vertices_ordenados}

    for edge in graph.get_edges():
        u, v = edge.get_source().strip('"'), edge.get_destination().strip('"')
        adj_list[u].append(v)
        if graph.get_type() == 'graph': # Grafo não direcionado
            adj_list[v].append(u)

    # Ordena a lista de vizinhos de cada vértice
    for vertice in adj_list:
        adj_list[vertice].sort()
        
    return adj_list, vertices_ordenados


class DFSTime:
    """Classe auxiliar para manter o contador de tempo global para o DFS."""
    def __init__(self):
        self.tempo = 0

def dfs(adj_list, vertices_ordenados):
    """
    Executa a Busca em Profundidade (DFS) em todo o grafo, gerando uma floresta.

    Args:
        adj_list (dict[str, list[str]]): A lista de adjacência do grafo.
        vertices_ordenados (list[str]): Lista com os nomes dos vértices ordenados.
    """
    if not vertices_ordenados:
        print("DFS: Grafo vazio.")
        return

    visitados = set()
    tempos_inicio = {}
    tempos_fim = {}
    timer = DFSTime()
    
    print("\nResultado da Busca em Profundidade (DFS):")

    def dfs_visit(u):
        visitados.add(u)
        timer.tempo += 1
        tempos_inicio[u] = timer.tempo
        print(f"  Visitando: {u} (Início: {tempos_inicio[u]})")

        # Itera sobre os vizinhos em ordem lexicográfica
        for v in adj_list[u]:
            if v not in visitados:
                dfs_visit(v)
        
        timer.tempo += 1
        tempos_fim[u] = timer.tempo
        print(f"  Finalizando: {u} (Fim: {tempos_fim[u]})")

    # Inicia a busca a partir de cada vértice não visitado, em ordem lexicográfica
    for vertice in vertices_ordenados:
        if vertice not in visitados:
            print(f"\nIniciando busca a partir da árvore com raiz {vertice}:")
            dfs_visit(vertice)
            
    print("\nResumo dos tempos (Início/Fim):")
    for v in vertices_ordenados:
        print(f"  Vértice {v}: {tempos_inicio.get(v, '-')}/{tempos_fim.get(v, '-')}")