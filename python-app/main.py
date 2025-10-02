import pydot
import webbrowser
import os
import sys

def main():
    
    graphviz_path = r'C:\Program Files\Graphviz\bin'
    if os.path.isdir(graphviz_path) and graphviz_path not in os.environ['PATH']:
        os.environ['PATH'] += os.pathsep + graphviz_path

    
    if len(sys.argv) < 2:
        print("Erro: Forneça o caminho para o arquivo .dot como argumento.")
        print("Uso: python main.py <caminho_para_o_arquivo.dot>")
        sys.exit(1)

    graph_path = sys.argv[1]
    
    output_image_path = os.path.splitext(graph_path)[0] + '.png'

    if not os.path.exists(graph_path):
        print(f"Erro: Arquivo de grafo não encontrado em '{graph_path}'")
        sys.exit(1)

    try:
        (graph,) = pydot.graph_from_dot_file(graph_path)
        graph.write_png(output_image_path)
        print(f"Imagem do grafo salva em '{output_image_path}'")
        webbrowser.open('file://' + os.path.realpath(output_image_path))
    except OSError as e:
        print(f"Erro ao gerar o gráfico: {e}")
        print("Verifique se o Graphviz está instalado e se o seu executável está no PATH do sistema.")

if __name__ == "__main__":
    main()