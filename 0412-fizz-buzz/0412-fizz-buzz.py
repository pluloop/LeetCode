class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        Output = []
        
        i = 0
        for i in range(i+1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                Output.append("FizzBuzz")
            elif i % 3 == 0:
                Output.append("Fizz")
            elif i % 5 == 0:
                Output.append("Buzz")
            else:
                Output.append(str(i))
        
        return Output
            