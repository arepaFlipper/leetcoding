class Solution:
    def isValid(self, s: str) -> bool:
        open_br_stack: List[str]= []
        correspondent_open: Dict = {
            ")":"(",
            "}":"{",
            "]":"[",
            ">":"<",
        }
        close_brackets = correspondent_open.keys()
        open_brackets = correspondent_open.values()
        for br in s:
            if br in open_brackets:
                open_br_stack.append(br)
                print("open_br_stack:",open_br_stack) ## DELETEME:
            elif br in close_brackets: 
                print("open_br_stack[-1]:",open_br_stack[-1]) ## DELETEME:
                if open_br_stack and (open_br_stack[-1] == correspondent_open[br]):
                    open_br_stack.pop()#remove the most recent open bracket from stack
                else:
                    return False
                    # return True
        
        return True if not open_br_stack else False
        # return False if not open_br_stack else True
