import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# g(X) = tanh(X)
def g(X):
    return np.tanh(X)

# g'(X) = 1 - tanh^2 (X)
def g_prime(X):
    return 1 - g(X) ** 2

def whitening(X):
    # centering
    mean = X.mean(axis=1, keepdims=True)
    X -= mean

    # whitening
    cov_mtrx = np.cov(X)
    d, E = np.linalg.eigh(cov_mtrx)
    print(d)
    D = np.linalg.inv(np.sqrt(np.diag(d)))
    return np.dot(E, np.dot(D, np.dot(E.T, X)))

def ICA(X, max_iter=10000, e=1e-15):
    X = whitening(X)
    m, n = X.shape
    W = np.random.rand(m, m)
    for i in range(m):
        w = W[i, :]
        for j in range(max_iter):
            # calc next_w
            next_w = (X * g(np.dot(w.T, X))).mean(axis=1)\
                    - g_prime(np.dot(w.T, X)).mean() * w
            next_w /= np.linalg.norm(next_w)

            if i > 0:
                next_w -= np.dot(np.dot(next_w, W[:i].T), W[:i])

            # check distance between w & next_w
            dist = np.abs(np.abs((w * next_w).sum()) - 1)
            if dist < e:
                w = next_w
                print(j)
                break

            w = next_w
        W[i, :] = w
        print(W)

    return np.dot(W, X)
