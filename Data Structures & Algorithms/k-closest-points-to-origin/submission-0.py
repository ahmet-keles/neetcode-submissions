class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, [-math.sqrt((points[i][0]) ** 2 + (points[i][1]) ** 2), points[i][0], points[i][1]])

        for i in range(k, len(points)):
            distance = -math.sqrt((points[i][0]) ** 2 + (points[i][1]) ** 2)
            low = heap[0][0]
            if distance > low:
                heapq.heappop(heap)
                heapq.heappush(heap, [distance, points[i][0], points[i][1]])
        return [item[1:] for item in heap]