import pydot
import webbrowser
import os
import sys
from app.bfs import prepare_graph_data as prepare_for_bfs, bfs
from app.dfs import prepare_adj_list as prepare_for_dfs, dfs

def setup_graphviz_path():
    """
    Adiciona o diretório bin do Graphviz ao PATH do sistema em ambientes Windows,
    se não estiver presente. Em outros sistemas, assume-se que o Graphviz
    já está no PATH.
    """
    if sys.platform == "win32":
        # Tenta adicionar o caminho padrão do Graphviz no Windows ao PATH
        graphviz_path = r'C:\Program Files\Graphviz\bin'
        if os.path.isdir(graphviz_path) and graphviz_path not in os.environ.get('PATH', ''):
            os.environ['PATH'] += os.pathsep + graphviz_path

def get_graph_path_from_args() -> str:
    """Valida e retorna o caminho do arquivo .dot fornecido como argumento de linha de comando."""
    if len(sys.argv) < 2:
        print("Erro: Forneça o caminho para o arquivo .dot como argumento.")
        print("Uso: python main.py <caminho_para_o_arquivo.dot>")
        sys.exit(1)
    
    graph_path = sys.argv[1]    
    if not os.path.exists(graph_path):
        print(f"Erro: Arquivo de grafo não encontrado em '{graph_path}'")
        sys.exit(1)
    return graph_path

def generate_graph_image(graph_path: str) -> pydot.Dot:
    """Lê um arquivo .dot, gera uma imagem .png e a abre."""
    output_image_path = os.path.splitext(graph_path)[0] + '.png'
    try:
        (graph,) = pydot.graph_from_dot_file(graph_path)
        graph.write_png(output_image_path)
        print(f"Imagem do grafo salva em '{output_image_path}'")
        webbrowser.open('file://' + os.path.realpath(output_image_path))
        return graph
    except OSError as e:
        print(f"Erro ao gerar o gráfico: {e}")
        print("Verifique se o Graphviz está instalado e se o seu executável está no PATH do sistema.")
        sys.exit(1)
    except ValueError:
        print(f"Erro: O arquivo '{graph_path}' não pôde ser interpretado como um grafo. Verifique a sintaxe do arquivo DOT.")
        sys.exit(1)

def main():
    """Função principal que orquestra a execução do programa."""
    setup_graphviz_path()
    graph_path = get_graph_path_from_args()
    graph = generate_graph_image(graph_path)

    print("-" * 30)
    # Preparar e executar BFS
    matriz_adj, vertices_ord, mapa_idx = prepare_for_bfs(graph)
    bfs(matriz_adj, vertices_ord, mapa_idx)
    
    print("-" * 30)
    # Preparar e executar DFS
    lista_adj, vertices_ord_dfs = prepare_for_dfs(graph)
    dfs(lista_adj, vertices_ord_dfs)
    print("-" * 30)

if __name__ == "__main__":
    main()