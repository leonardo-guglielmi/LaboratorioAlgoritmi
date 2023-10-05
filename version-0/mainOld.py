import ListaConcatenataOld as lc
import ForesteInsiemiDisgiuntiOld as fi
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
    return graph


def connect_components_lista(graph, vertex, counter):
    for v in vertex:
        lc.make_set(v)
        counter[0] += 1

    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[0]):
            if graph[i][j] == 1:
                counter[1] += 2
                if lc.find(vertex[i]) is not lc.find(vertex[j]):
                    counter[2] += 1
                    lc.union(vertex[i].set, vertex[j].set)


def connect_components_hlista(graph, vertex, counter):
    for v in vertex:
        lc.heuristics_make_set(v)
        counter[0] += 1

    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[0]):
            if graph[i][j] == 1:
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
            if graph[i][j] == 1:
                counter[1] += 2
                if fi.find(vertex[i]) is not fi.find(vertex[j]):
                    fi.union(vertex[i], vertex[j])
                    counter += 1


def main():
    N = 410
    min = 10
    num_iter = 100

    lc_time = numpy.zeros(N-min)
    lch_time = lc_time.copy()
    fi_time = lc_time.copy()

    lc_operation_counter = numpy.zeros((3, N-min)) # 0 make_set, 1 find, 2 union
    lch_operation_counter = numpy.zeros((3, N-min))
    fi_operation_counter = numpy.zeros((3, N-min))

    begin_timestamp = timer()
    for i in range(N-min):
        print("inizio iter ", i)
        for j in range(num_iter):
            # creo i vari vertici
            lc_vertex = [lc.Element(k) for k in range(i+min)]
            lch_vertex = lc_vertex.copy()
            fi_vertex = [fi.SetTreeElement(k) for k in range(i+min)]

            # creo la matrice di adiacenza per il grafo
            graph = make_graph(i+min)

            if i == 0 and j == 0:
                print(graph)
                print(graph[0])
                print((graph[:, 0])[5])

            # eseguo i vari algoritmi e registro i tempi
            lc_tmp = timer()
            connect_components_lista(graph, lc_vertex, lc_operation_counter[:, i])
            lc_time[i] += timer() - lc_tmp

            lch_tmp = timer()
            connect_components_hlista(graph, lch_vertex, lch_operation_counter[:, i])
            lch_time[i] += timer() - lch_tmp

            fi_tmp = timer()
            connect_components_forest(graph, fi_vertex, fi_operation_counter[:, i])
            fi_time[i] += timer() - fi_tmp

        lc_time[i] /= num_iter
        lch_time[i] /= num_iter
        fi_time[i] /= num_iter

        lc_operation_counter[0, i] /= num_iter
        lc_operation_counter[1, i] /= num_iter
        lc_operation_counter[2, i] /= num_iter
        lch_operation_counter[0, i] /= num_iter
        lch_operation_counter[1, i] /= num_iter
        lch_operation_counter[2, i] /= num_iter
        fi_operation_counter[0, i] /= num_iter
        fi_operation_counter[1, i] /= num_iter
        fi_operation_counter[2, i] /= num_iter

    print("Tempo totale di esecuzione: ", timer() - begin_timestamp)

    # creo e disegno i grafici
    xAxis = [i for i in range(min, N)]
    graphRes, plotRes = plt.subplots()
    plotRes.plot(xAxis, lc_time, color="orange")
    plotRes.plot(xAxis, lch_time, color="green")
    plotRes.plot(xAxis, fi_time, color="blue")
    plotRes.set_title("Confronto calcolo CC")
    plotRes.set_ylabel("tempo impiegato (secondi)")
    plotRes.set_xlabel("dimensione vettore")

    graphCountLc, plotCountLc = plt.subplots()
    plotCountLc.plot(xAxis, lc_operation_counter[0], color="red")
    plotCountLc.plot(xAxis, lc_operation_counter[1], color="purple")
    plotCountLc.plot(xAxis, lc_operation_counter[2], color="cyan")
    plotCountLc.set_title("Numero istruzioni LC")
    plotCountLc.set_ylabel("numero operazioni")
    plotCountLc.set_xlabel("dimensione vettore")

    graphCountLch, plotCountLch = plt.subplots()
    plotCountLch.plot(xAxis, lch_operation_counter[0], color="red")
    plotCountLch.plot(xAxis, lch_operation_counter[1], color="purple")
    plotCountLch.plot(xAxis, lch_operation_counter[2], color="cyan")
    plotCountLch.set_title("Numero istruzioni LCH")
    plotCountLch.set_ylabel("numero operazioni")
    plotCountLch.set_xlabel("dimensione vettore")

    graphCountFi, plotCountFi = plt.subplots()
    plotCountFi.plot(xAxis, fi_operation_counter[0], color="red")
    plotCountFi.plot(xAxis, fi_operation_counter[1], color="purple")
    plotCountFi.plot(xAxis, fi_operation_counter[2], color="cyan")
    plotCountFi.set_title("Numero istruzioni FI")
    plotCountFi.set_ylabel("numero operazioni")
    plotCountFi.set_xlabel("dimensione vettore")

    lc_patch = mpatch.Patch(color='orange', label='lc')
    lch_patch = mpatch.Patch(color='green', label='lch')
    fi_patch = mpatch.Patch(color='blue', label='fi')
    plotRes.legend(handles=[lc_patch, lch_patch, fi_patch])

    num_make_patch = mpatch.Patch(color='red', label='make_set')
    num_find_patch = mpatch.Patch(color='purple', label='find')
    num_union_patch = mpatch.Patch(color='cyan', label='union')
    plotCountLc.legend(handles=[num_make_patch, num_find_patch, num_union_patch])
    plotCountLch.legend(handles=[num_make_patch, num_find_patch, num_union_patch])
    plotCountFi.legend(handles=[num_make_patch, num_find_patch, num_union_patch])

    plt.show()


if __name__ == '__main__':
    main()

