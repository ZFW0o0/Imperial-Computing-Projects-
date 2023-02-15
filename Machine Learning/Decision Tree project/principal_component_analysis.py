import numpy as np
from scipy import stats


# generate the post PCA dataset given an input dataset
def calculate_pca_characteristics(attributes_data, num_to_drop=0):
    z_matrix = stats.zscore(attributes_data, axis=0)
    cov_matrix = np.cov(z_matrix, rowvar=False)
    eig_values, eig_vectors = np.linalg.eig(cov_matrix)

    # calculate contribution to variance for each eigenvector
    eig_vector_contrib = eig_values / np.sum(eig_values)

    # order the eigenvector array by the eigenvalues
    sort_ord = np.argsort(eig_values)
    sorted_eig_vectors = eig_vectors[np.flip(sort_ord)]

    # drop columns based on num_to_drop parameter
    final_eig_vectors = sorted_eig_vectors[:, :(sorted_eig_vectors.size - num_to_drop)]

    # return eigenvectors, eigenvalues, and contribution to variation by each vector
    return np.transpose(final_eig_vectors), eig_values[np.flip(sort_ord)], eig_vector_contrib[np.flip(sort_ord)]
