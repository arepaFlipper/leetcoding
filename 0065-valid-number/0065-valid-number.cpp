#include <iterator>
#include <ostream>
#include <string>
#include <iostream>
class Solution {
private:
  bool isSymbol(char character){
    if (character == '+'|| character == '-') return true;
    return false;
  }

  bool isDigit(char character){
    if('0'<=character && character <= '9'){
      return true;
    }
    return false;
  }

  bool isExp(char character){
    if(character == 'e' || character == 'E'){
      return true;
    }
    return false;
  }
public:
  bool isNumber(std::string s) {
    bool dot=false, e=false; 
    int symbol=0;
    std::string bef_dot ="", af_dot="", af_e="";

    for(int i=0;i<af_e.size(); i++){
      if(!('0'<=af_e[i]&& af_e[i] <= '9')){
        return false;
      }
    }

    for(char c: s){
      if(c=='.'){
        if(dot || e){
          return false;
        }
        dot=true;
      }
      if(c=='e'||c=='E'){
        if(e){
          return false;
        }
        e=true;
      } if(isSymbol(c)){
        symbol= symbol +1;
      } else {
        if (e){
          af_e += c;
        } else if (dot){
          af_dot += c;
        } else {
          bef_dot += c;
          if(!('0'<=c && c <= '9')&&(c!='-')&&( c!='+')){
            return false;
          }
        }
      }
    }
    for(int i=0;i<s.size(); i++){
      if(isSymbol(s[i])){
        if(i>0){
          if(!e){
            return false;
          }
          if(s[i+1]=='e'){
            return false;
          }
          if(i==s.size()-1){
            return false;
          }
          if(isDigit(s[i+1]) && !isExp(s[i-1])){
            return false;
          }
        }
        

      }
    }

    if (dot){
      if(bef_dot == "" && af_dot == "."){
        return false;
      }

      if(bef_dot.length()>0 && (bef_dot[0]=='+' || bef_dot[0]=='-')){
        bef_dot = bef_dot.substr(1);
      }

      if(bef_dot=="" && af_dot==""){
        return false;
      }

      for(int i = 0; i< bef_dot.size(); ++i){
        if(!('0'<= bef_dot[i] && bef_dot[i] <= '9')){
          // is not a number
          if(i>0 || (bef_dot[i] != '+' && bef_dot[i] != '-')){
            return false;
          }
        }
      }

      for(int i = 0; i< af_dot.size(); ++i){
        if(!('0'<= af_dot[i] && af_dot[i] <= '9')){
          // is not a number
          if(i>0 || (af_dot[i] != '+' && af_dot[i] != '-' && af_dot[i] != '.')){
            return false;
          }
        }
      }
    } else {
      if(bef_dot.length()>0 && (bef_dot[0]=='+' || bef_dot[0]=='-')){
        bef_dot = bef_dot.substr(1);
      }

      if(bef_dot == "") {
        return false;
      }

    }

    if(e){
      if(af_e.length()>0 && (isSymbol(af_e[0]))){
        af_e = af_e.substr(1);
      }
      if(af_e=="e" || af_e=="E"){
        return false;
      }
      for(int i=0;i<af_e.size(); i++){
        if(!('0'<=af_e[i]&& af_e[i] <= '9')){
          if(i>0){
            return false;
          }
        }
      }
    }
    if (symbol>1){
      if(('0'<=af_e[0]&& af_e[0] <= '9')|| (!e)){
        return false;
      }
    }

    /* if(symbol=1&&(af_e[0]!='+' || af_e[0]!='-'||bef_e[0])){ */
    /* } */

    return true;
  }
};

int main() {
    Solution solution;

    // Example test cases
    std::cout << std::boolalpha << "Example 092e359-2: " << solution.isNumber("092e359-2") << std::endl;
    std::cout << std::boolalpha << "Example 459277e38+: " << solution.isNumber("459277e38+") << std::endl;
    std::cout << std::boolalpha << "Example 5-e95: " << solution.isNumber("5-e95") << std::endl;
    std::cout << std::boolalpha << "Example 9E: " << solution.isNumber("9E") << std::endl;
    std::cout << std::boolalpha << "Example 6+1: " << solution.isNumber("6+1") << std::endl;
    std::cout << std::boolalpha << "Example 6: " << solution.isNumber(".") << std::endl;
    std::cout << std::boolalpha << "Example 1e: " << solution.isNumber("1e") << std::endl;
    std::cout << std::boolalpha << "Example --6: " << solution.isNumber("--6") << std::endl;
    std::cout << std::boolalpha << "Example -0.1: " << solution.isNumber("-0.1") << std::endl;
    std::cout << std::boolalpha << "Example +3.14: " << solution.isNumber("+3.14") << std::endl;
    std::cout << std::boolalpha << "Example 4.: " << solution.isNumber("4.") << std::endl;
    std::cout << std::boolalpha << "Example -.9: " << solution.isNumber("-.9") << std::endl;
    std::cout << std::boolalpha << "Example -90E3: " << solution.isNumber("-90E3") << std::endl;
    std::cout << std::boolalpha << "Example +6e-1: " << solution.isNumber("+6e-1") << std::endl;
    std::cout << std::boolalpha << "Example 53.5e93: " << solution.isNumber("53.5e93") << std::endl;
    std::cout << std::boolalpha << "Example -123.456e789: " << solution.isNumber("-123.456e789") << std::endl;
    std::cout << std::boolalpha << "Example e3: " << solution.isNumber("e3") << std::endl;
    std::cout << std::boolalpha << "Example 99e2.5: " << solution.isNumber("99e2.5") << std::endl;
    std::cout << std::boolalpha << "Example -+3: " << solution.isNumber("-+3") << std::endl;
    std::cout << std::boolalpha << "Example 95a54e53: " << solution.isNumber("95a54e53") << std::endl;
    std::cout << std::boolalpha << "Example 0 : " << solution.isNumber("0") << std::endl;
    std::cout << std::boolalpha << "Example abc: " << solution.isNumber("abc") << std::endl;
    std::cout << std::boolalpha << "Example 1a: " << solution.isNumber("1a") << std::endl;
    std::cout << std::boolalpha << "Example 2: " << solution.isNumber("2") << std::endl;
    std::cout << std::boolalpha << "Example 0089 : " << solution.isNumber("0089") << std::endl;
    std::cout << std::boolalpha << "Example 2e10: " << solution.isNumber("2e10") << std::endl;
    std::cout << std::boolalpha << "Example 3e+7: " << solution.isNumber("3e+7") << std::endl;

    return 0;
}
