---
date: 2022-04-20
---
## Pure functions
-   A function is pure if it:
	-   Always return the same result if given the same arguments
		-   This is called _referential transparency_
	-   Can't cause any side effects
		-   Cannot make changes outside of the function itself
-   Pure functions are as stable and problem free as artithmetic

## Immutable data structures
-   [[Clojure]] has **immutable data structures**
    -   Meaning they cannot be changed in place
        -   This ensures your code won't have any side effects
-   Living with immutable data structures
	-   Recursion instead of `for`/`while`
		-   Better use for performance reasons
	-   Function composition instead of attribute mutation
		-   > This comparison also starts to reveal some limitations of object-oriented programming (OOP). In OOP, one of the main purposes of classes is to protect against unwanted modification of private data—something that isn’t necessary with immutable data structures. You also have to tightly couple methods with classes, thus limiting the reusability of the methods. In the Ruby example, you have to do extra work to reuse the clean! method. In Clojure, clean will work on any string at all. By both a) decoupling functions and data, and b) programming to a small set of abstractions, you end up with more reusable, composable code. You gain power and lose nothing.
		-   > In OOP, you think about data as something you can embody in an object, and you poke and prod it until it looks right. During this process, your original data is lost forever unless you’re very careful about preserving it. By contrast, in functional programming you think of data as unchanging, and you derive new data from existing data. During this process, the original data remains safe and sound.
##  Functions for working with pure functions
### `comp`
- Can be used for composing functions
```clojure
((comp inc *) 2 3)
; => 7
```

 ### `memoize`
-   If a function with a certain argument is called with only the first call will take longer, every subsequent call will return immediately
	-   Useful for functions with referential transperency
-   [e.g.](https://clojuredocs.org/clojure.core/memoize#example-542692ccc026201cdc326c75)