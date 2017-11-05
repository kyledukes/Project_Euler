import java.util.*;

class Euler {
    public static void main(String[] args) {
        long start_time = System.nanoTime();
        // starting from the largest pandigital number
        int num = 987654321;
        while (true) {
            num -= 2;
            String numString = Integer.toString(num);
            ArrayList<Integer> intList = new ArrayList<Integer>();
            Set<Character> charSet = new HashSet<Character>();
            boolean containsZero = false;
            
            for (Character c : numString.toCharArray()) {
                if (c == '0') {
                    containsZero = true;
                    break;
                }
                int a = Character.getNumericValue(c);
                charSet.add(c);
                intList.add(a);
            }
            if (containsZero) {
                continue;
            }
            if (intList.size() != charSet.size()) {
                continue;
            }
            ArrayList<Integer> groundTruthDigits = new ArrayList<Integer>();
            for (int i = 1; i < intList.size() + 1; i++) {
                groundTruthDigits.add(i);
            }
            Collections.sort(intList);
            if (!intList.equals(groundTruthDigits)) {
                continue;
            }
            ArrayList<Integer> sqrtRange = new ArrayList<Integer>();
            for (int i = 3; i < Math.sqrt(num) + 1; i+=2) {
                sqrtRange.add(i);
            }
            boolean notPrime = false;
            for (int i : sqrtRange) {
                if (num % i == 0) {
                    notPrime = true;
                    break;
                }
            }
            if (notPrime) {
                continue;
            }
            System.out.println("Answer: " + num);
            long nano_seconds = System.nanoTime() - start_time;
            double seconds = ((double) nano_seconds) / 1E9;
            System.out.println("Seconds: " + seconds);
            break;

        }
    }
}