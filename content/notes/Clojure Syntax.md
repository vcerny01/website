---
date: 2022-04-20
---
Clojure's syntax, like of all Lisps, is very simple.
## Forms
-   All Clojure code is written in a uniform structure
-   Clojure recognizes two kinds of structures:
	-   **Literal representations of data structures** (like numbers, strings, maps and vectors)
	-   **Operations**
-   Clojure evaluates every form to produce a value
-   All operations take the form _opening parenthesis_, _operator_, _operands_, _closing parenthesis_
	-  `(` _operator_ _operand1_ _operand2_ ... _operandn_ `)`
	-   Clojure uses whitespace to seperate operands
## Control Flow
### `if`	
```clojure
(if boolean-form 
  then-form
  optional-else-form
  )
```

### `do`
-   The operator lets you wrap up multiple forms in parentheeses and run each of them
```clojure
(if true
(do (println "Success!")
	"By Zeus's hammer!")
(do (println "Failure!")
	"By Aquaman's trident!"))
```
	
 ### `when`
 -   The when operator is like a combination of if and do, but with no else branch.
```clojure
(when true
	(println "Success!")
	"abra cadabra")
```

-   Use `when` if you want to do multiple things when some condition is true, and you always want to return nil when the condition is false.

### nil, true, flase, Truthiness, Equality and Boolean Expressions
- `nil` is used to indicate *no value*.
	- You can check if a value is `nil` with the `nil?` function
```clojure
 (nil? 1)
; => false
```
- Equality operator in Clojure is `=`
```clojure
(= 1 1)
; => true
```

- Clojure uses boolean operators are `or` and `and`
	- `or`  returns either the first truthy value or the last value
	- `and` returns the first falsey value value or, if no values are falsey, the last truthy value
### Naming values with  `def`
- Use `def` to bind a name to a value
- In other languages one would assign value to a variable and those languages usually encourage you to perform multiple assignments to the same variable
	- However in Clojure it is rarely needed to alter the name value association
## Data Structures
- Clojure comes with a handful of data structures you'll use the majority of time
- All Clojure's data structures are immutable, meaning they cannot be changed at place
### Numbers
- Clojure has quite sophisticated numerical support
- Here's an integer, a float and a ratio, respectively:
```clojure
93
1.2
1/5
```
### Strings
- Strings represent text
- Clojure only allows double quotes to delineate strings
```clojure
"Lord Voldemort"
"\"He who must not be named\""
"\"Great cow of Moscow!\" - Hermes Conrad"
```
- Clojure doesn't have string interpolation
	- String concatenation is possible using the `str` function
```clojure
(def name "Chewbacca")
(str "\"Uggllglglglglglglglll\" - " name)
; => "Uggllglglglglglglglll" - Chewbacca
```
### Maps
- Maps are a way of associating a value with some other value 
	- They are similar to dictionaries or hashes in other languages
- They are two kinds of maps in Clojure
	- **Hash** maps
	- **Sorted** maps
- Maps can be of any type: strings, numbers, maps, vectors and even functions...!
- Examples
	- empty map
		- `{}`
	- In this example, `:first-name` and `:last-name` are keywords
```clojure
{:first-name "Charlie"
:last-name "McFishwich"}```
- Here we associate "string-key" with the `+` function:
```clojure
{"string-key" +}
```
- Maps can be nested
```clojure
{:name {:first "John" :middle "Jacob" :last "Jingleheimerschmidt"}}
```
#### Working with maps
- `hash-map` function can be used to create a map
```clojure
(hash-map :a 1 :b 2)
; => {:a 1 :b 2}
```
- You can look up values in a map with `get` function
```clojure
(get {:a 0 :b 1} :b)
; => 1
(get {:a 0 :b {:c "ho hum"}} :b)
; => {:c "ho hum"}
```
- The `get-in` function lets you look up values in nested maps
```clojure
(get-in {:a 0 :b {:c "ho hum"}} [:b :c])
; => "ho hum"
```
- Another way to look up a value in a map is to treat the map like a function with the key as its argument:
```clojure
({:name "The Human Coffeepot"} :name)
; => "The Human Coffeepot"
```

