# Grafos com Java - implementação de Algoritmos BFS e DFS

## Descrição

Este projeto implementa os algoritmos de busca em grafos BFS (Busca em Largura) e DFS (Busca em Profundidade) utilizando Java.

Os grafos são lidos de arquivos no formato DOT, compatível com o Graphviz, podendo ser direcionados ou não.

A leitura e impressão dos grafos pode utilizar bibliotecas externas, mas a implementação dos algoritmos é própria.

## Dependências

- Java 11 ou superior
- [JGraphT](https://jgrapht.org/) (para leitura e manipulação de grafos)
- [Graphviz-java](https://github.com/nidi3/graphviz-java) (opcional, para visualização)

## Execução

1. Clone o repositório:

```python
git clone https://github.com/Elildes/grafos-dfs-bfs.git
cd grafos-dfs-bfs/java-app
```

2. Compile e execute o projeto (exemplo usando Maven):

```maven
mvn clean install
java -jar target/grafos-dfs-bfs.jar caminho/do/arquivo.dot
```

## Estrutura do Projeto

- `src/main/java/`: Código-fonte dos algoritmos e utilitários.
- `BFS.java`: Implementação do algoritmo BFS.
- `DFS.java`: Implementação do algoritmo DFS.
- `GraphUtils.java`: Funções auxiliares para leitura e manipulação de grafos.
- `Main.java`: Classe principal para execução.

## Exemplo de Uso

```java
java -jar target/grafos-dfs-bfs.jar exemplos/grafo.dot
```

## Testes

Os testes automatizados podem ser executados com:

``` maven
mvn test
```

## Referências

- [Graphviz DOT Language](https://graphviz.org/doc/info/lang.html)
- Livro: "Algoritmos: Teoria e Prática" (Cormen et al.), 4ª Ed., Seção 20.3
