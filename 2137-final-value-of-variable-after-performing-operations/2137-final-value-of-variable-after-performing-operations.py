class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        pos = operations.count("X++") + operations.count("++X")
        neg = operations.count("X--") + operations.count("--X")
        return pos-neg
        