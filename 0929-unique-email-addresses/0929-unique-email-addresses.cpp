class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
      unordered_set<string> email_set;
      
      for(string email: emails){
        string local = "", domain = "";
        bool in_local = true; // are no in in_local or not
        bool before_plus = true; // have we hit a plis sign yet?

        for (char c: email){
          if (c == '@'){
            in_local = false;
            continue;
          }

          if (in_local) {
            if (c == '+'){
              before_plus = false;
            }

            if (c != '.'){
              if (before_plus){
                local += c;
              }
            }
          } else {
            domain += c;
          }
        }
        string final_email = local + "@" + domain;
        email_set.insert(final_email);
      }
      return email_set.size();
        
    }
};
