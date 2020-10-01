def knapsack(weights, values, W):

    n = len(weights)
    tab = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        # check all possible maxWeight values from 1 to W
        for j in range(1, W + 1):
            if weights[i - 1] <= j:
                tab[i][j] = max(
                    tab[i - 1][j], values[i - 1] + tab[i - 1][j - weights[i - 1]]
                )
            else:
                tab[i][j] = tab[i - 1][j]

    return tab[n][W]


def main():

    values = [12, 1000, 30, 10, 1000]  
    weights = [19, 120, 20, 1, 120]  
    W = 40

    
    print("Result - {}".format(knapsack(weights, values, W)))

    return


if __name__ == "__main__":
    main()
