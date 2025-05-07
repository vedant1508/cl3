import numpy as np

def fuzzyUnion(setA, setB):
    return np.maximum(setA, setB)
    
def fuzzyIntersection(setA, setB):
    return np.minimum(setA, setB)
    
def fuzzyComplement(setA):
    return 1 - setA 

def fuzzyDifference(setA, setB):
    return np.maximum(setA - setB, 0)

# Relation
def cartesianProduct(setA, setB):
    return np.outer(setA, setB)

# Min-Max composition 
def maxMinComposition(setA, setB):
    return np.max(np.minimum.outer(setA, setB), axis=1)

# if __name__ == "__main__":
setA = np.array([0.8, 0.5, 0.6, 0.4, 0.7])
setB = np.array([0.6, 0.7, 0.4, 0.5, 0.8])

# Perform fuzzy set operations
print("Fuzzy Union:", fuzzyUnion(setA, setB))
print("Fuzzy Intersection:", fuzzyIntersection(setA, setB))
print("Fuzzy Complement (setA):", fuzzyComplement(setA))
print("Fuzzy Difference (setA - setB):", fuzzyDifference(setA, setB))

        # Fuzzy relations
relationA = np.array([0.2, 0.4, 0.6])
relationB = np.array([0.3, 0.5, 0.7])
       # Perform fuzzy relation operations
print("Cartesian Product:", cartesianProduct(relationA, relationB))
print("Max-Min Composition:", maxMinComposition(relationA, relationB))