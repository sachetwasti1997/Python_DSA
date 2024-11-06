from typing import List

class Trie:
    def __init__(self, val):
        self.map = {}
        self.isEnd = False
        self.val = val

    def insert(self, word: List[str]):
        temp = self
        for i in word:
            if i == '':
                continue
            if i not in temp.map:
                temp.map[i] = Trie(i)
            temp = temp.map[i]
        temp.isEnd = True

class Solution:
    def findParent(self, res: List[str], trie: Trie, tmp: str):
        if trie.isEnd:
            res.append(tmp)
            return

        for i in trie.map:
            tmp += "/"+i
            self.findParent(res, trie.map[i], tmp)
            tmp = tmp[:-(len(i)+1)]

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie('/0')
        for path in folder:
            trie.insert(path.split("/"))
        res = []
        self.findParent(res, trie, '')
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))