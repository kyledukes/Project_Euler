import java.util.*;
import java.io.*;

class Euler {
    public static void main(String[] args) throws IOException {
        File temp = new File("p42_words.txt");
        Scanner file = new Scanner(temp);
        String words = new String(file.nextLine());
        char[] alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
        HashMap<Character, Integer> letterScores = new HashMap<Character, Integer>();

        for (int i = 0; i < 26; i++) {
            letterScores.put(alphabet[i], i + 1);
        }
        Set<Integer> triangleNumbers = new HashSet<Integer>();
        int num = 1;

        while (triangleNumbers.size() < 18) {
            num++;
            int sum = 0;
            for (int i = 0; i < num; i++) {
                sum += i;
            }
            triangleNumbers.add(sum);
        }
        int total = 0;
        for (String w : words.split(",")) {
            String word = w.replace("\"", "");
            int wordScore = 0;

            for (char ch : word.toCharArray()) {
                wordScore += letterScores.get(ch);
            }
            if (triangleNumbers.contains(wordScore)) {
                total++;
            }
        }
        System.out.println(total);
    }
}
