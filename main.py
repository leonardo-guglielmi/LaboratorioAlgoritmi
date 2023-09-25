import quickFind as qf
import quickUnion as qu


def main():
    elemento = qu.Element(10)
    set1 = qu.make_set(elemento)
    elemento2 = qu.Element(12)
    set2 = qu.make_set(elemento2)
    qu.union(set1, set2)
    print(qu.find(elemento))
    print(qu.find(elemento2))

    # il del dell'insieme si può fare anche fuori dalla funzione union o lo devo mettere lì?

if __name__ == '__main__':
    main()

