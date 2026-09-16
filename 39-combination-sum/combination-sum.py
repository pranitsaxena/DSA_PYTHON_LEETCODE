class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # Same number can be used again
                backtrack(i, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)

        return result