class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed), key=lambda x:x[0], reverse=True))
        position, speed = list(position), list(speed)
        
        stk = []
        num_fleet = 1
        for p, s in zip(position, speed):
            current_time = (target - p) / s
            while stk and current_time > stk[-1]:
                stk.pop()
                if not stk:
                    num_fleet += 1
            if stk and current_time < stk[-1]:
                current_time = stk[-1]
            
            stk.append(current_time)
        return num_fleet
