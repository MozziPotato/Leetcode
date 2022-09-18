class Solution:
    def canIWin(self, maxChoosableInter: int, desiredTotal: int) -> bool:
        seen = {}

        def CheckIfICanWin(choices, remainTotal):
            if max(choices) >= remainTotal:
                return True

            selected = tuple(choices)
            if selected in seen:
                return seen[selected]

            for i in range(len(choices)):
                if not CheckIfICanWin(choices[:i] + choices[i + 1:], remainTotal - choices[i]):
                    seen[selected] = True
                    return True

            seen[selected] = False
            return False

        sumTotal = (maxChoosableInter) * (maxChoosableInter + 1) / 2

        if sumTotal < desiredTotal:
            return False
        if sumTotal == desiredTotal:
            return maxChoosableInter % 2

        choices = [i for i in range(1, maxChoosableInter + 1)]

        return CheckIfICanWin(choices, desiredTotal)