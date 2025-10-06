# Grafos com Python - implementação de Algoritmos BFS e DFS

## Descrição

Este projeto implementa os algoritmos de busca em grafos BFS (Busca em Largura) e DFS (Busca em Profundidade) utilizando Python. Os grafos são lidos de arquivos no formato DOT, compatível com o Graphviz, e podem ser direcionados ou não.

A leitura e impressão dos grafos pode utilizar bibliotecas externas, mas a implementação dos algoritmos é própria.

## Dependências

- Python 3.13.7 ou superior
- [pydot](https://github.com/pydot/pydot): Para ler e interpretar arquivos no formato DOT.
- [Graphviz](https://graphviz.org/download/): Ferramenta necessária para renderizar e salvar os grafos como imagens.

Para instalar as dependências, execute:

`pip install pydot`  
`pip show pydot`  
`dot -V`  

## Execução

1. Clone o repositório:

```python
git clone https://github.com/Elildes/grafos-dfs-bfs.git
cd grafos-dfs-bfs/python-app
```

2. Execute o programa principal:

`python main.py graphs\ex01.dot`  

## Estrutura do Projeto

- `main.py:` Arquivo principal para execução dos algoritmos.
- `bfs.py:` Implementação do algoritmo BFS.
- `dfs.py:` Implementação do algoritmo DFS.
- `utils.py:` Funções auxiliares para leitura e manipulação de grafos.

## Exemplo de Uso

```python
PS C:\...\Git\grafos-dfs-bfs\python-app> python .\main.py .\graphs\ex02.dot`  
Imagem do grafo salva em '.\graphs\ex02.png'
------------------------------
Resultado da Busca em Largura (BFS):
a -> b -> c -> d
------------------------------

Resultado da Busca em Profundidade (DFS):     

Iniciando busca a partir da árvore com raiz a:
  Visitando: a (Início: 1)
  Visitando: b (Início: 2)
  Visitando: c (Início: 3)
  Finalizando: c (Fim: 4)
  Visitando: d (Início: 5)
  Finalizando: d (Fim: 6)
  Finalizando: b (Fim: 7)
  Finalizando: a (Fim: 8)

Resumo dos tempos (Início/Fim):
  Vértice a: 1/8
  Vértice b: 2/7
  Vértice c: 3/4
  Vértice d: 5/6
------------------------------
```

## Referências

- [Graphviz DOT Language](https://graphviz.org/doc/info/lang.html)
- Livro: "Algoritmos: Teoria e Prática" (Cormen et al.), 4ª Ed., Seção 20.3
