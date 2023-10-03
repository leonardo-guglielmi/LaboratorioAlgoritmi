import ListaConcatenata as lc
import ForesteInsiemiDisgiunti as fi
import numpy
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch


def make_graph(N):
    graph = numpy.random.randint(low=0, high=2, size=(N, N))
    # mi accerto che non ci siano valori sulla diagonale
    for i in range(N):
        graph[i][i] = 0
    # rendo la matrice simmetrica rispetto alla diagonale
    graph = graph + graph.T
    graph = graph >= 2
    return graph


def connect_components_lista(graph, vertex, counter):
    for v in vertex:
        lc.make_set(v)
        counter[0] += 1

    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[0]):
            if graph[i][j] is True:
                counter[1] += 2
                if lc.find(vertex[i]) is not lc.find(vertex[j]):
                    lc.union(vertex[i].set, vertex[j].set)
                    counter[2] += 1


def connect_components_hlista(graph, vertex, counter):
    for v in vertex:
        lc.heuristics_make_set(v)
        counter[0] += 1

    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[0]):
            if graph[i][j] is True:
                counter[1] += 2
                if lc.find(vertex[i]) is not lc.find(vertex[j]):
                    lc.heuristics_union(vertex[i].set, vertex[j].set)
                    counter[2] += 1

def connect_components_forest(graph, vertex, counter):
    for v in vertex:
        fi.make_set(v)
        counter[0] += 1

    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[0]):
            if graph[i][j] is True:
                counter[1] += 2
                if fi.find(vertex[i]) is not fi.find(vertex[j]):
                    fi.union(vertex[i], vertex[j])
                    counter[2] += 1


def main():
    N = 30
    min = 10
    num_iter = 100

    lc_time = numpy.zeros(N-min)
    lch_time = lc_time.copy()
    fi_time = lc_time.copy()

    lc_data = numpy.zeros(N-min)
    lch_data = lc_data.copy()
    fi_data = lc_data.copy()

    for i in range(N-min):
        print("inizio iter ", i)
        for j in range(num_iter):
            # creo i vari vertici
            lc_vertex = [lc.Element(k) for k in range(i+min)]
            lch_vertex = lc_vertex.copy()
            fi_vertex = [fi.SetTreeElement(k) for k in range(i+min)]

            # creo la matrice di adiacenza per il grafo
            graph = make_graph(i+min)

            # resetto i contatori
            lc_counter = numpy.zeros(3)  # 0-make_set,1-find,2-union
            lch_counter = numpy.zeros(3)
            fi_counter = numpy.zeros(3)

            # eseguo i vari algoritmi e registro i tempi
            lc_tmp = timer()
            connect_components_lista(graph, lc_vertex, lc_counter)
            lc_time[i] += timer() - lc_tmp

            lch_tmp = timer()
            connect_components_hlista(graph, lch_vertex, lch_counter)
            lch_time[i] += timer() - lch_tmp

            fi_tmp = timer()
            connect_components_forest(graph, fi_vertex, fi_counter)
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

