class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []
        
        for i in range(n):
            divisible_three = (i+1)%3 == 0
            divisible_five = (i+1)%5 == 0
            
            if not divisible_three and not divisible_five:
                answer.append(str(i+1))
            if divisible_three and divisible_five:
                answer.append("FizzBuzz")
            if divisible_three and not divisible_five:
                answer.append("Fizz")
            if not divisible_three and divisible_five:
                answer.append("Buzz")
        
        return answer