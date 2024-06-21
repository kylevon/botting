import numpy as np
import matplotlib.path as mpath

def generate_gaussian_position(min_x, max_x, min_y, max_y):
    # Calculate the center and standard deviation for the Gaussian distribution
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    std_dev_x = (max_x - min_x) / 6  # 99.7% of values fall within the range in a Gaussian distribution
    std_dev_y = (max_y - min_y) / 6

    while True:
        # Generate random positions using Gaussian distribution
        x = np.random.normal(center_x, std_dev_x)
        y = np.random.normal(center_y, std_dev_y)

        # Check if the position is within the square
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return int(x), int(y)

def polygon_centroid(vertices):
    """
    Calculate the centroid of a polygon.

    :param vertices: A list of tuples [(x1, y1), (x2, y2), ..., (xn, yn)] representing the vertices of the polygon.
    :return: A tuple (cx, cy) representing the centroid of the polygon.
    """
    x_coords = [vertex[0] for vertex in vertices]
    y_coords = [vertex[1] for vertex in vertices]
    centroid_x = sum(x_coords) / len(vertices)
    centroid_y = sum(y_coords) / len(vertices)
    return centroid_x, centroid_y

def max_length(vertices):
    """
    Calculate the maximum length between any two vertices of the polygon.

    :param vertices: A list of tuples [(x1, y1), (x2, y2), ..., (xn, yn)] representing the vertices of the polygon.
    :return: The maximum length between any two vertices.
    """
    max_len = 0
    for i, v1 in enumerate(vertices):
        for v2 in vertices[i+1:]:
            length = np.hypot(v2[0] - v1[0], v2[1] - v1[1])
            if length > max_len:
                max_len = length
    return max_len

def random_point_in_polygon(vertices):
    """
    Generate a random point inside the polygon with higher probability near the centroid.

    :param vertices: A list of tuples [(x1, y1), (x2, y2), ..., (xn, yn)] representing the vertices of the polygon.
    :return: A tuple (x, y) representing the random point inside the polygon.
    """
    centroid = polygon_centroid(vertices)
    max_len = max_length(vertices)
    std_dev = max_len / 4
    path = mpath.Path(vertices)

    while True:
        point = np.random.normal(centroid, std_dev, size=2)
        if path.contains_point(point):
            return tuple(point)

def generate_gaussian(mean, sd):
    return np.random.normal(mean, sd)

if __name__ == "__main__":
    # Example usage
    min_x, max_x = 10, 20
    min_y, max_y = 15, 25

    random_position = generate_gaussian_position(min_x, max_x, min_y, max_y)
    print(f'Random Position: {random_position}')
