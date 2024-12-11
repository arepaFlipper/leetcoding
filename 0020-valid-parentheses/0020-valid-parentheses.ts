function isValid(s: string): boolean {
  if (s.length % 2 ){
    return false;
  }
  let stack: string[] = []
  const open_bracket = ["(","[","{"];
  const close_bracket = {
    ")": "(",
    "]": "[",
    "}": "{",
  };
  for (let i=0; i<s.length; ++i){
    const c = s[i];
    if (open_bracket.some(br=>c===br)) {
      stack.push(c)
    } else if (close_bracket[c]=== stack[stack.length-1]) {
      stack.pop();
    } else {
      return false;
    }
  }
  return stack.length === 0;
};
