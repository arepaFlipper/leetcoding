function longestCommonPrefix(strs: string[]): string {
  let prefix: string = "";
  const words: string[] = strs;
  let first_word: string = words[0];
  for(let i=0; i<first_word.length; ++i){
    for (let j=1; j<words.length; ++j){
      const word: string = words[j];
      const c: string = word[i]
      if (i === word.length || c !== first_word[i] ){
        return prefix;
      }
    }
    prefix = prefix + first_word[i]
  }
  return prefix;
};
