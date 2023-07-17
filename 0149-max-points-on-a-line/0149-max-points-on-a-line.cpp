#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
#include <map>
struct cmp {
  /*
    a/b < c/d
    a*b < c*d
  */
  bool operator()(
    const std::pair<int, int> a,
    const std::pair<int, int> b
  ) 
  const {
    if (a.second == 0 && b.second == 0){
      return false;
    }

    if(a.second == 0){
      return true;
    }

    if(b.second == 0){
      return true;
    }

    return a.first * b.second < b.first * a.second;
  }
};
struct Frac {
  int a,b,c,d;
  bool operator < (const Frac& other)const {
    return this ->a* other.b <other.a * this->b;
  }
};

class Solution {
public:
  int maxPoints(std::vector<std::vector<int>> &points) {
    std::vector<std::pair<Frac,int>> v;

    int len = points.size();

    for(int i=0; i<len; ++i){
      int xi = points[i][0];
      int yi = points[i][1];
      for(int j=i+1; j<len; ++j){
        std::pair<int,int> xint;
        int xj = points[j][0];
        int yj = points[j][1];
        int delta_x = xi-xj;
        int delta_y = yi-yj;
        int yintercept;
        if (delta_y == 0) {
          yintercept= yj;
        } else{

        }
        Frac slope = {delta_x,delta_y};
        bool found =0;
        for(std::pair<Frac,int>& y: v){
          Frac z = y.first;
          if(z.a * slope.b == z.b*slope.a && z.c == slope.c){
            found = 1;
            ++y.second;
            break;
          }
        }
        if (!found) v.push_back({slope,1});
      }
    }
    int best = 0;
    for (auto y: v){
      best = std::max(best,y.second);
    }
    int ans = 1;

    while (ans* (ans-1)/2 != best){
      ++ans;
    }
    if (ans== 0){
      ++ans;
    }
    return ans;
  }
};
