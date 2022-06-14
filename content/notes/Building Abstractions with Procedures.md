---
date: 2022-05-30
---
## The paradigm
- > Since large programs grow from small ones, it is crucial that we develop an arsenal of standard program structures of whose correctness we have become sure—we call them idioms—and learn to combine them into larger structures using organizational techniques of proven value.
- A computer language is a novel formal medium for expressing ideas about methodology
	- => Programs must be written for people to read, and only incidentally for machines to execute
	- CS describes the structure of knowedge from an imperative point of view (*how to*), as opposed to the more declarative point of view taken by mathematical subjects (*what is*)
- Lisp is most significant by its ability to manipulate descripions of processes as othe Lisp data
	- Lisp blurs the traditional distinction between passive and active data

## Elements of Programming
- When we describe a language, it is crucial to pay attention to the means that the language provides for combining simple ideas to form more complex ideas
	- Every powerful language has 3 mechanisms for accomplishing this:
		- **Primitive expressions**
			- The simplest entities the language is concerned with
		- **Means of combination**
			- By which compound elements are built from simpler ones
		- **Means of abstraction**
			- By which compound elements can be named and manipulated as units
- REPL
	- = *read-eval-print loop*
	- The mode interpreters run in, it reads the expression, evaluates it and prints the result
### Evaluation
- Combination evaluation
	- 1. Evaluate the subexpressions of the combination
	- 2. Apply the procedure, that is the value of the leftmost subexpression (the operator), to the arguments that are the values of the subexpressions (the operands)
	- Exceptions to this rule are called *special forms*
- Two ways to evaluate
	- Normal-order evaluation
		- That is: fully expand and then reduce
	- Applicative-order evaluation
		- Basically what is described above applied at scale
### Procedures as black-box abstractions
- Each procedure should accomplish an identifiable task that can be used as a module in defining other procedures
- The principle that meaning of a procedure should be independent to the parameter names used by its author seems self-evident, but its consequences are profound
	- The simplest: The parameter names of a procedure must be local to the body of the procedure
	- When it doesn't matter what name the variable has (such as in the case of formal parameters), we call such name a *bound variable*
		- We say the procedure binds its formal parameters
		- If a variable is not bound, we say it's *free*
- Internal definitions and block structure
	- The set of expressions for which a binding defines a name is called the *scope* of that name
	- To simplify and auxiliarize our code, we employ block structure
		- As any other data, we can bind procedures to procedures too
		- This discipline is called *lexical scoping*

## Procedures and the Processes They Generate
- Procedure is a patter for the local evolution of a computational process
	- It specifies how each stage of the process is built upon the previous stage

### Linear Recursion and Iteration
- Example (two ways to compute a factorial):
	- 1. 
		- ![[Pasted image 20220531092143.webp]]
		- The amount of information needed to keep track of the process grows linearly
		- This is an example of *linear recursive process*
			- Time complexity: O(x), space complexity: O(x)
	- 2.
		- ![[Pasted image 20220531092605.webp]]
		- The number of steps required to get the result grows linearly
		- This is an example of *linear iterative process*
			- Time complexity: O(x), space complexity: O(1)
- We need to differentiate between recursive procedures and processes 
	- Most implementations of common languages are designed in such a way that the interpretation of any recursive procedure consumes an amount of memory that grows with the number of procedure calls, even though the process is in principle iterative, thus they have to resor to special-purpose "looping constructs"
- ![[Pasted image 20220531145605.webp]]
	- Every node in the tree has to be examined (thus the same subtrees have to be evaluated more times)
		- This process grows exponentially
			- It has a time complexity of O(fib(n)) (space complexity: O(n))
		- That's why it's inefficent to use this processes on numbers
			- But they can be useful when working with hiearachically structured data

## Formulating Abstractions with Higher-Order Procedures
- Procedures that manipulate procedures are called higher-order procedure
- Useful abstractions when we have procedures that share an underlying pattern