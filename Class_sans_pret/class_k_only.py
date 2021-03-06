from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
from pre_proc_programs import *


def km_only(dataset, n_cluster, norm_bool, liss_bool, crop_bool):

    # Pré-traitement
    pre_pro_dataset = pre_pro(dataset, norm_bool, liss_bool, crop_bool)
    pre_pro_dataset = pre_pro_dataset.reshape(len(pre_pro_dataset), -1) # Adapte le format à celui demandé par sklearn.

    # Entrainement
    print("KM Only - Fin du pré-traitement, début de l'entrainement..")
    kmeans = KMeans(n_cluster).fit(pre_pro_dataset)
    print("KM Only - Fin de l'entrainement")

    return pre_pro_dataset, kmeans


def kmedoids_only(dataset, n_cluster, norm_bool, liss_bool, crop_bool):
    # Pré-traitement
    pre_pro_dataset = pre_pro(dataset, norm_bool, liss_bool, crop_bool)

    # Changement de format (compatibilité avec KMEDOIS
    pre_pro_dataset = pre_pro_dataset.reshape(len(pre_pro_dataset), -1)

    # Entrainement
    kmedoids = KMedoids(n_clusters=n_cluster, metric='euclidean', method='alternate', init='random').fit(pre_pro_dataset)

    return pre_pro_dataset, kmedoids









