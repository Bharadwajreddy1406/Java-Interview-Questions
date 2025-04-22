## 📘 Problem: 208. Implement Trie (Prefix Tree)

### 🔗 Link
[Leetcode 208](https://leetcode.com/problems/implement-trie-prefix-tree/)

---

### 🧠 Intuition
We want to design a data structure (Trie) to support:
- Inserting a word.
- Searching for a word.
- Checking if any word starts with a given prefix.

A Trie allows fast prefix-based search, ideal for dictionary-like problems.

---

### 🧱 Data Structures
- `Node`: Custom class that contains:
  - `child`: array of 26 Trie nodes for each lowercase letter.
  - `isEnd`: boolean flag to denote the end of a valid word.
- `Trie`: Main class with:
  - `root`: the root node of the Trie.

---

```

Insert: cat, cap, can

          (root)
          / 
        c
       /
      a
    / | \
   t  p  n

```

---
### 🔄 Functions

#### 🔹 `insert(String word)`
- Traverse each character.
- If a child node for that character doesn’t exist, create it.
- Move to the next node.
- After the loop, mark the last node’s `isEnd = true`.

#### 🔹 `search(String word)`
- Traverse the trie for the word.
- If a character path is missing, return `false`.
- At the end, check `isEnd` to verify full word match.

#### 🔹 `startsWith(String prefix)`
- Similar to `search`, but no need to check `isEnd`.
- Just validate the path exists for the given prefix.

---

### ✅ Code
```java
class Node{
    Node[] child;
    boolean isEnd;

    Node (){
        child = new Node[26];
        isEnd = false;
    }
}

class Trie {
    private Node root;
    public Trie() {
        root = new Node();
    }
    
    public void insert(String word) {
        Node node = root;
        for( char ch : word.toCharArray()){
            if(node.child[ch-'a'] == null){
                node.child[ch-'a'] = new Node();
            }
            node = node.child[ch-'a'];
        }
        node.isEnd = true;
    }
    
    public boolean search(String word) {
        Node node = root;
        for( char ch : word.toCharArray()){
            int index = ch-'a';
            if(node.child[index] == null){
                return false;
            }
            node = node.child[index];
        }
        return node.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        Node node = root;
        for( char ch : prefix.toCharArray()){
            int index = ch-'a';
            if(node.child[index] == null){
                return false;
            }
            node = node.child[index];
        }
        return true;
    }
}
````

---

### 🧠 Complexity

|Operation|Time Complexity|Space Complexity|
|---|---|---|
|insert(word)|O(n)|O(n)|
|search(word)|O(n)|O(1)|
|startsWith()|O(n)|O(1)|

Where `n` = length of the word or prefix.

---

### 🗒️ Notes

- Trie is great for prefix search, autocomplete, spell checkers.
    
- Each level corresponds to a character in the word.
    
- Array of size 26 is space-efficient for lowercase-only alphabets.
    
- Can be optimized using HashMap for dynamic character sets.
    

---

### 🧪 Test Cases

```java
Trie obj = new Trie();
obj.insert("apple");
obj.search("apple");    // true
obj.search("app");      // false
obj.startsWith("app");  // true
obj.insert("app");
obj.search("app");      // true
```

---

### 🗓️ Date Solved

12-04-2025

---
## **EXPLANATION**

Let's trace this:

```java
Trie trie = new Trie();
trie.insert("cat");
trie.search("cat");     // true
trie.search("cap");     // false
trie.startsWith("ca");  // true
```

---

### 📦 Step 1: `trie.insert("cat")`

We start from the root.

**Characters in "cat"**: `'c'`, `'a'`, `'t'`

Each character goes through:

```java
int index = ch - 'a'; // maps 'a' -> 0, ..., 'z' -> 25
```

|Char|Index|Action|
|---|---|---|
|'c'|2|`children[2] == null` → Create new node|
|'a'|0|`children[0] == null` → Create new node|
|'t'|19|`children[19] == null` → Create new node|

✔️ Finally, mark `isEndOfWord = true` at `'t'` node.

---

### 📚 Current Trie Structure (after inserting `"cat"`)

```
(root)
  |
  c (children[2])
  |
  a (children[0])
  |
  t (children[19], isEndOfWord = true)
```

---

### 🔍 Step 2: `trie.search("cat")`

We trace `'c'` → `'a'` → `'t'`:

|Char|Index|Exists in children?|
|---|---|---|
|'c'|2|✅ Yes|
|'a'|0|✅ Yes|
|'t'|19|✅ Yes|

Now check: `isEndOfWord == true`  
✅ So, `"cat"` **exists**

---

### ❌ Step 3: `trie.search("cap")`

We trace `'c'` → `'a'` → `'p'`:

|Char|Index|Exists in children?|
|---|---|---|
|'c'|2|✅ Yes|
|'a'|0|✅ Yes|
|'p'|15|❌ No (null)|

So `"cap"` **does NOT exist**

---

### 🔎 Step 4: `trie.startsWith("ca")`

Trace `'c'` → `'a'`:

|Char|Index|Exists in children?|
|---|---|---|
|'c'|2|✅ Yes|
|'a'|0|✅ Yes|

We didn’t check for `isEndOfWord` here because we just care if **any word** starts with `"ca"`.

✅ So, `"ca"` is a valid **prefix**.

---

### 🎨 Visual Summary (after inserting `"cat"`)

```
           (root)
             |
            [c]  (children[2])
             |
            [a]  (children[0])
             |
            [t]  (children[19], isEndOfWord = true)
```

- `"cat"` ✅ found
    
- `"cap"` ❌ not found
    
- `"ca"` ✅ is a valid prefix
    

---
