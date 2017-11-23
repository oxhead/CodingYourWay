def k_closet_points(points, k):
    """Find out the k closet points to the origin.

    Args:
        points: a list of tuples
        k: an integer
    Returns:
        A list of k closet points.
    """

    distances = map(lambda point: sum(map(lambda x: x**2, point)), points)
    k_closet_indexs = sorted(range(len(points)), key=lambda i: distances[i])[:k]
    return [points[i] for i in k_closet_indexs]
