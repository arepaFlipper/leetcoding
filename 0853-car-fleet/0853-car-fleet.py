class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs: List= [[pos,spd] for pos,spd in zip(position,speed)]

        fleets: List = []
        for pos,spd in sorted(pairs)[::-1]: # Reverse Sorted Order
            rem_dist = target-pos
            time_arriving = rem_dist / spd
            fleets.append(time_arriving)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)
