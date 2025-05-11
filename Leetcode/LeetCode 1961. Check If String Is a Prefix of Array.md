# LeetCode 1961. Check If String Is a Prefix of Array

**Link:** [LeetCode 1961](https://leetcode.com/problems/check-if-string-is-a-prefix-of-word/)

---

## 🧠 Problem Statement

Given a string `s` and an array of strings `words`, determine if `s` is a **prefix concatenation** of the elements in `words` in order.

In other words, is `s` a prefix string of `words`?

---

## 🧪 Example Test Cases

### Example 1:
```

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]  
Output: true  
Explanation: "i" + "love" + "leetcode" = "iloveleetcode"

```

### Example 2:
```

Input: s = "iloveleetcod", words = ["i","love","leetcode","apples"]  
Output: false  
Explanation: "iloveleetcod" is not equal to any prefix concatenation of words

````

---

## 🔍 Constraints

- `1 <= s.length <= 100`
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `s` and `words[i]` consist of lowercase English letters.

---

## 🧠 Intuition

We try to build the string `s` by adding words from the `words` array one by one and check if:

- We're still matching the prefix of `s` at each step
- If at any point `t == s`, then return true
- If length exceeds or prefix breaks, return false

---

## 🧰 Data Structures Used

- `String t` – to accumulate the words
- No extra data structure is needed

---

## ✅ Approach 1: Simulated Pointer (Commented in Code)

```java
public boolean isPrefixString(String s, String[] words) {
    int pointer = 0;

    for (String word : words) {
        if (pointer + word.length() > s.length()) return false;
        if (!s.startsWith(word, pointer)) return false;
        pointer += word.length();
        if (pointer == s.length()) return true;
    }

    return pointer == s.length();
}
````

### TC: O(n)

### SC: O(1)

---

## ✅ Approach 2: String Accumulation (Your Preferred Approach)

```java
class Solution {
    public boolean isPrefixString(String s, String[] words) {
        String t = "";

        for (String i : words) {
            if (s.startsWith(t)) {
                t += i;
            }

            if (t.length() == s.length() && t.equals(s)) return true;
            if (t.length() > s.length()) return false;
            if (!s.startsWith(t)) break;
        }

        return false;
    }
}
```

### TC: O(n) — In worst case we scan every character once

### SC: O(n) — Due to building `t`

---

## 🧠 Observations

- `startsWith()` is used to verify that `t` is still a valid prefix of `s` after each addition.
    
- Early stopping is important when `t.length() > s.length()` or prefix mismatch occurs.
    
- Approach 1 is slightly more efficient as it avoids repeated `t += i` string operations.
    
###### Ian leetcode approach 2 got 1ms because 

- Java's compiler and the JIT (Just-In-Time) compiler can **optimize string concatenation** like `t += i` into more efficient bytecode using `StringBuilder` internally.
    
- So the expected O(n²) behavior might **not actually happen** for small to medium inputs — it gets flattened out.
---
