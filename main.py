import linked_list as ll
import set_forest as sf

import numpy
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch


def make_graph(N):
    graph = numpy.random.randint(low=0, high=2, size=(N, N))

    for i in range(N):
        graph[i][i] = 0

    graph = graph + graph.T
    graph = graph > 1
    return graph


def connect_components_ll(graph, vertex, counter):
    for v in vertex:
        ll.make_set(v)
        counter[0] += 1

    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[0]):
            if graph[i][j]:
                counter[1] += 2
                if ll.find(vertex[i]) != ll.find(vertex[j]):
                    ll.union(vertex[j].set, vertex[i].set)
                    counter[2] += 1


def connect_components_llh(graph, vertex, counter):
    for v in vertex:
        ll.heuristics_make_set(v)
        counter[0] += 1

    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[0]):
            if graph[i][j]:
                counter[1] += 2
                if ll.find(vertex[i]) != ll.find(vertex[j]):
                    ll.heuristics_union(vertex[i].set, vertex[j].set)
                    counter[2] += 1


def connect_components_forest(graph, vertex, counter):
    for v in vertex:
        sf.make_set(v)
        counter[0] += 1

    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[0]):
            if graph[i][j]:
                counter[1] += 2
                if sf.find(vertex[i]).name != sf.find(vertex[j]).name:
                    sf.union(vertex[i], vertex[j])
                    counter[2] += 1


