# LeetCode 401 – Binary Watch

**Link:** [LeetCode 401](https://leetcode.com/problems/binary-watch/)

---

## 🧠 Problem Statement

A binary watch has 4 LEDs for the **hour (0–11)** and 6 LEDs for the **minute (0–59)**.

You're given an integer `on` representing the number of LEDs that are currently on.  
Return all possible times the watch could represent.

Each valid time should be formatted as `"H:MM"` with leading zeros in the minute if needed.

---

## ✅ Code (Java – Backtracking Approach)

```java
import java.util.*;

class Solution {

    public int[] hours = {1, 2, 4, 8};
    public int[] minutes = {1, 2, 4, 8, 16, 32};

    public void solve(List<String> res, int on, int hoursOn, int minutesOn, int index) {
        if (on == 0) {
            if (hoursOn < 12 && minutesOn < 60) {
                res.add(String.format("%d:%02d", hoursOn, minutesOn));
            }
            return;
        }

        for (int i = index; i < hours.length + minutes.length; i++) {
            if (i < hours.length) {
                solve(res, on - 1, hoursOn + hours[i], minutesOn, i + 1);
            } else {
                solve(res, on - 1, hoursOn, minutesOn + minutes[i - hours.length], i + 1);
            }
        }
    }

    public List<String> readBinaryWatch(int on) {
        List<String> res = new ArrayList<>();
        solve(res, on, 0, 0, 0);
        return res;
    }
}
````

---

## 💡 Notes

- This problem is **combinatorial**, requiring all valid selections of `on` LEDs.
    
- We try **all combinations** of turning on `on` LEDs out of the 10 total (4 for hours, 6 for minutes).
    
- We don't need a visited array or separate hours/minutes list – we loop over a combined range and split based on index.
    

---

## 🔍 Intuition

- Treat the LEDs as an array of size 10: `[h0,h1,h2,h3,m0,m1,m2,m3,m4,m5]`.
    
- Use **backtracking** to choose `on` LEDs from this array.
    
- At each step, either:
    
    - Add to `hoursOn` if it's an hour LED.
        
    - Add to `minutesOn` if it's a minute LED.
        
- Once `on == 0`, check if it's a valid time and add it in `"H:MM"` format.
    

---

## 🛠️ Formatting Edge Cases

- **Hour must be `< 12`**
    
- **Minute must be `< 60`**
    
- Use `String.format("%d:%02d", h, m)` to handle `07` → `"07"` formatting for minutes.
    

---

## 🧮 Time & Space Complexity

- **Time:** O(C(10, on)) – choosing `on` LEDs out of 10.
    
- **Space:** O(on) recursion + output list.
    

---

## ✅ Test Cases

```text
Input: on = 1
Output: [
  "0:01", "0:02", "0:04", "0:08", "0:16", "0:32",
  "1:00", "2:00", "4:00", "8:00"
]

Input: on = 2
Output includes:
  "0:03", "0:05", "0:09", "0:17", "0:33", ...
  "1:01", "1:02", ..., "2:01", "3:00", ...
```

---

## 🌳 Backtracking Flow (Simplified)

For `on = 2`:

- Start from index 0:
    
    - Try hours`[0]` = 1 → remaining on = 1
        
        - Try hours`[1]` = 2 → on = 0 → 3:00 ✅
            
        - Try minutes`[0]` = 1 → on = 0 → 1:01 ✅
            
        - etc...
            

---

##  Observations

> The main idea is to try all possible combinations.  
> We loop over 10 possible LED positions (4 for hours, 6 for minutes).  
> If `i < 4`, it's an hour LED. Else, it's a minute LED.  
> Backtracking is used to choose exactly `on` LEDs.  
> Formatting and bounds checking (hour < 12, minute < 60) are key.

