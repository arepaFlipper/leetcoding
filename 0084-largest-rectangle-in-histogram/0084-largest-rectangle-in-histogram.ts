type pair = {
  start_x: number;
  height: number;
};

function largestRectangleArea(heights: number[]): number {
    let max_area = 0;
    let stack = [];
    // for (let i = 0; i < heights.length; i++) {
  
    heights.forEach((curr_h, i) => {
        let start = i;
        while (stack.length > 0 && stack[stack.length - 1].height > curr_h) {
            let { start_x, height } = stack.pop();
            const width = i - start_x;
            const area = height * width;
            max_area = Math.max(max_area, area);
            start = start_x;
        }
        stack.push({start_x: start, height:curr_h});
    });

    stack.forEach(({start_x, height}, jdx) => {
      const current_area = height * (heights.length - start_x );
      max_area = Math.max(max_area, current_area);
    });

    return max_area;
};


