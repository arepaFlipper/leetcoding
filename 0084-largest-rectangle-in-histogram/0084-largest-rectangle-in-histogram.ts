type pair = {
  start_x: number;
  height: number;
};

function largestRectangleArea(heights: number[]): number {
  let max_area = 0;
  let stack: pair[] = [];

  for (let i = 0; i < heights.length; i++) {
    let start = i;
    while (stack.length > 0 && stack[stack.length - 1].height > heights[i]) {
      const { start_x, height } = stack.pop()!;
      const width = i - start_x;
      const area = height * width;
      max_area = Math.max(max_area, area);
      start = start_x;
    }
    stack.push({ start_x: start, height: heights[i] });
  }

  while (stack.length > 0) {
    const { start_x, height } = stack.pop()!;
    const width = heights.length - start_x;
    const area = height * width;
    max_area = Math.max(max_area, area);
  }

  return max_area;
}

