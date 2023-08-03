impl Solution {
    pub fn largest_rectangle_area(mut heights: Vec<i32>) -> i32 {
        let mut res: i32 = 0;
        let mut stack: Vec<usize> = Vec :: new();
        heights.push(0);
        heights.insert(0,0);

        for (index, height) in heights.iter().enumerate(){
            while stack.len() > 0 && heights[*stack.iter().last().unwrap()] > *height {
                let idx_removed = stack.pop().unwrap();
                let width = ( index - stack[stack.len() -1] -1 ) as i32;
                let area = width * heights[idx_removed];
                res = res.max(area);
            }
            stack.push(index);
        }
        res
    }
}
