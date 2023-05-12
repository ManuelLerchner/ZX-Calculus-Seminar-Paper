# ZX-Calculus

## What is ZX-Calculus?

+ A way of representing quantum circuits
+ Graphical language, with very simple components
+ Rules for simplifying these diagrams

## Applications

### Compilation of quantum circuits

+ Quantum circuits can be drawn with abstract gates
  + E.g. Hadamard gate, Phase gate ...

+ But actual quantum computers only have a limited set of gates, due to hardware constraints
  + E.g. CNOT, Toffoli, ...

+ ZX-Calculus can be used to compile abstract quantum circuits (Quiskit) into a sequence of elementary gates

### T-Count Optimization

+ TCount stands for the number of Troffoli gates in a circuit

+ T-Count is a metric for the complexity of a quantum circuit

+ So by reducing the T-Count, we can reduce the complexity of a circuit
  and possibly allow it to be run on a quantum computer

+ Using the simplification logic of ZX-Calculus, we can try reduce the T-Count of a circuit

## ZX-Calculus Mathematical Background

+ ZX-Calculus is based on the mathematical model of Tensornetworks and Category Theory
+ Process Diagrams
+ Processes do something to data, and wires carry information

+ Combine them using an extension of the Diraac notation

## ZX-Notation

+ Mathematical Background is cool, but since its a graphical language, its more intutive to use the visual representation

+ The ZX-Notation is very concise, it basically consist only of two elements: spiders and lines.

### Spiders

+ Spiders are nodes in the graph. They represent elements of quantum circuits, such as gates and qubits. (Both!)

+ A spider can have any number of input and output lines

+ They come in two colors: green and red
  + The color represents the Basis in which they are represented
  + Green: Z-Basis
  + Red: X-Basis

+ It is also usefull if they can store a phase angle, which allows them to represent all ??? elementary quantum gates

### Spiders represented as Linear Maps

+ Each spider has a linear map associated with it

+ The linear map is a matrix, which is determined by the number of input and output lines (doesnt need to be square!) => !Hilbert Space

+ The linear map is determined by the number of input and output lines:
  + Input lines: $n$ ??????
  + Output lines: $m$ ??????
  + Linear map: $m \times n$ ??????

$$
\begin{aligned}
\text{GreenSpider}(n,m)_\alpha &= |\underbrace{0\dots 0}_{m}\rangle \langle \underbrace{0\dots0}_{n}| &+& e^{i\alpha}|\underbrace{1\dots1}_{m}\rangle \langle \underbrace{1\dots1}_{n}|\\

\text{RedSpider}(n,m)\alpha &= |\underbrace{+ \dots +}_{m}\rangle \langle \underbrace{+ \dots +}_{n}| &+& e^{i\alpha}|\underbrace{- \dots -}_{m}\rangle \langle \underbrace{- \dots -}_{n}|
\end{aligned}
$$

### Examples of Spiders

+ **Green Copy Spider**
  + This spider is supposed to copy its "input" to both of its "outputs"
  + How exactly this works, we will see later

  + Matrix Representation

    + $\text{GreenSpider}(1,2) = |00\rangle \langle 0| + |11\rangle \langle 1| = \begin{pmatrix} 1 & 0 \\ 0 & 0 \\ 0 & 0 \\ 0 & 1 \end{pmatrix}$

  + >Note: The matrix is not square, and furthermore it is not even normalized. This means that this spider alone is not a valid quantum gate. However, it can be used as a building block for more complex gates.

+ **Identity**
  + This spider is supposed to copy its "input" to its "output". So it should do nothing

  + The color in this case is irrelevant

  + Matrix Representation

    + $\text{GreenSpider}(1,1) = |0\rangle \langle 0| + |1\rangle \langle 1| = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$

+ **Bell States**

  + It is also possible, to pruduce entangled states using spiders

  + The color also does not matter here

  + Matrix representation
  
    + $\text{GreenSpider}(0,2) = |00\rangle \langle | + |11\rangle \langle| = |00\rangle \cdot 1 + |11\rangle \cdot 1 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix}$

  + Which is the Bell State $|\Phi^+\rangle$
  
  + Notice however that it is not normalized

## Combining Spiders

+ Spiders can be combined by connecting them in such a way that the output lines of one spider are connected input lines of other spider

[TODO: Picture]

+ The result is a graph, which represents a quantum circuit
+ Notice that the relative position of the spiders does not matter, only the connections between them (their topology)

### Example: CNOT

+ The CNOT gates are key components of quantum circuits

+ They are represented by the following circuit

[TODO: Picture]

+ How to represent this as a matrix?

+ We divide up the graph, into regions, each of which contains a single spider

  1. Combine each regions next to each other using the tensor product

  2. Combine the regions on top of each other using the matrix product

  3. The result is the matrix representation of the circuit

+ The regions are:

[TODO: Picture]

+ Combining the horizontal regions:

+ $A=\text{GreenSpider}(1,1) \otimes \text{RedSpider}(2,1)$
  + $A=(|0\rangle \langle 0| + |1\rangle \langle 1|) \otimes (|\text{+}\rangle \langle \text{+ +}| + |\text{-}\rangle \langle \text{- -}|)$
  + $A=\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \otimes \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 0 & 0 &1 \\ 0 & 1 & 1 & 0 \end{pmatrix}$
  + $A=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 0 & 0 & 1 & 0 &0 &0 &0\\ 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0 \end{pmatrix}$

+ $B=\text{GreenSpider}(1,2) \otimes \text{GreenSpider}(1,1)$
  + $B=(|00\rangle \langle 0| + |11\rangle \langle 1|) \otimes (|0\rangle \langle 0| + |1\rangle \langle 1|)$
  + $B=\begin{pmatrix} 1 & 0 \\ 0 & 0 \\ 0 & 0 \\ 0 & 1 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$
  + $B=\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$

+ Combining the vertical regions:
  + $\text{CNOT} = A \cdot B = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 &0\\ 0 & 0 & 0 & 1 \\0 & 0 & 1 & 0 \\ \end{pmatrix}$

+ But calculating a circuit in this way is just as slow as simulating the circuit classically

## Simplification Rules