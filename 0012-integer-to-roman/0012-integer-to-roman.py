class Solution:
    def intToRoman(self, num: int) -> str:
        
        # 일단 Hash Table의 목적은 O(1)의 searching (from 컴기)
        # 특정 숫자가 들어왔을 때, 빠르게 로마 숫자를 찾아서 뱉어줄 수 있는 Hash Table을 만들어보자.
        
        # 그런데 문제는 자리수에 대한 개념이 추가되어야 한다는 것.
        # 천의 자리에 있는 1과 백의 자리에 있는 1에 대한 표현이 다르기 때문에,
        # 주어진 숫자만 믿고 converting을 하면 안되고, 자리수 정보를 함께 섞어서 converting 해야 함.
        
        # 그럼 자리수는 어떻게 알아낼 수 있을까?
        # 간단하게 접근하면 string으로 바꿔서 reverse 한 후, enumerate를 써서 idx로 처리
        # 아니면 string으로 바꾼 후, 길이를 측정해서, 길이에 따라 순차적으로 처리
        
        
        output = ""
        
        nums = str(num)
        digits = [i for i in range(len(nums))]
        digits = reversed(digits)
        
        # 1:'I', 10:'X', 100:'C', 1000:'M'
        hash_table_ten = {0:'I', 1:'X', 2:'C', 3:'M'}
        
        # 4:'IV', 40:'XL', 400:'CD'
        hash_table_four = {0:'IV', 1:'XL', 2:'CD'}
        
        # 5:'V', 50:'L', 500:'D'
        hash_table_five = {0:'V', 1:'L', 2:'D'}
        
        # 9:'IX', 90:'XC', 900:'CM'
        hash_table_nine = {0:'IX', 1:'XC', 2:'CM'}
        
        
        for digit, num in zip(digits, nums):
            value = int(num)
            if value == 0:
                continue
            if value < 4:
                for i in range(value):
                    output += hash_table_ten[digit]
            elif value == 4:
                output += hash_table_four[digit]
            elif value < 9:
                output += hash_table_five[digit]
                for i in range(value - 5):
                    output += hash_table_ten[digit]
            else:
                output += hash_table_nine[digit]
                
                    
        return output