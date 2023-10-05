import ListaConcatenata2 as lc
import ForesteInsiemiDisgiunti2 as fi
import numpy
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


def make_graph(N):
    print("check dimension: ", N)
    graph_matrix = numpy.random.randint(low=0, high=2, size=(N, N))
    # mi accerto che non ci siano valori sulla diagonale
    for i in range(N):
        graph_matrix[i][i] = 0
    # rendo la matrice simmetrica rispetto alla diagonale

    graph = list()
    for i in range(N):
        for j in range(N):
            if graph_matrix[i][j] == 1:
                graph.append(Edge(i, j))
    print(graph)




def connect_components_lista(edges, vertex):
    for v in vertex:
        lc.make_set(v)

    #for arch in edges:
     #   while arch is not None:



def connect_components_hlista(edges, vertex):
    pass

def connect_components_forest(edges, vertex):
    pass


def main():
    N = 11
    min = 10
    num_iter = 1

    lc_time = numpy.zeros(N-min)
    lch_time = lc_time.copy()
    fi_time = lc_time.copy()

    for i in range(N-min):
        print("inizio iter ", i)
        for j in range(num_iter):

            lc_vertex = [lc.Element(k) for k in range(i + min)]
            lch_vertex = lc_vertex.copy()
            fi_vertex = [fi.SetTreeElement(k) for k in range(i + min)]
            archi = make_graph(i+min)

            # eseguo i vari algoritmi e registro i tempi
            lc_tmp = timer()
            connect_components_lista(archi, lc_vertex)
            lc_time[i] += timer() - lc_tmp

            lch_tmp = timer()
            connect_components_hlista(archi, lch_vertex)
            lch_time[i] += timer() - lch_tmp

            fi_tmp = timer()
            connect_components_forest(archi, fi_vertex)
            fi_time[i] += timer() - fi_tmp

        lc_time[i] /= num_iter
        lch_time[i] /= num_iter
        fi_time[i] /= num_iter

    # creo e disegno i grafici
    xAxis = [i for i in range(min, N)]
    graphRes, plotRes = plt.subplots()

    plotRes.plot(xAxis, lc_time, color="orange")
    plotRes.plot(xAxis, lch_time, color="green")
    plotRes.plot(xAxis, fi_time, color="blue")

    plotRes.set_title("Confronto calcolo CC")
    plotRes.set_ylabel("tempo impiegato (secondi)")
    plotRes.set_xlabel("dimensione vettore")

    lc_patch = mpatch.Patch(color='orange', label='lc')
    lch_patch = mpatch.Patch(color='green', label='lch')
    fi_patch = mpatch.Patch(color='blue', label='fi')
    plotRes.legend(handles=[lc_patch, lch_patch, fi_patch])

    plt.show()


if __name__ == '__main__':
    main()

