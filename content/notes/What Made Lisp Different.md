---
date: 2022-04-22
---
#Article 
## Metadata
-   **Author**: Paul Graham
-   **URL**: http://www.paulgraham.com/diff.html
-   **Read in**: 2021
- [[Functional Programming]]

## Notes
-   [[Lisp]] embodied nine new ideas:
    -   **Conditionals**
        -   if-then-else construct
        -   While taken for granted today, they were invented by [[John McCarthy]]
            -   [[Fortran]] at that time had only conditional goto
    -   **Function type**
        -   Functions are first class objects in Lisp
            -   As a literal represantation, they can be stored in variables or passed as arguments
    -   **Recursion**
        -   Lisp was the first language to support it
            -   This is implied by the previous point
    -   **Variables as pointers**
        -   In Lisp, all variables are effectively pointers.
        -   Values are what have types, not variables
        -   Assigning or binding variables means copying pointers, not what they point to.
    -   **Garbage-collection**
    -   **Programs composed of expressions**
        -   Every expression returns a value
    -   **A symbol type**
        -   They differ from strings in that you can tesst equality by comparing a pointer
    -   **The whole language always available**
        -   > There is no real distinction between read-time, compile-time, and runtime. You can compile or run code while reading, read or run code while compiling, and read or compile code at runtime.
        -   > Running code at read-time lets users reprogram Lisp's syntax; running code at compile-time is the basis of macros; compiling at runtime is the basis of Lisp's use as an extension language in programs like Emacs; and reading at runtime enables programs to communicate using s-expressions, an idea recently reinvented as XML.
    -   > Lisp wasn't designed to fix the mistakes in Fortran; it came about more as the byproduct of an attempt to [axiomatize computation](http://www.paulgraham.com/rootsoflisp.html).