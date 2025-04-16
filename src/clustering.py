from sklearn.cluster import KMeans

def run_kmeans(df, k=5, init_method='random'):
    kmeans = KMeans(n_clusters=k, init=init_method, random_state=42)
    kmeans.fit(df)
    return kmeans

def assign_clusters(df, model):
    labels = model.predict(df)
    df['Cluster'] = labels
    return df, labels
