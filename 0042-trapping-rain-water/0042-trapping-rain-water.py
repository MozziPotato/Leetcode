class Solution:
    def trap(self, height: List[int]) -> int:

        # 01.28 PM 8:43 ~ 10:15

        # 일단 처음에 봤을 때 생각 난 건 예전에 풀었던 water container 문제.
        # 어쩌면 double pointer로 풀어야 할 수도 있다는 점 숙지하고 시작.
        
        # 먼저 water가 담기기 위해서는 웅덩이가 있어야 함.
        # 웅덩이가 생기기 위해서는 좌, 우 기준 막대가 필요하며 그 가운데의 막대들은 좌, 우보다 낮아야 한다.
        # 따라서 가장 높은 막대를 찾으면 웅덩이가 있을 거라고 기대할 수 있다.
        # 다만 가장 높은 막대여도 웅덩이가 없을 수 있는데,
        # 1. 가장 높은 막대 바로 양 옆의 높이가 같은 경우
        # 2. 가장 높은 막대 바로 양 옆의 막대가 그 다음으로 높은 막대일 경우
        # 이므로, 이들만 제외하면 가장 높은 막대와 그 다음으로 높은 막대의 사이에는 웅덩이가 필연적으로 존재하게 된다.
        # 따라서 가장 높은 2개의 막대를 찾은 후, 그 사이를 제외한 나머지 영역에 대해 다시 위 로직을 적용하면 된다.
        # 결국 recursion 문제.

        # 그럼 base case는? water가 더 이상 담길 수 없는 경우임. 그런 경우들은 아래의 경우.
        # 1. 웅덩이를 찾으려는 영역의 막대가 2개 이하임.
        # 2. 웅덩이를 찾으려는 영역의 막대들의 높이가 모두 같음.
        # 위 내용들을 바탕으로 recursion을 짠다.

        # 웅덩이를 찾았으면 물의 양은 어떻게 계산하는가?
        # 2개의 가장 긴 막대 중 낮은 막대의 높이를 기준 값으로 삼음.
        # 사이에 있는 작은 막대기들을 for문으로 돌면서,
        # sum(낮은 막대 높이 - 사이 막대 높이)을 return

        # def recursion(heights: List[int]) -> int:

        #     # base cases
        #     if len(heights) <= 2:
        #         return 0
            
        #     if min(heights) == max(heights):
        #         return 0

        #     # find longest sticks
        #     first_longest = 0
        #     second_longest = 0
        #     first_index = 0
        #     second_index = 0
        #     for index, height in enumerate(heights):
        #         if height >= first_longest:
        #             second_longest = first_longest
        #             second_index = first_index
        #             first_longest = height
        #             first_index = index

        #     # exception for longest sticks
        #     if first_index == second_index:
        #         return recursion(heights[first_index+1:])
        #     if first_index - second_index == 1:
        #         return recursion(heights[:second_index+1]) + recursion(heights[first_index:])
        #     else:
        #         water = 0
        #         for height in heights[second_index+1:first_index]:
        #             water += second_longest - height
        #         return recursion(heights[:second_index+1]) + water + recursion(heights[first_index:])

        # return recursion(height)

        # problem: infinite recursion
        # left -> right로 탐색하다보니 가장 맨 처음 것이 가장 길 때 경우에는 
        # first_index == second_index가 되면서 maximum depth recursion error가 발생
        # 이를 처리하기 위해 가장 맨 처음 것을 제외하고 탐색하도록 처리했음 -> 그러나 [4,2,3] 같은 case에서 문제 발생.
        # 즉 first 막대가 맨 앞에 있고, 그 뒤에 second 막대가 있을 경우에는 계산을 못함.
        # 근본적인 해결이 필요함.

        # 가장 높은 막대를 찾은 후, 좌우로 탐색해서 그 다음으로 높은 막대를 찾도록 변경.
        # 좌우 각각 function을 짜준다.

        # # exception
        # if len(height) <= 2:
        #     return 0
        
        # if min(height) == max(height):
        #     return 0

        # if sorted(height) == height:
        #     return 0
        
        # def get_left_water(heights: List[int], longest: int) -> int:

        #     # base cases
        #     if len(heights) <= 1:
        #         return 0
        #     if min(heights) == max(heights):
        #         return 0

        #     # find second longest stick
        #     second_longest = 0
        #     second_index = 0
        #     for height in range(len(heights)-1, -1, -1):
        #         if heights[height] > second_longest:
        #             second_longest = heights[height]
        #             second_index = height
            
        #     # exception
        #     if second_index == len(heights):
        #         return get_left_water(heights[:len(heights)-1], second_longest)
        #     else:
        #         water = 0
        #         for height in heights[second_index+1:]:
        #             water += second_longest - height
        #         return water + get_left_water(heights[:second_index], second_longest)
        
        # def get_right_water(heights: List[int], longest: int) -> int:

        #     # base cases
        #     if len(heights) <= 1:
        #         return 0
        #     if min(heights) == max(heights):
        #         return 0

        #     # find second longest stick
        #     second_longest = 0
        #     second_index = 0
        #     for height in range(len(heights)):
        #         if heights[height] > second_longest:
        #             second_longest = heights[height]
        #             second_index = height
            
        #     # exception
        #     if second_index == 0:
        #         return get_right_water(heights[1:len(heights)], second_longest)
        #     else:
        #         water = 0
        #         for height in heights[:second_index]:
        #             water += second_longest - height
        #         return water + get_right_water(heights[second_index+1:], second_longest)

        # longest_height = 0
        # longest_index = 0

        # for index, h in enumerate(height):
        #     if h > longest_height:
        #         longest_height = h
        #         longest_index = index
        
        # return get_left_water(height[:longest_index], longest_height) + get_right_water(height[longest_index+1:], longest_height)

        # problem: 아주 긴 길이의 sorted array (319번 case)에서 time limit exceeded가 떴음.
        # sorted case에 대한 exception 처리를 해보자. -> 해결
        # problem: 막대 사이에 0 짜리 막대가 들어가 있는 경우(320번 case)에도 time limit exceeded가 떴음.
        # 여기서 든 생각 -> recursion으로 푸는 게 아닌가? 혹은 내가 푼 방식이 아예 잘못되었는가?




        # 결국 이 문제는 solution을 찾아봤고, solution의 동작 방식의 핵심은 다음과 같음.
        # 어떤 i번째 막대를 기준으로 왼쪽으로의 max와 우측으로의 max를 찾아내서, -> 2개의 list(left_max, right_max)
        # 왼쪽 max와 우측 max 중 작은 값으로부터 해당 i번째 막대의 높이를 빼면, 
        # 해당 막대의 위로 쌓이는 물의 양이 되므로 이들을 summation.
        
        # curr_max = 0
        # max_left = [curr_max:= max(curr_max, h) for h in height]
        # curr_max = 0
        # max_right = [curr_max:= max(curr_max, h) for h in reversed(height)]
        # max_right.reverse()
        # return sum([min(max_left[i], max_right[i]) - height[i] for i in range(len(height))])

        # solution 2 : index in stack
        stack = [0]
        area = 0
        for i in range(1, len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                waters = min(height[stack[-1]], height[i]) - height[top]
                area += distance * waters
            
            stack.append(i)
        return area