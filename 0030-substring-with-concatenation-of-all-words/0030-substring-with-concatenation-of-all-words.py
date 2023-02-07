class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # 가능한 모든 permutation을 만든 다음,
        # 우리가 word의 개수를 알고 있으며 word length가 모두 동일하다는 점을 이용해서 max length를 계산한 후,
        # 주어진 string에 대해 word length를 간격으로 jump를 시키면서,
        # 뒤이은 max length에 해당하는 string이 permutation에 존재하는지를 확인하면서 처리하는 방식이 있겠다.
        # 그런데 이 방법은 Hash를 사용하는 풀이가 아님.
        # 또한 permutation 메소드를 사용하면, 동일한 word가 중복된 경우에 대한 처리가 불가.
        
#         output = list()
#         word_length = len(words[0])
#         max_length = word_length * len(words)
        
#         permutation = [''.join(tup) for tup in permutations(words, len(words))]
        
#         for i in range(0, len(s)-max_length, word_length):
#             if s[i:i+max_length] in permutation:
#                 output.append(i)
        
#         return output

########################################################################################################
        
        # 따라서 hashing 개념을 사용해서 풀어보자.
        # 일단 탐색에 있어서는 기존의 jump 방식을 차용한다.
        # 여기서 words의 개수를 센 base dictionary를 만들고,
        # e.g., base = {'foo': 1, 'bar': 1}
        # word length 간격으로 jump하며 탐색했을 때 dictionary에 존재하는 word이면,
        # base dictionary의 개수를 차감하고 해당 word를 stack에 쌓는다.
        # 그러다가 base dictionary의 모든 value가 0이 되면 index를 계산하여 return
        # 만약 word 음수로 떨어질 경우에는 reset
        
#         output = list()
        
#         dictionary = dict()
#         word_length = len(words[0])
#         max_length = len(words)
        
#         for word in words:
#             if word not in dictionary.keys():
#                 dictionary[word] = 1
#             else:
#                 dictionary[word] += 1
    
#         stack = list()
#         index = 0
#         while index <= len(s) - word_length:
#             word = s[index:index+word_length]
#             if word not in dictionary.keys():
#                 for i in range(len(stack)):
#                     dictionary[stack.pop(0)] += 1
#                 index += 1
#             else:
#                 dictionary[word] -= 1
#                 stack.append(word)
#                 if not any(dictionary.values()):
#                     output.append(index - (max_length * word_length) + word_length)
#                 if len(stack) >= max_length:
#                     dictionary[stack.pop(0)] += 1
#                 index += word_length
                                        
#         return output
    
        # problem: 159/178 번째에서 wrong answer -> "aaaaaaaaaaaa", ["aa", "aa"]
        # 연속해서 붙어 있는 경우를 식별하지 못하는 문제 발생

########################################################################################################        
        
        # 주어진 string을 한 글자 단위 간격으로 기준점을 잡아서 슬라이딩 윈도우처럼 탐색하도록 수정.
        # 한 번 기준점을 잡았을 때에는 단어 길이 만큼의 간격을 두고, max 단어의 개수 만큼의 자리를 탐색해서, 조건에 부합하는지 확인한다.
        # 즉, list[i+(0*word_length)], list[i+(1*word_length)], ..., list[i + (max_length * word_length) - word_length)]
        # ["boo", "the", "far", "boo"] -> {"boo":1, "the":2, "far":3} -> {1:2, 2:1, 3:1}
        
        output = list()        
        dictionary = dict()
        
        for word in words:
            if word not in dictionary.keys():
                dictionary[word] = 1
            else:
                dictionary[word] += 1
                continue
        
        stack = list()
        word_length = len(words[0])
        word_num = len(words)
        max_length = word_length * word_num
        
        for i in range(len(s)-max_length+1):
            for j in range(word_num):
                word = s[i+(j*word_length):i+(j+1)*word_length]
                if word not in dictionary.keys():
                    for k in range(len(stack)):
                        dictionary[stack.pop(0)] += 1
                    break
                else:
                    if dictionary[word] == 0:
                        for k in range(len(stack)):
                            dictionary[stack.pop(0)] += 1
                        break
                    else:
                        dictionary[word] -= 1
                        stack.append(word)
                        if not any(dictionary.values()):
                            output.append(i)
                            for k in range(len(stack)):
                                dictionary[stack.pop(0)] += 1
                            break
                
                if j == word_num-1:
                    for i in range(len(stack)):
                        dictionary[stack.pop(0)] += 1
        
        
        return output