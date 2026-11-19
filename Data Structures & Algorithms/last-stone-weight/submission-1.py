class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            heaviest = -heapq.heappop(heap)
            heaviest -= -heapq.heappop(heap)
            heapq.heappush(heap, -heaviest)
        
        if len(heap) == 1:
            return -heap[0]
        else:
            return 0