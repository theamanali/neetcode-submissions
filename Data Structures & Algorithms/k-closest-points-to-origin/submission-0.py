class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the points based on the squared distance from the origin
        sorted_points = sorted(points, key=lambda point: point[0]**2 + point[1]**2)
        # Return the first k points
        return sorted_points[:k]