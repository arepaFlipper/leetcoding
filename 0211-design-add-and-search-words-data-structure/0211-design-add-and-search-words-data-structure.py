class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else: 
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# Test Case 1
word_dict_1 = WordDictionary()
result_1_1 = word_dict_1.addWord("bad")
result_1_2 = word_dict_1.addWord("dad")
result_1_3 = word_dict_1.addWord("mad")
result_1_4 = word_dict_1.search("pad")
result_1_5 = word_dict_1.search("bad")
result_1_6 = word_dict_1.search(".ad")
result_1_7 = word_dict_1.search("b..")

expected_output_1 = [None, None, None, False, True, True, True]

print("Test Case 1:")
print("Output:")
print(result_1_1)
print(result_1_2)
print(result_1_3)
print(result_1_4)
print(result_1_5)
print(result_1_6)
print(result_1_7)

if result_1_1 == expected_output_1[0] and result_1_2 == expected_output_1[1] and \
   result_1_3 == expected_output_1[2] and result_1_4 == expected_output_1[3] and \
   result_1_5 == expected_output_1[4] and result_1_6 == expected_output_1[5] and \
   result_1_7 == expected_output_1[6]:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
word_dict_2 = WordDictionary()
result_2_1 = word_dict_2.addWord("apple")
result_2_2 = word_dict_2.addWord("banana")
result_2_3 = word_dict_2.search("ap.le")
result_2_4 = word_dict_2.search("ban.na")
result_2_5 = word_dict_2.search("pineapple")
result_2_6 = word_dict_2.search(".....ple")

expected_output_2 = [None, None, True, True, False, True]

print("\nTest Case 2:")
print("Output:")
print(result_2_1)
print(result_2_2)
print(result_2_3)
print(result_2_4)
print(result_2_5)
print(result_2_6)

if result_2_1 == expected_output_2[0] and result_2_2 == expected_output_2[1] and \
   result_2_3 == expected_output_2[2] and result_2_4 == expected_output_2[3] and \
   result_2_5 == expected_output_2[4] and result_2_6 == expected_output_2[5]:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
