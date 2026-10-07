class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = sorted(zip(position, speed), reverse = True)
        x = 0
        for i in range(len(position)):
            stack[i] = (target - stack[i][0]) / (stack[i][1])
            if stack[i] > x:
                x = stack[i]
            else:
                stack[i] = x
        hashset = set(stack)
        print(hashset)
        return len(hashset)