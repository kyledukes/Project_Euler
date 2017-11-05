import java.util.*;

class Euler {
    public static void main(String[] args) {
        long start_time = System.nanoTime();
        int num = 11;
        Set<Integer> abundantSet = new HashSet<Integer>();
    
        while (num < 28123){
            num ++;
            int sum = 0;
            int half = num / 2;
            ArrayList<Integer> halfRange = new ArrayList<Integer>();
            
            for (int i = 1; i <= half; i++) {
                halfRange.add(i);
            } 
            for (int n : halfRange) {
                if (num % n == 0){
                    sum += n;
                }
            }
            if (sum > num){
                abundantSet.add(num);
            }
        }
        int non_abundants_sum = 0;
        int number = 0;
       
        while (number < 28123){
            number++;
            boolean notAbundantSum = true;
            
            for (int abundant : abundantSet) {
                int diff = number - abundant;
                if (abundantSet.contains(diff)) {
                    notAbundantSum = false;
                    break;
                }
            }
            if (notAbundantSum) {
                non_abundants_sum += number;
            }
        }
        System.out.println("Answer: " + non_abundants_sum);
        long nano_seconds = System.nanoTime() - start_time;
        double seconds = ((double) nano_seconds) / 1E9;
        System.out.println("Seconds: " + seconds);
    }
}