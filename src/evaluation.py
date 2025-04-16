import matplotlib.pyplot as plt
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans

def compute_inertia(model):
    return model.inertia_

def plot_elbow_method(df, k_range=(1, 11)):
    inertias = []
    for k in range(*k_range):
        model = KMeans(n_clusters=k, init='random', random_state=42)
        model.fit(df)
        inertias.append(model.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(*k_range), inertias, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.grid(True)
    plt.show()

def visualize_elbow(df, k_range=(1, 11)):
    model = KMeans(init='random', random_state=42)
    visualizer = KElbowVisualizer(model, k=k_range)
    visualizer.fit(df)
    visualizer.show()