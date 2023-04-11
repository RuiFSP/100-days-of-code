import cv2
import numpy as np
from sklearn.cluster import KMeans


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}


def get_top_colors(img, num_colors=10):
    # Convert the image to the LAB color space
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    # Reshape the image to a 2D array of pixels and 3 color channels
    pixels = lab.reshape((-1, 3))
    # Use k-means clustering to group similar colors together
    kmeans = KMeans(n_clusters=32, random_state=42, n_init=10).fit(pixels)
    # Get the labels for each pixel
    labels = kmeans.labels_
    # Count the number of pixels in each cluster
    counts = np.bincount(labels)
    # Get the most common colors in each cluster
    colors = kmeans.cluster_centers_.astype(int)
    # Sort the colors by their frequency
    sorted_colors = colors[np.argsort(counts)[::-1]]
    return sorted_colors[:num_colors]
