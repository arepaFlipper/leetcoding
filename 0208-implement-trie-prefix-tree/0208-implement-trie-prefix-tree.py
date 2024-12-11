class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# Test Case 1
trie_1 = Trie()
result_1_1 = trie_1.insert("apple")
result_1_2 = trie_1.search("apple")
result_1_3 = trie_1.search("app")
result_1_4 = trie_1.startsWith("app")
result_1_5 = trie_1.insert("app")
result_1_6 = trie_1.search("app")

expected_output_1 = [None, True, False, True, None, True]

print("Test Case 1:")
print("Output:")
print(result_1_1)
print(result_1_2)
print(result_1_3)
print(result_1_4)
print(result_1_5)
print(result_1_6)

if result_1_1 == expected_output_1[0] and result_1_2 == expected_output_1[1] and \
   result_1_3 == expected_output_1[2] and result_1_4 == expected_output_1[3] and \
   result_1_5 == expected_output_1[4] and result_1_6 == expected_output_1[5]:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
trie_2 = Trie()
result_2_1 = trie_2.search("a")
result_2_2 = trie_2.startsWith("a")
result_2_3 = trie_2.insert("abc")
result_2_4 = trie_2.search("abc")
result_2_5 = trie_2.startsWith("ab")

expected_output_2 = [False, False, None, True, True]

print("\nTest Case 2:")
print("Output:")
print(result_2_1)
print(result_2_2)
print(result_2_3)
print(result_2_4)
print(result_2_5)

if result_2_1 == expected_output_2[0] and result_2_2 == expected_output_2[1] and \
   result_2_3 == expected_output_2[2] and result_2_4 == expected_output_2[3] and \
   result_2_5 == expected_output_2[4]:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
