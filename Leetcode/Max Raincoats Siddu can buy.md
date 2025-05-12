# 🧠 Max Rain Coats Siddu Can Buy

`#greedy` `#sorting` `#arrays` `#java`

#### 📌 Problem Statement

Siddu wants to get some rain coats before the rainy season begins.  
There are `N` rain coats in a store. He is provided an array `price[]`, where `price[i]` represents the dollar price of the `i-th` rain coat.

Siddu has `D` dollars to spend, and he wants to buy as many rain coats as he can, to give to his family and friends as gifts.

Your task is to assist Siddu in purchasing the **maximum number of rain coats** possible using `D` dollars.

**Note:** Siddu can purchase the rain coats in any order.

**Input Format:**

```
Line-1: Two space separated integers, N and D  
Line-2: N space separated integers, prices of N rain coats.
```

**Output Format:**

```
Print an integer result.
```

#### 🧪 Test Cases

```
Input:
7 15  
6 12 7 5 13 10 1

Output:
3
```

```
Input:
10 3  
15 13 11 4 11 5 9 14 14 5

Output:
0
```

#### ✅ Code

```java
import java.util.*;

public class Solution {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int d = sc.nextInt();
        
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        
        Arrays.sort(arr);
        
        int c = 0;
        for (int i = 0; i < n; i++) {
            if (d - arr[i] >= 0) {
                c++;
                d -= arr[i];
            }
        }
        
        System.out.println(c);
    }
}
```

#### 📊 Complexity

- Time Complexity: `O(N log N)` (due to sorting)
    
- Space Complexity: `O(1)`
    

---
