// @leet start
impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        if s.is_empty() || s.starts_with('0'){
            return 0;
        }

        let mut dp = vec![0; s.len() +1 ];
        dp[0] = 1;
        dp[1] = if s.chars().nth(0).unwrap() != '0' { 1 } else { 0 };

        for i in 2..=s.len(){
            let one_digit = s[i-1..i].parse::<i32>().unwrap();
            let two_digits = s[i-2..i].parse::<i32>().unwrap();

            if one_digit >= 1 && one_digit <= 9 {
                dp[i] += dp[i-1];
            }

            if two_digits >= 10 && two_digits <= 26 {
                dp[i] += dp[i-2];
            }
        }

        dp[s.len()]
        
    }
}


// @leet end
