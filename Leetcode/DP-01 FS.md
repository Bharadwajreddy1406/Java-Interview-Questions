## 🏺 Problem: Circular Tomb Robbery (Artifact Collection)

> similar to house robber 2

### 🧾 Problem Statement

You are a stealthy archaeologist exploring a **circular ring of ancient tombs** located deep within a jungle. Each tomb contains a certain number of **precious artifacts**.

However, the tombs are protected by an ancient magical **curse**:

> If you disturb **two adjacent tombs** during the same night, the entire ring **activates a trap** that **seals you in forever**.

The tombs are arranged in a **perfect circle**, meaning the **first and last tombs are adjacent**.

You must plan your artifact retrieval carefully to **maximize** the number of artifacts collected **in a single night** without triggering the curse.

---

### ✍️ Input

An integer array `artifacts[]` where `artifacts[i]` represents the number of artifacts in the i-th tomb.

- `1 <= artifacts.length <= 100`
    
- `0 <= artifacts[i] <= 1000`
    

---

### 🟢 Output

Return the **maximum** number of artifacts you can collect without disturbing any two **adjacent** tombs on the same night.

---

### 🔍 Examples

#### Example 1

```
Input: 2 4 3
Output: 4

Explanation: You cannot loot tomb 1 (2 artifacts) and tomb 3 (3 artifacts), as they are adjacent in the circular setup.
```

#### Example 2

```
Input: 1 2 3 1
Output: 4

Explanation: You can loot tomb 1 (1 artifact) and tomb 3 (3 artifacts) safely.
Total = 1 + 3 = 4 artifacts.
```

#### Example 3

```
Input: 1 2 3
Output: 3

Explanation: Looting tomb 2 (2) and tomb 3 (3) is invalid. Best is just tomb 3 (3).
```

---

### 🧠 Intuition

- You cannot take both the first and last tombs due to the circular curse.
    
- So, split the problem into **two linear cases**:
    
    1. Consider tombs from index `0` to `n-2` (exclude the last).
        
    2. Consider tombs from index `1` to `n-1` (exclude the first).
        
- Use classic **House Robber DP** for both ranges and return the **maximum** of the two.
    

---

### 💡 Java Solution

```java
import java.util.*;

public class Solution {

    public static int func(int[] vals, int start, int index, int[] dp) {
        if (index < start) return 0;
        if (index == start) return vals[start];
        if (dp[index] != -1) return dp[index];

        int pick = vals[index] + func(vals, start, index - 2, dp);
        int np = func(vals, start, index - 1, dp);

        return dp[index] = Math.max(pick, np);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        int n = str.length;

        int[] vals = new int[n];
        for (int i = 0; i < n; i++) vals[i] = Integer.parseInt(str[i]);

        int[] dp = new int[n];
        Arrays.fill(dp, -1);
        int first = func(vals, 0, n - 2, dp);

        Arrays.fill(dp, -1);
        int second = func(vals, 1, n - 1, dp);

        System.out.print(Math.max(first, second));
    }
}
```

---
