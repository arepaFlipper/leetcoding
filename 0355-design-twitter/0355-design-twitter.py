from typing import List
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.follow_map[userId].add(userId) # user follows himself
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                [count, tweetId] = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        while min_heap and len(res) < 10:
            (count, tweetId, followeeId, index) = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                [count, tweetId] = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index -1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
twitter = Twitter()

# Test Case 1
input_1 = [
    ["Twitter"],
    ["postTweet", 1, 5],
    ["getNewsFeed", 1],
    ["follow", 1, 2],
    ["postTweet", 2, 6],
    ["getNewsFeed", 1],
    ["unfollow", 1, 2],
    ["getNewsFeed", 1]
]
expected_output_1 = [None, None, [5], None, None, [6, 5], None, [5]]
result_1 = []

for command in input_1:
    if command[0] == "Twitter":
        twitter = Twitter()
        result_1.append(None)
    else:
        method = getattr(twitter, command[0])
        result_1.append(method(*command[1:]))

print("Test Case 1:")
print("Input:")
print("Commands:", input_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
