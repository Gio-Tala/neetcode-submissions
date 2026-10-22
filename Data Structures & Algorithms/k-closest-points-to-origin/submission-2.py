class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance_points = [[x**2 + y**2, x, y] for [x,y] in points]
        
        heapq.heapify(distance_points)
        outp = []

        for i in range(k):
            outp.append(heapq.heappop(distance_points)[1:])
        
        return outp