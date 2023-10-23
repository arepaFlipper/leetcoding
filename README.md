Daily LeetCode Problem Solving

LeetCode
Python
Typescript
c++
Rust
Last Commit
Overview

This repository is dedicated to solving a LeetCode problem every day to improve coding skills and keep the algorithmic thinking sharp. Each problem's solution is provided mostly in Python and organized into separate directories for easy reference.
LeetCode Profile

    https://leetcode.com/cristian00tovar/

Directory Structure

    <id_problem>-<problem-name>/: Contains the solution and test cases for the problem.
    ...

Problem Solving Approach

I expect to follow a structured approach when solving problems, which includes:

    Problem Statement: A brief description of the problem.

    Solution: The code solution in Python.

    Explanation: A detailed explanation of the solution and its time and space complexity.

    Time Complexity: An analysis of the time complexity of the solution.

    Space Complexity: An analysis of the space complexity of the solution.

Running the Code

You can run the code by copying and pasting it into your Python environment or using an online Python IDE.

python

# Example for running a solution
python filename.py

Contribute

Feel free to contribute by adding more solutions, improving existing ones, or providing alternative solutions. Make sure to follow the contribution guidelines in the CONTRIBUTING.md file.
Acknowledgments

Thanks to LeetCode for providing a platform for honing our coding and problem-solving skills.
License

This project is licensed under the MIT License - see the LICENSE.md file for details.
Contact

If you have any questions or suggestions, feel free to contact me at your.email@example.com.

Happy coding! :rocket:

You can customize this template to your specific needs, add badges, links, and any other information you find relevant. Be sure to keep your README up-to-date as you continue to solve daily problems on LeetCode.

## Filter the `problemsSiteData.json`

```
❯ jq 'map(select(.neetcode150 == true and .pattern == "Linked List")) | sort_by(.difficulty | if . == "Easy" then 0 elif . == "Medium" then 1 else 2 end)' problemSiteData.json
```
