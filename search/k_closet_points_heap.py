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

    k_points = []
    # maintain a min heap with size k
    for i in range(k):
        heapq.heappush(k_points, distances[i])
    heapq.heapify(k_points)

    for i in range(k, len(points)):
        if distances[i] > k_points[0]:
            k_points[0] = distances[i]
            heapq.heapify(k_points)

    return [point for _, point in k_points]
