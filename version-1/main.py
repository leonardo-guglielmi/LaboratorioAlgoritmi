import ListaConcatenata as lc
import ForesteInsiemiDisgiunti as fi
import timeLog as tl
import numpy
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


def connect_components_lista(graph, vertex, time_log):
    for v in vertex:
        lc.timed_make_set(v, time_log)

    for i in range(graph.shape[0]):
        for j in range(graph.shape[0]):
            if graph[i][j] is True and lc.timed_find(vertex[i], time_log) is not lc.timed_find(vertex[j], time_log):
                lc.timed_union(vertex[i].set, vertex[j].set, time_log)


def connect_components_hlista(graph, vertex, time_log):
    for v in vertex:
        lc.timed_heuristics_make_set(v, time_log)

    for i in range(graph.shape[0]):
        for j in range(graph.shape[0]):
            if graph[i][j] is True and lc.timed_find(vertex[i], time_log) is not lc.timed_find(vertex[j], time_log):
                lc.timed_heuristics_union(vertex[i].set, vertex[j].set, time_log)


def connect_components_foreste(graph, vertex, time_log):
    for v in vertex:
        fi.timed_make_set(v, time_log)

    for i in range(graph.shape[0]):
        for j in range(graph.shape[0]):
            if graph[i][j] is True and fi.timed_find(vertex[i], time_log) is not fi.timed_find(vertex[j], time_log):
                fi.timed_union(vertex[i].set, vertex[j].set, time_log)

def main():
    max_dim = 200
    min_dim = 10
    num_dim = max_dim - min_dim
    num_iter = 70

    lc_time = numpy.zeros(num_dim)
    lch_time = numpy.zeros(num_dim)
    fi_time = numpy.zeros(num_dim)

    for i in range(max_dim - min_dim):
        print("inizio iter con dimensione ", i)

        lc_time_log = tl.TimeLog()
        lch_time_log = tl.TimeLog()
        fi_time_log = tl.TimeLog()

        for j in range(num_iter):
            # creo i vari vertici
            lc_vertex = [lc.Element(k) for k in range(i + min_dim)]
            lch_vertex = [lc.Element(k) for k in range(i + min_dim)]
            fi_vertex = [fi.SetTreeElement(k) for k in range(i + min_dim)]

            # creo la matrice di adiacenza per il grafo
            graph = make_graph(i + min_dim)

            # eseguo i vari algoritmi e registro i tempi
            lc_time_log.t = 0
            lch_time_log.t = 0
            fi_time_log.t = 0

            connect_components_lista(graph, lc_vertex, lc_time_log)
            connect_components_hlista(graph, lch_vertex, lch_time_log)
            connect_components_foreste(graph, fi_vertex, fi_time_log)

        lc_time[i] = lc_time_log.t / num_iter
        lch_time[i] = lch_time_log.t / num_iter
        fi_time[i] = fi_time_log.t / num_iter


    # creo e disegno i grafici
    xAxis = [i for i in range(min_dim, max_dim)]
    graphRes, plotRes = plt.subplots()

    plotRes.plot(xAxis, lc_time, color="orange")
    plotRes.plot(xAxis, lch_time, color="green")
    plotRes.plot(xAxis, fi_time, color="blue")

    plotRes.set_title("Confronto calcolo CC")
    plotRes.set_ylabel("tempo impiegato (secondi)")
    plotRes.set_xlabel("numero di vertici")

    # graphCounter, plotCounter = plt.subplots()

    # plotCounter.plot(xAxis, color="orange")
    # plotCounter.plot(xAxis, color="green")
    # plotCounter.plot(xAxis, color="blue")
    # plotCounter.plot(xAxis, xAxis, color="red")

    # plotCounter.set_title("Crescita del parametro m")
    # plotCounter.set_ylabel("dimensione m")
    # plotCounter.set_xlabel("dimensione n")

    # adding labels and legends
    lc_patch = mpatch.Patch(color='orange', label='lc')
    lch_patch = mpatch.Patch(color='green', label='lch')
    fi_patch = mpatch.Patch(color='blue', label='fi')

    plotRes.legend(handles=[lc_patch, lch_patch, fi_patch])
    # plotCounter.legend(handles=[lc_patch, lch_patch, fi_patch])

    plt.show()


if __name__ == '__main__':
    main()

