import numpy as nm


def checkio(data):
    data = nm.matrix(data)
    slices = []
    slices.extend(data.tolist())
    slices.extend(data.transpose().tolist())
    slices.extend([data.diagonal(i).tolist()[0] for i in range(-(data.shape[1])-4, data.shape[0]-3)])
    slices.extend([data[::-1].diagonal(i).tolist()[0] for i in range(-(data.shape[1])-4, data.shape[0]-3)])
    print(slices)
    for piece in slices:
        count = 0
        for i in range(len(piece) - 1):
            if piece[i] == piece[i+1]:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
    else:
        return False
