## 🧠 Problem: Add Binary

**Leetcode**: 67  
**Date**: 2025-04-12  
**Tags**: String, Binary, Simulation, Math

---

### ❓ Problem Statement

You're given two **binary strings** — for example:

```java
a = "1011"  // 11 in decimal  
b = "1101"  // 13 in decimal
````

**Goal**: Return their **sum**, also as a binary string:

```
1011
+1101
------
11000  // (11 + 13 = 24)
```

---

## 🔍 Key Idea

We add the binary digits **from right to left**, keeping track of the **carry**, just like how we perform regular binary addition.

---

### ✨ Code Breakdown

```java
int i = a.length() - 1;  // pointer for string a (rightmost bit)
int j = b.length() - 1;  // pointer for string b (rightmost bit)
int carry = 0;
StringBuilder result = new StringBuilder();
```

---

### 🔁 While Loop

```java
while (i >= 0 || j >= 0 || carry > 0)
```

This loop continues as long as:

- There are bits left in either `a` or `b`
    
- Or there’s a `carry` remaining from the previous addition
    

---

### 🧮 Inside the Loop

```java
int bitA = i >= 0 ? a.charAt(i--) - '0' : 0;
int bitB = j >= 0 ? b.charAt(j--) - '0' : 0;
int sum = bitA + bitB + carry;
carry = sum / 2;
result.append(sum % 2);
```

#### ✅ 1. Get current bits

If `i` or `j` is out of bounds, treat it as 0.

```java
bitA = i >= 0 ? a.charAt(i--) - '0' : 0;
```

#### ✅ 2. Add the bits and the carry

```java
sum = bitA + bitB + carry;
```

#### ✅ 3. Update carry

```java
carry = sum / 2;
```

#### ✅ 4. Append result bit

```java
result.append(sum % 2);
```

#### ✅ 5. Reverse and return

```java
return result.reverse().toString();
```

---

### 🧪 Example Walkthrough

For:

```
a = "1011"
b = "1101"
```

|i|j|bitA|bitB|sum|carry|result|
|---|---|---|---|---|---|---|
|3|3|1|1|2|1|0|
|2|2|1|0|2|1|0|
|1|1|0|1|2|1|0|
|0|0|1|1|3|1|1|
|-1|-1|0|0|1|0|1|

After reversing: `11000`

---

### ✅ Final Code (Java)

```java
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();

        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0 || carry > 0) {
            int bitA = i >= 0 ? a.charAt(i--) - '0' : 0;
            int bitB = j >= 0 ? b.charAt(j--) - '0' : 0;

            int sum = bitA + bitB + carry;
            carry = sum / 2;
            result.append(sum % 2);
        }

        return result.reverse().toString();
    }
}
```

---

### ⏱️ Complexity

- **Time**: `O(max(n, m))` — one pass over the longer string
    
- **Space**: `O(max(n, m))` — result string
    

---

### 💭 Reflections

- Classic binary addition simulation.
    
- Avoids converting to decimal — pure character-based processing.
    
- Clean and efficient.
    
---
