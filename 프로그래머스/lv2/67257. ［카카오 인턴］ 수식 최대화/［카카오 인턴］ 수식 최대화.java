import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.lang.Math;

class Solution {
    public long solution(String expression) {
        long answer = 0;
        ArrayList<String> split_exp = new_split(expression);
        Operation[] ops_rule = new Operation[3];
        ops_rule[0] = new Operation("+",1);
        ops_rule[1] = new Operation("-",2);
        ops_rule[2] = new Operation("*",3);
        for(int i=0;i<3;i++){
        ops_rule[1].order = 3;
        ops_rule[2].order = 2;
        ops_rule = ops_sort(ops_rule);
        answer = (answer<calc_array(split_exp,ops_rule))?calc_array(split_exp,ops_rule):answer;
        ops_rule[0].order =2;
        ops_rule[1].order =1;
        ops_rule = ops_sort(ops_rule);
        answer = (answer<calc_array(split_exp,ops_rule))?calc_array(split_exp,ops_rule):answer;
        }
        return answer;
    }
    
    
    public static ArrayList<String> new_split(String exp){
        int start_index=0;
        ArrayList<String> result = new ArrayList<String>();
        for(int i=0;i<exp.length();i++){
            if(exp.charAt(i)=='+'||exp.charAt(i)=='-'||exp.charAt(i)=='*'){
                result.add(exp.substring(start_index,i));
                result.add(exp.substring(i,i+1));
                start_index=i+1;
            }
            if(i==exp.length()-1){
                result.add(exp.substring(start_index,i+1));
            }
        }
        return result;
    }
    
   public static long calc_array(ArrayList<String> exp, Operation[] ops_rule){
    long result=0;
    ArrayList<String> temp = (ArrayList<String>)exp.clone();
    while(temp.contains(ops_rule[0].opr)){
        int index = temp.indexOf(ops_rule[0].opr);
        temp.add(index+2,Long.toString(calc_string(temp.get(index-1),temp.get(index+1),temp.get(index))));
        for(int i=0;i<3;i++)temp.remove(index-1);
    }
    while(temp.contains(ops_rule[1].opr)){
        int index = temp.indexOf(ops_rule[1].opr);
        temp.add(index+2,Long.toString(calc_string(temp.get(index-1),temp.get(index+1),temp.get(index))));
        for(int i=0;i<3;i++)temp.remove(index-1);
    }
    while(temp.contains(ops_rule[2].opr)){
        int index = temp.indexOf(ops_rule[2].opr);
        temp.add(index+2,Long.toString(calc_string(temp.get(index-1),temp.get(index+1),temp.get(index))));
        for(int i=0;i<3;i++)temp.remove(index-1);
    }
    return Math.abs(Long.parseLong(temp.get(0)));
}
    
    public static long calc_string(String a, String b, String ops){
    long a_long = Long.parseLong(a);
    long b_long = Long.parseLong(b);
    switch(ops){
        case "+":
            return a_long+b_long;
        case "-":
            return a_long-b_long;
        case "*":
            return a_long*b_long;
    }
    return 0;
}
    
    public class Operation{
        String opr;
        int order;
        
        Operation(String s, int i){
            this.opr = s;
            this.order = i;
        }
        
        public int getOrder(){
            return order;
        }
        public String getOpr(){
            return opr;
        }
    }
    
    public Operation[] ops_sort(Operation[] ops){
            Arrays.sort(ops, new Comparator<Operation>(){
                public int compare(Operation o1, Operation o2){
                    return o1.getOrder()-o2.getOrder();
                }
            });
            Operation[] result = new Operation[ops.length];
            for(int i=0;i<ops.length;i++){
                result[i]= new Operation(ops[i].getOpr(),ops[i].getOrder());
            }
            return result;
        }
}