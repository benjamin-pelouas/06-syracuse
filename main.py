from plotly.graph_objects import Scatter, Figure


### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Affiche le graphique de la suite de Syracuse."""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({'layout': {'title': {'text': title},
                             'xaxis': {'title': {'text': "x"}},
                             'yaxis': {'title': {'text': "y"}},
                             }
                  }
                 )

    x = [i for i in range(len(lsyr))]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None


#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    if n <= 0:
        return []  # La suite n'est définie que pour n > 0

    l = [n]  # On initialise la liste avec le premier terme
    while n != 1:
        if n % 2 == 0:  # n est pair
            n = n // 2
        else:  # n est impair
            n = 3 * n + 1
        l.append(n)  # On ajoute le nouveau terme à la liste
    return l


def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    if not l:  # Si la liste est vide
        return 0

    # Le temps de vol est le nombre d'étapes (flèches)
    # Pour [3, 10, 5], il y a 3 termes et 2 étapes.
    # C'est donc la longueur - 1
    return len(l) - 1


def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    if not l:  # Si la liste est vide
        return 0

    n_depart = l[0]  # Le terme de départ (ex: 6)
    n_count = 0

    # On boucle sur la liste SAUF le premier terme (l[1:])
    for valeur in l[1:]:
        # On compte si la valeur est > au terme de départ
        if valeur > n_depart:
            n_count += 1

    # Pour n=6 (l=[6, 3, 10, 5, 16, 8,...]), les valeurs > 6 sont 10, 16, 8.
    # n_count sera 3.
    return n_count


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    if not l:  # Si la liste est vide
        return 0

    # La fonction max() de Python fait le travail
    return max(l)


#### Fonction principale


def main():
    """Fonction principale pour tester les fonctions."""

    # Test avec n=3 (Exemple du README)
    print("--- Test n=3 (Exemple README) ---")
    lsyr_3 = syracuse_l(3)
    print(f"Suite : {lsyr_3}")
    print(f"Temps de vol : {temps_de_vol(lsyr_3)}")  # Attendu: 7
    print(f"Temps de vol en altitude : {temps_de_vol_en_altitude(lsyr_3)}")  # Attendu: 5
    print(f"Altitude maximale : {altitude_maximale(lsyr_3)}")  # Attendu: 16
    # syr_plot(lsyr_3) # On peut le décommenter pour voir le graphique

    print("\n--- Test n=15 (Votre test initial) ---")
    lsyr = syracuse_l(15)
    print(f"Suite : {lsyr}")
    print(f"Temps de vol : {temps_de_vol(lsyr)}")
    print(f"Temps de vol en altitude : {temps_de_vol_en_altitude(lsyr)}")
    print(f"Altitude maximale : {altitude_maximale(lsyr)}")
    syr_plot(lsyr)  # Ouvre le graphique pour n=15


if __name__ == "__main__":
    main()

