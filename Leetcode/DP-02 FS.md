# 🤖 Robot Maze Decoder (Digit-to-Letter Navigation)

**Date**: 2025-04-23  
**Topic**: Recursive DP, String Decoding  
**Platform**: Custom Problem  
**Tags**: `Recursion`, `Backtracking`, `Digit Parsing`, `DP-Like`

---

## 🧩 Problem Statement

You're a robot navigating a maze represented as a string of digits. Each digit (or valid two-digit combination) corresponds to a letter using the mapping:

- "1" → 'A',  
- "2" → 'B',  
- ...  
- "26" → 'Z'.

You can interpret:
- A **single digit** (e.g., `"3"` → `'C'`)
- Or a **pair of digits** (e.g., `"12"` → `'L'`) if it forms a valid number between 10 and 26 (inclusive)

**Note**: A combination like `"05"` is invalid, but `"5"` is valid.

### 🎯 Objective

Count the number of distinct ways to decode the string from start to end following the valid rules.

---

## 🔍 Sample Inputs & Outputs

### 🔹 Input 1:
```

123

```

🔸 Output:
```

3

```

🧠 Explanation:  
- `1 2 3` → "ABC"  
- `12 3` → "LC"  
- `1 23` → "AW"

---

### 🔹 Input 2:
```

326

```

🔸 Output:
```

2

````

🧠 Explanation:  
- `3 2 6` → "CBF"  
- `3 26` → "CZ"

---

## 💡 Intuition

Use recursion from left to right:
- If a digit at `index` is `'0'`, return 0 (invalid start of a segment)
- Try 1-digit decode
- If next digit exists and the two-digit number ≤ 26 → try 2-digit decode

---

## 🔢 Recursive Code (Java)

```java
import java.util.*;

public class Solution{
    
    public static int func(String s, int index, int n){
        if(index >= n) return 1; // reached end successfully
        if(s.charAt(index) == '0') return 0; // invalid: can't start with '0'

        int ways = 0;

        // Try two-digit decode if possible
        if(index < s.length() - 1){
            int twoDigit = Integer.parseInt("" + s.charAt(index) + s.charAt(index + 1));
            if(twoDigit <= 26){
                ways += func(s, index + 2, n);
            }
        }

        // Try one-digit decode
        ways += func(s, index + 1, n);

        return ways;
    }
    
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(func(s, 0, s.length()));
    }
}
````

---

## 🧠 Dry Run Example

### Input: `"123"`

|Index|Path|Result|
|---|---|---|
|0 → 1|`"A"` + func(1)|→ try "B" or "W"|
|1 → 2|`"B"` + func(2)|`"C"` → `"ABC"`|
|1 → 23|`"W"`|`"AW"`|
|0 → 12|`"L"` + func(2)|`"LC"`|

Total Ways: `3`

---

## ⏱️ Complexity

|Metric|Value|
|---|---|
|Time|Exponential without memoization|
|Space|O(n) recursion depth|

✅ Memoization can optimize this to **O(n)** time.

---

## 💭 Reflections

- Similar to **LeetCode 91: Decode Ways**
    
- Can be further improved using **DP tabulation** or **memoization**
    
- Good practice for recursive backtracking problems involving branching logic
    

---
