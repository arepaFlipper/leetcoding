class MinStack {
public:
    stack<int> values, minimums;

    MinStack() {

    }
    
    void push(int val) {
      values.push(val);
      int previous_min = val;
      if (!minimums.empty()){
        previous_min = minimums.top();
      }
      minimums.push(min(val,previous_min));
    }
    
    void pop() {
        
    }
    
    int top() {
        
    }
    
    int getMin() {
        
    }
};
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
