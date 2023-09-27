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

    # test di quick union ==============================================================================================
    # uso una tabella per avere un riferimento a ciascuno degli elementi del grafo
    qu_set = dict()
    # algoritmo CC
    for i in range(N):
        e = qu.make_set(i)
        qu_set[i] = e

    for i in range(N):
        for j in range(N):
            if graph[i][j] is 1:
                if qu.find(qu_set[i]) is not qu.find(qu_set[j]):
                    qu.union(qu_set[i], qu_set[j])

    # test di balanced quick union =====================================================================================
    bqu_set = dict()

    for i in range(N):
        e = qu.balanced_make_set(i)
        bqu_set[i] = e

    for i in range(N):
        for j in range(N):
            if graph[i][j] is 1:
                if qu.find(bqu_set[i]) is not qu.find(bqu_set[j]):
                    qu.balanced_union(bqu_set[i], bqu_set[j])


if __name__ == '__main__':
    main()

