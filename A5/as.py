import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# Data points
data = [[1, 1], [2, 2], [2, 4], [1, 2]]

# Calculate the distance matrix using Euclidean distance
distance_matrix = sch.distance.pdist(data)

# Perform single-link clustering
linkage_matrix = sch.linkage(distance_matrix, method='single')

# Generate the dendrogram
plt.figure(figsize=(8, 6))
dendrogram = sch.dendrogram(linkage_matrix, labels=["A", "B", "C", "D"])
plt.title("Dendrogram (Single-Link Clustering)")
plt.xlabel("Data Points/Clusters")
plt.ylabel("Distance")
plt.show()