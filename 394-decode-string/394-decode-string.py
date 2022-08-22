class Solution:
    def decodeString(self, s: str) -> str:
        
        # string을 담을 list
        container = []
        # bracket이 열리고 닫힘을 식별하기 위한 count 변수
        bracket_count = 0
        # bracket이 열렸을 때 bracket 안의 string을 담을 변수
        bracket = ""
                
        # string 철자 순환
        for ch in s:
            
            if ch == "[":
                
                # 최초로 열린 bracket일 경우 -> count+
                if bracket_count == 0:
                    bracket_count += 1
                    
                # 중간에 열린 bracket일 경우 -> count+ & bracket 안에 저장
                else:
                    bracket_count += 1
                    bracket += ch
            
            elif ch == "]":
                
                # 중간에 닫힌 bracket일 경우 -> count- & bracket 안에 저장
                if bracket_count > 1 :
                    bracket_count -= 1
                    bracket += ch
                    
                # 마지막에 닫힌 bracket일 경우 -> count- & bracket 안의 철자를 container에 저장
                else:
                    bracket_count -= 1
                    container.append(bracket)
                    # 저장을 끝냈으니 bracket 초기화
                    bracket = ""
            
            # bracket 안의 숫자나 문자는 bracket 안에 저장
            elif bracket_count > 0:
                bracket += ch
            
            # bracket 밖의 숫자나 문자는 container에 저장
            else:
                container.append(ch)
        
        # bracket에 곱할 숫자를 담을 변수
        number = ""
        
        # 최종 output
        output =""
        
        # container 순환
        for element in container:
            
            # 길이가 2 이상이면 bracket 이므로 해체 필요
            if len(element) > 1:
                
                # bracket 해체를 위해 재귀함수 호출 및 결과값 반환
                tmp = self.decodeString(element)
                # 곱셈 수행을 위해 string으로 저장되어 있는 number를 int로 변경
                number = int(number)
                # int로 변경한 number와 bracket 안의 string을 곱하여 최종 output에 붙임
                output += number * tmp
                # 다음 bracket을 처리를 위해 number 초기화
                number = ""
            
            # 숫자일 경우 별도로 저장 -> 나중에 int로 변환하여 곱함
            elif 48 <= ord(element) <= 57:
                number += element
            
            # 일반 글자, 또는 길이가 1개짜리인 bracket일 경우
            else:
                
                # bracket일 경우 (숫자 뒤에는 반드시 bracket이 열리므로, number != "" 이면 길이 1짜리 bracket)
                if number != "":
                    number = int(number)
                    output += number * element
                    number = ""
                    
                # 일반 글자일 경우 그대로 최종 output에 붙임
                else:
                    output += element
                
        return output