#include <algorithm>
#include <iostream>
#include <iterator>
#include <ostream>
#include <string>
class Solution {
  bool isIntDec(std::string s, bool integer = true) {
    if (s.length() && (s[0] == '+' || s[0] == '-')){
      s = s.substr(1);       // begins with sign; skip that
    }
    return s.length() > 0 && // empty not OK
           s.find_first_not_of(
            integer ? "0123456789" : ".0123456789") == std::string::npos // contains only numbers and optionally a dot
            && (integer || std::count(s.begin(), s.end(), '.') < 2 &&
                              s != "."); // if not integer, contains at most 1
                                         // dot and is not only a dot
  }

public:
  bool isNumber(std::string s) {
    size_t e = s.find_first_of("eE"); // split the string at e or E
    std::string bef_e = s.substr(0, e);
    bool bef_e_ok = isIntDec(bef_e) || isIntDec(bef_e, false); // mantissa is either integer or decimal
    bool exponent_ok = e == std::string::npos || isIntDec( s.substr(e + 1)); // either no exponent or it has to be an integer
    return bef_e_ok && exponent_ok;
  }
};

int main() {
  Solution solution;

  // Example test cases
  std::cout << std::boolalpha
            << "Example 092e359-2: " << solution.isNumber("092e359-2")
            << std::endl;
  std::cout << std::boolalpha
            << "Example 459277e38+: " << solution.isNumber("459277e38+")
            << std::endl;
  std::cout << std::boolalpha << "Example 5-e95: " << solution.isNumber("5-e95")
            << std::endl;
  std::cout << std::boolalpha << "Example 9E: " << solution.isNumber("9E")
            << std::endl;
  std::cout << std::boolalpha << "Example 6+1: " << solution.isNumber("6+1")
            << std::endl;
  std::cout << std::boolalpha << "Example 6: " << solution.isNumber(".")
            << std::endl;
  std::cout << std::boolalpha << "Example 1e: " << solution.isNumber("1e")
            << std::endl;
  std::cout << std::boolalpha << "Example --6: " << solution.isNumber("--6")
            << std::endl;
  std::cout << std::boolalpha << "Example -0.1: " << solution.isNumber("-0.1")
            << std::endl;
  std::cout << std::boolalpha << "Example +3.14: " << solution.isNumber("+3.14")
            << std::endl;
  std::cout << std::boolalpha << "Example 4.: " << solution.isNumber("4.")
            << std::endl;
  std::cout << std::boolalpha << "Example -.9: " << solution.isNumber("-.9")
            << std::endl;
  std::cout << std::boolalpha << "Example -90E3: " << solution.isNumber("-90E3")
            << std::endl;
  std::cout << std::boolalpha << "Example +6e-1: " << solution.isNumber("+6e-1")
            << std::endl;
  std::cout << std::boolalpha
            << "Example 53.5e93: " << solution.isNumber("53.5e93") << std::endl;
  std::cout << std::boolalpha
            << "Example -123.456e789: " << solution.isNumber("-123.456e789")
            << std::endl;
  std::cout << std::boolalpha << "Example e3: " << solution.isNumber("e3")
            << std::endl;
  std::cout << std::boolalpha
            << "Example 99e2.5: " << solution.isNumber("99e2.5") << std::endl;
  std::cout << std::boolalpha << "Example -+3: " << solution.isNumber("-+3")
            << std::endl;
  std::cout << std::boolalpha
            << "Example 95a54e53: " << solution.isNumber("95a54e53")
            << std::endl;
  std::cout << std::boolalpha << "Example 0 : " << solution.isNumber("0")
            << std::endl;
  std::cout << std::boolalpha << "Example abc: " << solution.isNumber("abc")
            << std::endl;
  std::cout << std::boolalpha << "Example 1a: " << solution.isNumber("1a")
            << std::endl;
  std::cout << std::boolalpha << "Example 2: " << solution.isNumber("2")
            << std::endl;
  std::cout << std::boolalpha << "Example 0089 : " << solution.isNumber("0089")
            << std::endl;
  std::cout << std::boolalpha << "Example 2e10: " << solution.isNumber("2e10")
            << std::endl;
  std::cout << std::boolalpha << "Example 3e+7: " << solution.isNumber("3e+7")
            << std::endl;

  return 0;
}
