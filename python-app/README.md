# Grafos com Python - implementação de Algoritmos BFS e DFS

## Descrição

Este projeto implementa os algoritmos de busca em grafos BFS (Busca em Largura) e DFS (Busca em Profundidade) utilizando Python. Os grafos são lidos de arquivos no formato DOT, compatível com o Graphviz, e podem ser direcionados ou não.

A leitura e impressão dos grafos pode utilizar bibliotecas externas, mas a implementação dos algoritmos é própria.

## Dependências

- Python 3.8 ou superior
- [networkx](https://networkx.org/) (para leitura de arquivos DOT)
- [pydot](https://github.com/pydot/pydot) (opcional, para manipulação de DOT)
- Graphviz instalado (opcional, para visualização)

Para instalar as dependências, execute:

`pip install networkx pydot`

## Execução

1. Clone o repositório:

```python
git clone https://github.com/Elildes/grafos-dfs-bfs.git
cd grafos-dfs-bfs/python-app
```

2. Execute o programa principal:

`python main.py caminho/do/arquivo.dot`

## Estrutura do Projeto

- `main.py:` Arquivo principal para execução dos algoritmos.
- `bfs.py:` Implementação do algoritmo BFS.
- `dfs.py:` Implementação do algoritmo DFS.
- `utils.py:` Funções auxiliares para leitura e manipulação de grafos.

## Exemplo de Uso

`python main.py exemplos/grafo.dot`

## Referências

- [Graphviz DOT Language](https://graphviz.org/doc/info/lang.html)
- Livro: "Algoritmos: Teoria e Prática" (Cormen et al.), 4ª Ed., Seção 20.3
