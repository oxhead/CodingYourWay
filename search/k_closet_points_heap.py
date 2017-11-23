import heapq

def k_closet_points(points, k):
    """Find out the k closet points to the origin.

    Args:
        points: a list of tuples
        k: an integer
    Returns:
        A list of k closet points.
    """

    # Python implements min heap
    distances = map(lambda point: (sum(map(lambda x: -x**2, point)), point), points)

    k_points = distances[:k]
    heapq.heapify(k_points)

    for i in range(k, len(points)):
        if distances[i] > k_points[0]:
            heapq.heapreplace(distances[i])

    return [point for _, point in k_points]
