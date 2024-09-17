Page 1:
Title: *Vũ Hữu Bình*

# Equations with Integer Solutions

Page 2:
**Symbols Used in This Book**

\[ 
\mathbb{N} = \{0; 1; 2; 3; \ldots\} \text{ is the set of natural numbers.}
\]

\[ 
\mathbb{Z} = \{\ldots; -3; -2; -1; 0; 1; 2; 3; \ldots\} \text{ is the set of integers.}
\]

\[ 
\mathbb{N}^* = \{1; 2; 3; 4; \ldots\} \text{ is the set of natural numbers excluding 0}
\]
(also called the set of positive integers).

Page 3:
## INTRODUCTION

This book introduces integer equational problems and approaches to solve integer equational problems,
which are fascinating topics of Arithmetic and Algebra. Solving integer equational problems usually requires suitable methods, as well as practical exercises to train mathematical thinking in a flexible, adaptable, and creative manner. This is why integer equational problems are often discussed in math competitions, both domestically and internationally. The book consists of four chapters:

**Chapter I** introduces several common methods to solve integer equational problems, such as divisibility tests, using contradictions, using properties of the number itself.

**Chapter II** presents integer equational problems organized by problem types.

**Chapter III** introduces problems that apply the methods for solving integer equational problems, including both theoretical and practical problems.

**Chapter IV** introduces some integer equational problems named after famous mathematicians.

The latter part of the book provides solutions for the exercises. The solutions are selected to be clear, easy to understand, logical, and as natural as possible.

Page 4:
The book is partly dedicated to listing experiences in solving math problems involving Diophantine equations, helping readers practice logical reasoning methods as well as essential qualities in study and research. There are many people who have never encountered any mathematics problems in this book throughout their lives. But those experiences in finding solutions and solving problems, such as ways to analyze mathematical problems, ways to reason to find better directions, ways to divide problems into smaller easier-to-solve problems, ways to "bring the difficult back to the easy" or "the unfamiliar to the familiar", ways to relate directions of solving problems with each other in similar situations, ways to create tools to solve a new problem, ways to select appropriate approaches for different types of problems... all of these are skills that everyone needs in life.

The author hopes that this book will bring readers many useful things and help you appreciate the beauty of mathematics through Diophantine equations and integer problems.

Vũ Hữu Bình

Page 5:
**Chapter I**

# Some Methods for Solving Diophantine Equations

## §1. Diophantine Equations

1. Introductory Problem

*A certain number of tourists come to a shop to buy vases of flowers as souvenirs. If each customer buys one vase, the shop will have one vase left. If each customer buys one vase, except for one customer who doesn’t buy any, there will be no vases left. Knowing that the number of customers is an integer, calculate the number of customers and the number of vases the shop has.*

**Solution:**

Let the number of customers be \( x \) (\( x \in \mathbb{N}^* \)).

According to the first condition, the number of vases is \( x + y \).

According to the second condition, \( x-1 \) customers buy vases, so the number of vases is \( y(x-1) \).

We obtain the equation:

\[ x + y = y(x - 1) \]

We need to solve the above equation for positive integer solutions.

**Hint 1.**

Rewrite the equation into a quadratic equation with \( y \) as the variable:

\[ y^2 + (1 - x)y + x = 0. \]

\(\Delta = x^2 - 6x + 1. \)
Since this equation must have integer solutions for \( y \), \(\Delta\) must be a perfect square:

\[ x^2 - 6x + 1 = m^2 \quad (m \in \mathbb{N}) \]
\[
(x - 3 + m)(x - 3 - m) = 8.
\]

Page 6:
Given \( x - 3 + m \) and \( x - 3 - m \), they sum to \( 8 \), in which \( x - 3 + m \ge x - 3 - m \). The cases are as follows:

\[
\begin{array}{|c|c|c|}
\hline
x - 3 + m & 8 & 4 \\
\hline
x - 3 - m & 1 & 2 \\
\hline
m & 3.5 & 1 \\
\hline
x & \text{not applicable} & 6 \\
\hline
\end{array}
\]

Given \( x = 6 \), it follows that \( y = 2 \) or \( y = 3 \). Because \( y \) must be an integer (according to the problem statement), \( y = 2 \).

Answer: There are \( 6 \) customers, and there are \( 8 \) flowers.

\textbf{Solution 2:} We have \( x + y = y(x - y) \Rightarrow xy - y^2 = x - y = 0 \)

\[
\Rightarrow xy - x - y^2 + y = 2 \\
\Rightarrow x(y - 1) - y(y - 1) = 2 \\
\Rightarrow (y - 1)(x - y - 2) = 2
\]

Since \( y - 1 \) is odd, \( y - 1 \) must be \( \pm 1 \). Therefore,

\[
\begin{cases}
y - 1 = 1 \\
x - y - 2 = 2
\end{cases}
\Rightarrow 
\begin{cases}
y = 2 \\
x = 6
\end{cases}
\]

Answer: There are \( 6 \) customers, and there are \( 8 \) flowers.

Page 7:
\( \text{- 46 -} \)

### 2. Solving Integer Solution Equations

Solving the integer solution equations involving \(x, y, z, \ldots\) is finding all sets of integer \((x_0, y_0, z_0, \ldots)\) that satisfy the equation.

When solving for integer solutions, we need to utilize the properties of the set \( \mathbb{Z} \). Besides logical transformations, we often use transformations such that the variable values only need to satisfy the necessary (but not sufficient) conditions of the solution. In such cases, we must check these values by substituting them back into the given equation.

An equation with integer solutions may either have no solutions or have solutions. When examining equations characterized by integer solutions, these solutions are generally derived from expressions containing only integers.

\[ \S 2. \text{METHOD OF DIVISIBILITY ANALYSIS} \]

1. \[\text{Represent one variable in terms of the others, revealing divisibility relationships.}\]

Example 1. Draw the wishbone diagram.

\[ \text{Example 2. Finding integers where the product of two sums equals the sum of two products.} \]

\[ Kinh \text{ two integers...}\]

 \[ A. \left(\text{Expression}\right)\] 

 \[ \text{Bachet's Problem} \text{of Diophantus}\]

---

(Note: The example in the original image seems either incomplete or specific to a broader context within the document which isn't entirely visible. Hence, providing a clear explicit translation without more context for example 2 could be misleading.)

