import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] num_arr = new int[26];
        String word = br.readLine();

        for (int i = 0; i < word.length(); i++) {
            char a = word.charAt(i);
            int k = a;
            num_arr[k-97] += 1;
        }
        for (int a : num_arr) {
            System.out.print(a+" ");
        }
    }
}