import java.io.*;

class Stack {
    static int last = -1;
    static int[] stack = new int[10000];
    
    static void push(int n){
        stack[++last] = n;
    }
    
    static void pop(){
        if (last == -1) System.out.println(-1);
        else {
            System.out.println(stack[last--]);
        }
    }
    
    static void size(){
        System.out.println(last + 1);
    }
    
    static void empty(){
        System.out.println((last == -1)? 1 : 0);
    }
    
    static void top(){
        if (last == -1) System.out.println(-1);
        else System.out.println(stack[last]);
    }
}
public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        Stack s = new Stack();
        while(t-- > 0){
            String input = br.readLine(); 
            if (input.equals("size")) s.size();
            else if(input.equals("pop")) s.pop();
            else if (input.equals("empty")) s.empty();
            else if (input.equals("top")) s.top();
            else {
                String[] res = input.split(" ");
                int a = Integer.parseInt(res[1]);
                s.push(a);
            }
        }
    }
}