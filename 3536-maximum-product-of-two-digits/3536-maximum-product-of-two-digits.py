class Solution:
    def maxProduct(self, n: int) -> int:
        product = []
        while n > 0:
            last = n % 10
            product.append(last)
            n = n // 10
        product.sort()

        return product[-1] * product[-2]