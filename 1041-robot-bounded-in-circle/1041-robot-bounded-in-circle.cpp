#include <string>

class Solution {
private:
  const int dx[4] = {0,1,0,-1};
  const int dy[4] = {1,0,-1,0};
public:
    bool isRobotBounded(std::string instructions) {
      int x=0,y=0,direction=0;
      for(int i=0; i<4; ++i){
        for(char inst : instructions){
          if(inst == 'G'){
            x += dx[direction];
            y += dy[direction];
          } else if (inst == 'R'){
            direction = (direction + 1) % 4;
          } else {
            direction = (direction + 3) % 4;
          }
        }
      }
      return x==0 && y==0;
    }
};
