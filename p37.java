import java.util.*;

class Euler {
    public static void main(String[] args) {
        long start_time = System.nanoTime();
        int num = 21;
        Set<Character> firstCharSet = new HashSet<Character>(Arrays.asList('2', '3', '5', '7'));
        Set<Character> lastCharSet = new HashSet<Character>(Arrays.asList('3', '7'));
        
        int amount_of_trunc_primes = 0;
        int truncatable_primes_sum = 0;
        
        while (amount_of_trunc_primes < 11) {
            num += 2;
            String numString = Integer.toString(num);
            List<Character> charList = new ArrayList<Character>();
            
            for (Character c : numString.toCharArray()) {
                charList.add(c);
            }
            
            if (firstCharSet.contains(charList.get(0)) && lastCharSet.contains(charList.get(charList.size() - 1))) {
                int numLength = charList.size();
                boolean isPrime = true;
                for (int i = 0; i < numLength; i++) {
                    List<Character> truncateLR = charList.subList(i, numLength);
                    if (!prime(truncateLR)){
                        isPrime = false;
                        break;
                    }
                }
                if (!isPrime) {
                    continue;
                }
                for (int i = 0; i < numLength; i++) {
                    List<Character> truncateRL = charList.subList(0, numLength - i);
                    if (!prime(truncateRL)) {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime) {
                    truncatable_primes_sum += num;
                    amount_of_trunc_primes += 1;
                    System.out.println(num);
                }
            }
        }
        System.out.println("Answer: " + truncatable_primes_sum);
        long nano_seconds = System.nanoTime() - start_time;
        double seconds = ((double) nano_seconds) / 1E9;
        System.out.println("Seconds: " + seconds);
    }
    public static boolean prime(List<Character> chars) {
        StringBuilder builderLR = new StringBuilder(chars.size());
        
        for (Character c : chars) {
          builderLR.append(c);
        }
        String stringLR = builderLR.toString();
        int number = Integer.parseInt(stringLR);
        List<Integer> sqrtRange = new ArrayList<Integer>();
        
        for (int i = 2; i < Math.sqrt(number) + 1; i++) {
            sqrtRange.add(i);
        }
        boolean notPrime = false;
        
        for (int i : sqrtRange) {
            if (number % i == 0 && number != 2) {
                notPrime = true;
                break;
            }
        }
        if (notPrime) {
            return false;
        } else {
            return true;
        }
        
    }
}