### Keywords
- They are primarily used as keys in maps
```clojure
;; some keywords
:a
:rumplestiltsken
:34
:_?
;; you can look up :a in map
(:a {:a 1 :b 2 :c 3})
; => 1
```
- Keywords are usually used as a function
### Vectors
- A vector is similar to an array (it is a 0-indexed collection)
```clojure
;; vector literal
[3 2 1]
;; Returning the 0th element of a vector
(get [3 2 1] 0)
; => 3
```
- Vector elements can be of any type
- Vectors can be created with the `vector` function
```clojure
(vector "creepy" "full" "moon")
; => ["creepy" "full" "moon
```
- You can use `conj` to add additional elements to the vector
```clojure
(conj [1 2 3] 4)
; => [1 2 3 4]
```
### Lists
- Lists are similar to vectors in that they're linear collection of values
	- `'(1 2 3 4)` - to write a list literal
- If you want to retrieve elements from a list, use the `nth` function
```clojure
(nth '(:a :b :c) 2)
; => :c
```
- you cannot use `get`
	- `get` is more effective than `nth` so retrieving elements from a list is generally slower
- List values can have any type
- Lists can be created with the `list` function
```clojure
(list 1 "two" {3 4})
; => (1 "two" {3 4})
```
- Elements are added to the beginning of a list
```clojure
(conj '(1 2 3) 4)
; => (4 1 2 3)
```
### Sets
- Sets are collection of unique values
- Clojure has _hash_ sets and _sorted_ sets
- Literal notation for hashed sets:
	- `#{"kurt vonnegut" 20 :icicle}`
- Use `hash-set` to create a set
```clojure
(hash-set 1 1 2 2)
; => #{1 2}
```
- Multiple instances of a value become one unique value in a set
	- You can create sets from existing vectors and lists by using the `set` function
```clojure
(set [3 3 3 4 4])
; => #{3 4}
```
- Check for set membership using `contains?`
- Use `get` or keywords for accessing members of a set
## Functions
### Calling Functions
- As already mentioned, every Clojure operation has the same syntax: opening parenthesis, operator, operands, closing parentheses
- Function call is just another term for an operation where the operator is a function or a function expression (an expression that returns a function)
	- e.g. function expression that return `+` (addition) function
```clojure
(or + -)
; => #<core$_PLUS_ clojure.core$_PLUS_@76dace31>
((or + -) 1 2 3)
; => 6
```
- Clojure’s support for first-class functions allows you to build very powerful abstractions
	- In other languages we think usually think of functions as generalizations of operations over data instances
		- e.g.  the `+` function abstracts addition over any specific numbers.
	- By contrast, Clojure (and all Lisps) allows you to create functions that generalize over processes.
		- e.g.  `map` allows you to generalize the process of transforming a collection by applying a function—any function—over any collection.
```clojure
(map inc [0 1 2 3])
; => (1 2 3 4)
```
- Clojure has no priviliged functions
### Defining Functions
- Functions are defined with the `defn` keyword
- Functions are composed of five main parts:
	- 1. `defn` **keyword**
	- 2. Function **name**
	- 3. A **docstring** describing the function (optional)
	- 4. **Parameters** listed in brackets
	- 5. Function **body**
```clojure
(defn too-enthusiastic
"Return a cheer that might be a bit too enthusiastic"
[name]
(str "OH. MY. GOD! " name " YOU ARE MOST DEFINITELY LIKE THE BEST "
"MAN SLASH WOMAN EVER I LOVE YOU AND WE SHOULD RUN AWAY SOMEWHERE"))
```
#### Docstring
	- Can be viewed in REPL with `doc` *fn-name*
	- The docstring is also useful for generating documentation
#### Parameters
- Zero or more
	- The number of arguments is called *arity*
- The values passed are called arguments
	- Arguments can be of any type
- Functions support *arity overloading*
	- That is function can be defined so a a different function body will run with a different number of arguments
	- It is a way of providing default values tp arguments
```clojure
(defn x-chop
"Describe the kind of chop you're inflicting on someone"
([name chop-type]
(str "I " chop-type " chop " name "! Take that!"))
([name]
(x-chop name "karate")))
```
#### Rest parameter
- Functions support variable-arity by including a *rest parameter*
	- The rest parameter is indicated with an ampersand (`&`)
