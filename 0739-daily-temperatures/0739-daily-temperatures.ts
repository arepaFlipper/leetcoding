type T = {
  temp: number;
  idx: number;
}

function dailyTemperatures(temperatures: number[]): number[] {
  let stack: T[] = [];
  let res: number[] = new Array(temperatures.length).fill(0);

  for (let i=0; i<temperatures.length; i++){
    let cur_temp: number = temperatures[i];
    while ((stack.length > 0) && (stack[stack.length -1].temp < cur_temp) ){
      let { idx } = stack.pop();
      res[idx] = i - idx;
    }
    stack.push({ temp: cur_temp, idx:i})
  }

  return res;
};
