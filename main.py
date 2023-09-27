import quickFind as qf
import quickUnion as qu
import numpy


def main():

    # generazione di un grafo casuale ==================================================================================
    N = 20
    graph = numpy.random.randint(low=0, high=2, size=(N, N))
    # mi accerto che non ci siano valori sulla diagonale
    for i in range(N):
        graph[i][i] = 0
    print(graph)


if __name__ == '__main__':
    main()

