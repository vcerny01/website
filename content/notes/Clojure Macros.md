---
date: 2022-04-20
---
## Clojure's Evaluation Model
- Two-phase system
	- Reads textual code, producing data structures
	- Evaluating data structures
- Languages that have this relationship between source code, data, and evaluation are called *homoiconic*
##  [[Abstract Syntax Tree]]
- > Programming languages require a compiler or interpreter for translating the code you write, which consists of Unicodecharacters, into something else: machine instructions, code in another programming language, whatever. During this process, the compiler constructs an abstract syntax tree (AST), which is a data structure that represents your program. You can think of the AST as the input to the evaluator, which you can think of as a function that traverses the tree to produce the machine code or whatever as its output.
- Process of a non-[[Lisp]] language, where AST is inaccessible
	- ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FVitecek%2FG_Jo1toqli.png?alt=media&token=64336732-2c3a-4885-979f-a773de83b841)
- Lisps are different, they evelaute native data structures
    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FVitecek%2Fztj027i8Nq.png?alt=media&token=4a434780-ffc1-4961-8530-650d17c68ade)
- The evaluator doesn't care where its inputs come from; it doesn't have to come from a reader
	- As a result, you can send your program's data structures directly to Clojure evaluator with `eval`
```clojure
(def addition-list (list + 1 2))
(eval addition-list)
; => 3
```
## The reader
- Textual represantation of data structures is called *reader form*
- Reading and evaluation are discrete processes
- One way to interact directly with the reader is using the `read-string` function
- Many simple reader forms have one-to-one relationship to corresponding data structures
- *Reader macros*
	- Sets of rules for transforming text into data structures
		- They are designated by *macro characters* like `'`, `#` and `@`
## The evaluator
- > You can think of Clojure’s evaluator as a function that takes a data structure as an argument, processes the data structure using rules corresponding to the data structure’s type, and returns a result.
	- To evaluate a symbol, Clojure looks up what the symbol refers to.
		- Clojure resolves a symbol by:
			- Looking up whether the symbl names a special form. If it doesn't...
			- Looking up whether the symbol corresponds to a local binding. If it doesn’t...
			- Trying to find a namespace mapping introduced by `def`. If it doesn’t...
			- Throwing an exception
	- To evaluate a list, Clojure looks at the first element of the list and calls a function, macro, or special form.
	- Anyother values (including strings, numbers, and keywords) simply evaluate to themselves.
- Whenever Clojure evaluates data structures that aren’t a list or symbol, the result is the data structure itself
- Evaluates function calls and *special forms* differently

## Macros
- Macros give you a convenient way to manipulate lists before Clojure evaluates them
	- You can use Clojure to extend itself
	- Macros enable *syntactic expansion*
- Macros are a lot like functions:
	- They take arguments and return a value, just like a function would
	- They work on Clojure data structures, just like functions do
- What makes them unique and powerful is the way they fit in to the evaluation process
	- They are executed in between the reader and the evaluator—so they can manipulate the data structures that the reader spits out and transform with those data structures before passing them to the evaluator
- The process of determining the return value of a macro is called *macro expansion*
	- you can use the function `macroexpand` to see what data structure a macro returns before that data structure is evaluated
- Macros are defined with `defmacro`
```clojure
(defmacro ignore-last-operand
  [function-call]
  (butlast function-call))

(ignore-last-operand (+ 1 2 10))
; => 3

;; This will not print anything
(ignore-last-operand (+ 1 2 (println "look at me!!!")))
; => 3
```
- The `->` macro
- Often, Clojure consists of a bunch of nested function calls and that's something non-Lisp programmers are not used to
	- If you want to translate Clojure code so you can read it in a more familiar way, left-to-right, top-to-bottom manner, you can use the built-in `->` macro
		- Also known as *threading* or *stabby* macro
```clojure
;; without the macro
(defn read-resource
  "Read a resource into a string"
  [path]
  (read-string (slurp (clojure.java.io/resource path))))

;; with the macro
(defn read-resource
  [path]
  (-> path
      clojure.java.io/resource
      slurp
      read-string))
```