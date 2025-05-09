import numpy as np

# Fuzzy operations
def fuzzyUnion(setA, setB):
    return np.maximum(setA, setB)

def fuzzyIntersection(setA, setB):
    return np.minimum(setA, setB)

def fuzzyComplement(setA):
    return 1 - setA

def fuzzyDifference(setA, setB):
    return np.maximum(setA - setB, 0)

# Cartesian product using min
def cartesianProduct(setA, setB):
    return np.array([[min(a, b) for b in setB] for a in setA])

# Max-Min composition of 2D relation and 1D vector
def maxMinComposition(cartesian, target):
    result = []
    for row in cartesian:
        min_vals = [min(row[i], target[i]) for i in range(len(target))]
        result.append(max(min_vals))
    return np.array(result)


# Inputs
relationA = np.array([0.2, 0.4, 0.6])
relationB = np.array([0.3, 0.5, 0.7])

cart_product = cartesianProduct(relationA, relationB)
print("Cartesian Product:")
print(cart_product)

max_min_result = maxMinComposition(cart_product, relationB)
print("Max-Min Composition:")
print(max_min_result)
