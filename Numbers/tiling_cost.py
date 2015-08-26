from locale import currency, setlocale, LC_ALL


def tiling_cost(height, width, cost):
    setlocale(LC_ALL, '')
    return currency(height*width*cost)