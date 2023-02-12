class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        # BFS를 해야 좀 더 빨리 가장 짧은 path를 찾을 수 있음.
        # 왜냐하면 DFS를 할 경우, 전부 다 탐색한 후에 가장 짧은 걸 반환해야 하는데
        # BFS는 일단 찾기만 하면 그게 가장 짧은 path가 됨.
        
        # 이것은 Graph 구조와 동일하므로 Graph부터 생성.
        # 1글자 차이나면 link를 연결.
        # -> Time Limit Exceeded
        
        # Solution
        wordset = set(wordList)
        queue = collections.deque()
        queue.append((beginWord, 1))
        word_length = len(beginWord)
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(word_length):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in wordset:
                        wordset.remove(newWord)
                        queue.append((newWord, step+1))
        return 0