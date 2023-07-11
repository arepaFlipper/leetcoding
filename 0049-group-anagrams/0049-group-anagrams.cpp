#include <algorithm>
#include <unordered_map>
#include <vector>
#include <string>

class Solution {
public:
  std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string> &strs) {
    std::unordered_map<std::string, std::vector<std::string>> mp;;

    for (std::string s : strs){
      std::string t = s;
      std::sort(t.begin(), t.end());

      mp[t].push_back(s);
    }

    std::vector<std::vector<std::string>> answer;
    for(std::pair<std::string, std::vector<std::string>> group: mp){
      answer.push_back(group.second);
    }

    return answer;
  }
};
