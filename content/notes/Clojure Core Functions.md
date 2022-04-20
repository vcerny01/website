---
date: 2022-04-20
---
Some functions from [[Clojure]] `clojure.core`

- Data structures in [[Clojure]] implement **abstractions**
	- e.g. this allows `map` to work with different data structures
	- Clojure does this using *indirection*
		- > In programming, indirection is a generic term for the mechanisms a language employs so that one name can have multiple, related meanings.
		- Clojure has two ways of doing indirection
			- *Polymorphism*
				- Allows function to dispatch different function bodies based on the type supplied
			- Lightweight type conversion
## **Seq** functions examples
### `map`
- Elements of the first collection passed to `map` are used as the first argument for the mapping function `str`, the elements of the second collection are passed as the second argument and so on
```clojure
(map str ["a" "b" "c"] ["A" "B" "C"])
; => ("aA" "bB" "cC")

; it's as if map did the following
(list (str "a" "A") (str "b" "B") (str "c" "C"))
```
### `reduce`
- Used for deriving a new value from a seqable data structure
```clojure
(reduce (fn [new-map [key val]]
	(assoc new-map key (inc val)))
	{}
	{:max 30 :min 10})
; => {:max 31, :min 11}
```
### `take`, `drop`, `take-while`, `drop-while`
- `take` and `drop` both take two arguments: a number and a sequence
		- `take` returns the first *n* elements of the sequence
		- whereas `drop` returns a sequence with the first *n* elements removed
		- e.g.
```clojure
(take 3 [1 2 3 4 5 6 7 8 9 10])
; => (1 2 3)
(drop 3 [1 2 3 4 5 6 7 8 9 10])
; => (4 5 6 7 8 9 10)
```
- `take-while` and `drop-while` take a *predicate function* (a function whose value is evaluated for truth or falsity) to determine when it should stop taking or dropping
### `filter` and `some`
- Use `filter` to return all elements of a sequence that test true for a predicate function
- Use `some` to know if a collection contains any values that test true for a predicate function, `some` returns a boolean
```clojure
(filter #(< (:human %)
5) food-journal)
; => ({:month 2 :day 1 :human 4.9 :critter 2.1}
;	{:month 3 :day 1 :human 4.2 :critter 3.3}
;	{:month 3 :day 2 :human 4.0 :critter3.8}
;	{:month 4 :day 1 :human 3.7 :critter 3.9}
;	{:month 4 :day 2 :human 3.7 :critter 3.6})
```
### `sort` and `sort-by`
- Elements can be sorted in ascending order with `sort`
- If sorting gets more complicated `sort-by` can be used, which applies  a function to the elements of a sequence and use the values it returns to determine the sort order
```clojure
(sort-by count ["aaa" "c" "bb"])
; => ("c" "bb" "aaa")
```
### `concat`
- Concat simply appends the memebers of one sequence to the end of another
```clojure
(concat [1 2] [3 4])
; => (1 2 3 4)
```
## **Lazy Seqs**
- Many functions, including `map` and `filter` return a *lazy seq*
- A *lazy seq* is a seq whose members aren't computed until you try to access them
	- computing a seq's members is called *realizing* the seq
## The **Collection** Abstraction
- While the sequence abstraciton is about operating on members individually, the collection abstraction is about the data structure as a whole
### `into`
- lets you convert seq into other data structures
```clojure
(map identity {:sunlight-reaction "Glitter!"})
; => ([:sunlight-reaction "Glitter!"])
(into {} (map identity {:sunlight-reaction "Glitter!"}))
; => {:sunlight-reaction "Glitter!"}

(into {:favorite-emotion "gloomy"} [[:sunlight-reaction "Glitter!"]])
; => {:favorite-emotion "gloomy" :sunlight-reaction "Glitter!"}
(into ["cherry"] '("pine" "spruce"))
; => ["cherry" "pine" "spruce"]
```
### `conj`
- also adds elements to a collection but in a slightly different way 
	- > You’ll often see two functions that do the same thing, except one takes a rest parameter (`conj`) and one takes a seqable data structure (`into`).
```clojure
(conj [0] 1)
; => [0 1]
(conj [0] [1])
; => [0 [1]]
(conj [0] 1 2 3 4)
; => [0 1 2 3 4]
(conj {:time "midnight"} [:place "ye olde cemetarium"])
; => {:place "ye olde cemetarium" :time "midnight"}
```
## **Function** functions
### `apply`
- apply explodes a seqable data structure so it can be passed to a function that expects a rest parameter.
```clojure
(apply max [0 1 2])
; => 2
```
### `partial`
- Takes a function and any number of arguments. It then returns a new function. When you call the returned function, it calls the original function with the original arguments you supplied it along with the new arguments
```clojure
(def add10 (partial + 10))
(add10 3)
; => 13

(def add-missing-elements
(partial conj ["water" "earth" "air"]))
(add-missing-elements "unobtainium" "adamantium")
; => ["water" "earth" "air" "unobtainium" "adamantium"]
```

- `partial` can be useful when you find yourself repeating the same combination of functions and arguments in many different contexts

### `complement`
- *Complements* the negation of a Boolean function
	- Whereas `not` returns a boolean value immediately, `complement` returns a function
```clojure
(def not-vampire? (complement vampire?))
(defn identify-humans
[social-security-numbers]
(filter not-vampire?
	(map vampire-related-details social-security-numbers)))

(defn my-complement
[fun]
(fn [& args]
	(not (apply fun args))))

(def my-pos? (complement neg?))
(my-pos? 1)
; => true
```