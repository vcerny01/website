## Namespaces
- [[Clojure]] uses *namespaces* to organize code
	- Namespaces contain maps between human friendly symbolds and references to *vars*
	- Technically, namespaces are objects of type `clojure.lang.Namespace` and you can interact with them just like you can do with other Clojure data structures
		- e.g. you can refer to current namespace with `*ns*` and you can get its name with `(ns-name *ns*)`
	- Symbols
		- When you use a symbol (e.g. `map`), Clojure finds the corresponding var in the current namespace and retrieves the object
		- Quoting a form tells Clojure not to evelaute  it byt to treat it as a data
```clojure
inc
; => #<core$inc clojure.core$inc@30132014>
'inc
; => inc
```
## Defining
- When we use `def` to define a variable, the process is called *interning* a var
	- You can interact with interned vars
```clojure
(ns-interns *ns*)
; => {great-books #'user/great-books}
(get (ns-interns *ns*) 'great-books)
; => #'user/great-books
```
- Vars can use `deref` to get the objects vars point to
 ```clojure
(deref #'user/great-books)
; => ["East of Eden" "The Glass Bead Game"]
```
## Creating and switching to namespaces
- Namespaces can be created with `create-ns`
	- But this function is not really used as it's not very useful to create a namespace and not move into it
```clojure
user=> (create-ns 'cheese.taxonomy)
; => #<Namespace cheese.taxonomy>
```
- You can create and switch to namespace with `in-ns`
## Using data from other namespaces
- If you want to use functions and data from other namespaces using a *fully qualified* symbol
	- The general form is *namespace/name*
	- Calling `refer` with a namespace symbol lets you refer to the corresponding namespace’s objects without having to use fully qualified symbols
		- It does this by updating the current namespace’s symbol/object map
		- When you call refer, you can also pass it the filters `:only`, `:exclude`, and `:rename`
	- Calling `alias` lets you shorten a namespace name for using fully qualified symbols
```clojure
(clojure.core/alias 'taxonomy 'cheese.taxonomy)
```
## File paths and namespace names
- You can import namespaces with functions `require` and `use` (and you can utilize `alias` for example)
```clojure
(require 'the-divine-cheese-code.visualization.svg)
(alias 'svg 'the-divine-cheese-code.visualization.svg)

(use '[the-divine-cheese-code.visualization.svg :as svg])
(= svg/points points)
; => true
```
### The `ns` macro
- One `ns` call can incorporate `require`, `use`, `in-ns`, `alias` and `refer`
- `ns` refers `clojure-core` by default
- There are six possible references within  `ns`: `(:refere-clojure)`, `(:require)`, `(:use)`, `(:import)`, `(:load)`, `(:gen-class)`