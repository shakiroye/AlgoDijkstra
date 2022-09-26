inf = float("inf")


def algoDijkstra(G, deb):
    # Initialisation
    S1 = []
    n = len(G)
    S2 = list(range(n))
    pi = [inf] * n
    pi[deb] = 0
    pred = [None] * n

    while S2 != []:
        # Choisir i dans S2 tel que pi[i] soit minimal
        piMin = pi[S2[0]]
        sommet = S2[0]
        for i in S2:
            if pi[i] < piMin:
                piMin = pi[i]
                sommet = i
        S2.remove(sommet)
        S1.append(sommet)

        v = []
        for j in range(n):
            if G[sommet][j] != 0 and j in S2:
                v.append(j)

        for k in v:
            if pi[sommet] + G[sommet][k] < pi[k]:
                pi[k] = pi[sommet] + G[sommet][k]
                pred[k] = sommet
    return S1, pi


G = [[0, 8, 6, 5, inf, inf, 6, 11],

     [8, 0, inf, 10, 14, 8, 10, 15],

     [6, inf, 0, 5, inf, inf, inf, inf],

     [5, 10, 5, 0, 6, inf, inf, 8],

     [inf, 14, inf, 6, 0, 10, inf, inf],

     [inf, 8, inf, inf, 10, 0, 12, inf],

     [6, 10, inf, inf, inf, 12, 0, inf],

     [11, 15, inf, 8, inf, inf, inf, 0]]

listSommets, listPi = algoDijkstra(G, 0)

a = 0
for i in range (len(listSommets)):
    print(str(listSommets[a])+" -> "+str(listSommets[i])+" = "+str(listPi[i]))

print("\nListe des sommets: " +str(listSommets))
print("\nListe des poids: " +str(listPi))