def main():
    max_dim = 510
    min_dim = 10
    dim = max_dim - min_dim
    num_iter_for_dim = 100

    ll_time = numpy.zeros(dim)
    llh_time = ll_time.copy()
    sf_time = ll_time.copy()

    ll_operation_counter = numpy.zeros((3, dim))  # 0 make_set, 1 find, 2 union
    llh_operation_counter = numpy.zeros((3, dim))
    sf_operation_counter = numpy.zeros((3, dim))

    for i in range(dim):
        print(">> inizio iter ", i)

        for j in range(num_iter_for_dim):

            ll_vertex = [ll.Element(k) for k in range(i + min_dim)]
            llh_vertex = ll_vertex.copy()
            fi_vertex = [sf.Element(k) for k in range(i + min_dim)]

            graph = make_graph(i + min_dim)

            # run all connect-components algorithms ad record their time
            ll_begin = timer()
            connect_components_ll(graph, ll_vertex, ll_operation_counter[:, i])
            ll_time[i] += timer() - ll_begin

            llh_begin = timer()
            connect_components_llh(graph, llh_vertex, llh_operation_counter[:, i])
            llh_time[i] += timer() - llh_begin

            sf_begin = timer()
            connect_components_forest(graph, fi_vertex, sf_operation_counter[:, i])
            sf_time[i] += timer() - sf_begin

        ll_time[i] /= num_iter_for_dim
        llh_time[i] /= num_iter_for_dim
        sf_time[i] /= num_iter_for_dim

        ll_operation_counter[0, i] /= num_iter_for_dim
        ll_operation_counter[1, i] /= num_iter_for_dim
        ll_operation_counter[2, i] /= num_iter_for_dim
        llh_operation_counter[0, i] /= num_iter_for_dim
        llh_operation_counter[1, i] /= num_iter_for_dim
        llh_operation_counter[2, i] /= num_iter_for_dim
        sf_operation_counter[0, i] /= num_iter_for_dim
        sf_operation_counter[1, i] /= num_iter_for_dim
        sf_operation_counter[2, i] /= num_iter_for_dim

    x_axis = [i for i in range(min_dim, max_dim)]

    graph_res, plot_res = plt.subplots()
    plot_res.plot(x_axis, ll_time, color="orange")
    plot_res.plot(x_axis, llh_time, color="lime")
    plot_res.plot(x_axis, sf_time, color="cyan")
    plot_res.set_title("Confronto calcolo algoritmi componenti connesse")
    plot_res.set_ylabel("tempo impiegato (secondi)")
    plot_res.set_xlabel("numero di vertici nel grafo")

    graph_count_ll, plot_count_ll = plt.subplots()
    plot_count_ll.plot(x_axis, ll_operation_counter[0], color="red")
    plot_count_ll.plot(x_axis, ll_operation_counter[1], color="green")
    plot_count_ll.plot(x_axis, ll_operation_counter[2], color="blue")
    plot_count_ll.set_title("Operazioni eseguite con LINKED LIST")
    plot_count_ll.set_ylabel("numero operazioni")
    plot_count_ll.set_xlabel("numero di vertici nel grafo")

    graph_count_llh, plot_count_llh = plt.subplots()
    plot_count_llh.plot(x_axis, llh_operation_counter[0], color="red")
    plot_count_llh.plot(x_axis, llh_operation_counter[1], color="green")
    plot_count_llh.plot(x_axis, llh_operation_counter[2], color="blue")
    plot_count_llh.set_title("Operazioni eseguite con HEURISTICS LINKED LIST")
    plot_count_llh.set_ylabel("numero operazioni")
    plot_count_llh.set_xlabel("numero di vertici nel grafo")

    graph_count_sf, plot_count_sf = plt.subplots()
    plot_count_sf.plot(x_axis, sf_operation_counter[0], color="red")
    plot_count_sf.plot(x_axis, sf_operation_counter[1], color="green")
    plot_count_sf.plot(x_axis, sf_operation_counter[2], color="blue")
    plot_count_sf.set_title("Operazioni eseguite con SET FOREST")
    plot_count_sf.set_ylabel("numero operazioni")
    plot_count_sf.set_xlabel("numero di vertici del grafo")

    graph_count_ll_normalized, plot_count_ll_normalized = plt.subplots()
    plot_count_ll_normalized.plot(x_axis, ll_operation_counter[0], color="red")
    plot_count_ll_normalized.plot(x_axis, ll_operation_counter[1]/100, color="green")
    plot_count_ll_normalized.plot(x_axis, ll_operation_counter[2], color="blue")
    plot_count_ll_normalized.set_title("Operazioni eseguite con LINKED LIST (normalizzato)")
    plot_count_ll_normalized.set_ylabel("numero operazioni")
    plot_count_ll_normalized.set_xlabel("numero di vertici nel grafo")

    graph_count_llh_normalized, plot_count_llh_normalized = plt.subplots()
    plot_count_llh_normalized.plot(x_axis, llh_operation_counter[0], color="red")
    plot_count_llh_normalized.plot(x_axis, llh_operation_counter[1]/100, color="green")
    plot_count_llh_normalized.plot(x_axis, llh_operation_counter[2], color="blue")
    plot_count_llh_normalized.set_title("Operazioni eseguite con HEURISTICS LINKED LIST (normalizzato)")
    plot_count_llh_normalized.set_ylabel("numero operazioni")
    plot_count_llh_normalized.set_xlabel("numero di vertici nel grafo")

    graph_count_sf_normalized, plot_count_sf_normalized = plt.subplots()
    plot_count_sf_normalized.plot(x_axis, sf_operation_counter[0], color="red")
    plot_count_sf_normalized.plot(x_axis, sf_operation_counter[1]/100, color="green")
    plot_count_sf_normalized.plot(x_axis, sf_operation_counter[2], color="blue")
    plot_count_sf_normalized.set_title("Operazioni eseguite con SET FOREST (normalizzato)")
    plot_count_sf_normalized.set_ylabel("numero operazioni")
    plot_count_sf_normalized.set_xlabel("numero di vertici del grafo")

    ll_patch = mpatch.Patch(color='orange', label='linked list')
    llh_patch = mpatch.Patch(color='lime', label='linked list heuristics')
    sf_patch = mpatch.Patch(color='cyan', label='set forest')
    plot_res.legend(handles=[ll_patch, llh_patch, sf_patch])

    num_make_patch = mpatch.Patch(color='red', label='make_set')
    num_find_patch = mpatch.Patch(color='green', label='find')
    num_union_patch = mpatch.Patch(color='blue', label='union')
    plot_count_ll.legend(handles=[num_make_patch, num_find_patch, num_union_patch])
    plot_count_llh.legend(handles=[num_make_patch, num_find_patch, num_union_patch])
    plot_count_sf.legend(handles=[num_make_patch, num_find_patch, num_union_patch])

    num_find_normalized_patch = mpatch.Patch(color='green', label='find (normalizzato)')
    plot_count_ll_normalized.legend(handles=[num_make_patch, num_find_normalized_patch, num_union_patch])
    plot_count_llh_normalized.legend(handles=[num_make_patch, num_find_normalized_patch, num_union_patch])
    plot_count_sf_normalized.legend(handles=[num_make_patch, num_find_normalized_patch, num_union_patch])

    plt.show()


if __name__ == '__main__':
    main()

