// @leet start
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s: Vec<char> = s.chars()
            .filter(|c| c.is_alphanumeric())
            .map(|c| c.to_lowercase().next().unwrap())
            .collect();

        let length = s.len();

        for idx in 0..(length/2){
            if s[idx] != s[length - idx - 1] {
                return false
            }
        }

        true
    }
}
// @leet end
