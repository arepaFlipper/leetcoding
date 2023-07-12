#include <algorithm>
#include <iostream>
#include <ostream>
#include <vector>
class Solution {
public:
    int numMusicPlaylists(int n, int goal, int k) {
      auto dp = std::vector<std::vector<long>>(goal+1, std::vector<long>(n+1,0));// (length of playlist, # unique sons bet yet played)
      dp[0][n] = 1;

    const int mod = 1e9 + 7;
    for(int length = 0; length < goal; length++){
      for (int unplayed = n; unplayed>= 0; unplayed--){
        int in_recent = std::min(k,length);
        int played_unrecently = n - unplayed - in_recent;

        // play a song that was already played
        
        dp[length +1][unplayed] = (dp[length+1][unplayed] + dp[length][unplayed] * played_unrecently)% mod;

        // play a song taht was not played yet

        if (unplayed > 0){
          dp[length +1][unplayed-1] = (dp[length+1][unplayed -1 ]+ dp[length][unplayed] * unplayed);
        }
      }
    }
    return dp[goal][0];
    
    }
};

int main() {
  Solution solution;

    // Example 1
    int n1 = 3;
    int goal1 = 3;
    int k1 = 1;
    int output1 = solution.numMusicPlaylists(n1, goal1, k1);
    std::cout << "Example 1: " << output1 << std::endl; // Expected output: 6

    // Example 2
    int n2 = 2;
    int goal2 = 3;
    int k2 = 0;
    int output2 = solution.numMusicPlaylists(n2, goal2, k2);
    std::cout << "Example 2: " << output2 << std::endl; // Expected output: 6

    // Example 3
    int n3 = 2;
    int goal3 = 3;
    int k3 = 1;
    int output3 = solution.numMusicPlaylists(n3, goal3, k3);
    std::cout << "Example 3: " << output3 << std::endl; // Expected output: 2

    return 0;
}