```clojure
defn codger
[& whippersnappers]
(map codger-communication whippersnappers))

(codger "Billy" "Anne-Marie" "The Incredible Bulk")
; => ("Get off my lawn, Billy!!!"
;"Get off my lawn, Anne-Marie!!!"
;"Get off my lawn, The Incredible Bulk!!!")
```
- You can mix rest parameters with normal parameters, but the rest has to come last
#### Destructuring
- Lets you concisely bind names to values within a collection
```clojure
;; Return the first element of a collection
(defn my-first
[[first-thing]] ; Notice that first-thing is within a vector
first-thing)

(my-first ["oven" "bike" "war-axe"])
; => "oven"

;; you can also destructure maps
(defn announce-treasure-location
[{lat :lat lng :lng}]
(println (str "Treasure lat: " lat))
(println (str "Treasure lng: " lng)))
```
#### Function body
- Can contain forms of any kind
- Clojure automatically returns the last form evaluated
### Anonymous functions
- Functions don't need to have names
- Anonymous functions are defined with the `fn` keyword
	- `(fn [`*param-list*`]` 
	  *function body*`)`
```clojure
((fn [x] (* x 3)) 8)
; => 24```
- Anonymous function can be assigned with a name
	- e.g
		- ```clojure
(def my-special-multiplier (fn [x] (* x 3)))
(my-special-multiplier 12)
; => 36
```
- Clojure has also a more compact way to create anonymous functions using *reader macros* (later on)
```clojure
(#(str %1 " and " %2) "cornbread" "butter beans")
; => "cornbread and butter beans"
(#(identity %&) 1 "blarg" :yip)
; => (1 "blarg" :yip)
```
### Returning functions
- Functions can return other functions
- The returned functions are *closures*
	- Which means that they can access all the variables that were in scope when the function was created
```clojure
(defn inc-maker
"Create a custom incrementor"
[inc-by]
#(+ % inc-by))

(def inc3 (inc-maker 3))

(inc3 7)
; => 10
```

## Other tokens
### `let`
- Similar to `using` statement in C# for example
- Helps you define a custom scope in which a name is bound to a value
- You can reference existing bindings in `let`
	- You can use rest parameters in `let` as well
	- Two main use-cases
		- Clarity in naming things
		- Allows to evaluate a value only once and reuse the result
			- Important in the case of expensive function calls, e.g. to web APIs
```clojure
(let [x 3]
x)
; => 3

(def x 0)
(let [x (inc x)] x)
; => 1
```
### `loop`
- Provides another way to do recursion in Clojure
- `loop [iteration 0]` begins the loop and introduces a binding with an initial value
```clojure
(loop [iteration 0]
(println (str "Iteration " iteration))
(if (> iteration 3)
(println "Goodbye!")
(recur (inc iteration))))
; => Iteration 0
; => Iteration 1
; => Iteration 2
; => Iteration 3
; => Iteration 4
; => Goodbye!
```
- The same thing can be accomplished just by normal function definition
```clojure
(defn recursive-printer
([]
(recursive-printer 0))
([iteration]
(println iteration)
(if (> iteration 3)
(println "Goodbye!")
(recursive-printer (inc iteration)))))
(recursive-printer)
; => Iteration 0
; => Iteration 1
; => Iteration 2
; => Iteration 3
; => Iteration 4
; => Goodbye!
```
- But `loop` is less verbose and has better performance
### [[Regular Expression]]s
- The literal notation for a regular expression is to place the expression in quotes after a hash mark: `#"regular-expression"`
- `re-find` function can be used to check whether text matches a pattern
```clojure
(re-find #"^left-" "left-eye")
; => "left-"
(re-find #"^left-" "cleft-chin")
; => nil
``` 

```clojure
(defn matching-part
[part]
{:name (clojure.string/replace (:name part) #"^left-" "right-")
:size (:size part)})
(matching-part {:name "left-eye" :size 1})
; => {:name "right-eye" :size 1}]
(matching-part {:name "head" :size 3})
; => {:name "head" :size 3}]
```