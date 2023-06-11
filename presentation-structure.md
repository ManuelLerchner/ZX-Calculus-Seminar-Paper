# ZX-Calculus

## What is ZX-Calculus?

+ A way of representing quantum circuits
+ Graphical language, with very simple components
+ Rules for simplifying these diagrams

## Applications

### Quantum Circuit Optimization

+ Circuits are transformed into new circuits, which are equivalent
  + involving fewer gates
  + consisting of simpler gates [https://quantum-journal.org/papers/q-2020-06-04-279/pdf/]

+ Advantages of ZX vs classical identities <https://www.youtube.com/watch?v=JafI_LZts2g>

### Compilation of quantum circuits

+ Quantum circuits can be drawn with abstract gates
  + E.g. Hadamard gate, Phase gate ...

+ But actual quantum computers only have a limited set of gates, due to hardware constraints
  + E.g. CNOT, Toffoli, ...

+ ZX-Calculus can be used to compile abstract quantum circuits (Quiskit) into a sequence of elementary gates

+ Which Metrics to use for optimization?

  + T-Count
  + #Gates
  + #Cnot

### T-Count Optimization

+ TCount stands for the number of Troffoli gates in a circuit

+ T-Count is a metric for the complexity of a quantum circuit

+ So by reducing the T-Count, we can reduce the complexity of a circuit
  and possibly allow it to be run on a quantum computer

+ Using the simplification logic of ZX-Calculus, we can try reduce the T-Count of a circuit

#### Example: T-Count Optimization

+ <https://www.youtube.com/watch?v=lKHiV-Cyb-w> 35:00
  + Only use Clifford-T set gates

+ Trofoli gates

## ZX-Calculus Mathematical Background

+ ZX-Calculus is based on the mathematical model of Tensornetworks and Category Theory
+ Process Diagrams
+ Processes do something to data, and wires carry information

+ Combine them using an extension of the Diraac notation

+ Frobinius Algebras
  + [Math](https://www.cs.ox.ac.uk/people/bob.coecke/GreenRed.pdf)

### Process Theory

+ Everything in the world is a Process
+ A Process is a black box, which takes some input A and transforms it into some output B
+ Processes can happen successively, $\circ$, or in parallel, $\otimes$
  + Also ist auch eine zeitliche komponente dabei

+ Only topologies matter, not the specific position of the processes and wires

+ <https://www.youtube.com/watch?v=UQTTJV0ejfw>

+ sliding around, tensors and compositions

+ If it looks like the same graph its the same thing

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
  + (this isn't a problem, it just means ZX can describe non-unitary matrices.)

+ The linear map is determined by the number of input and output lines:
  + Input lines: $n$ ??????
  + Output lines: $m$ ??????
  + Linear map: $m \times n$ ??????

$$
\begin{aligned}
\text{GreenSpider}(n,m)_\alpha &= |\underbrace{0\dots 0}_{m}\rangle \langle \underbrace{0\dots0}_{n}| &+& e^{i\alpha}|\underbrace{1\dots1}_{m}\rangle \langle \underbrace{1\dots1}_{n}|\\
&= |0\rangle^{\otimes m} \langle 0|^{\otimes n} &+& e^{i\alpha}|1\rangle^{\otimes m} \langle 1|^{\otimes n}
\\

\text{RedSpider}(n,m)\alpha &= |\underbrace{+ \dots +}_{m}\rangle \langle \underbrace{+ \dots +}_{n}| &+& e^{i\alpha}|\underbrace{- \dots -}_{m}\rangle \langle \underbrace{- \dots -}_{n}|\\
&= |+\rangle^{\otimes m} \langle +|^{\otimes n} &+& e^{i\alpha}|-\rangle^{\otimes m} \langle -|^{\otimes n}
\end{aligned}
$$

### Examples of Spiders

+ **Basis States**
  + A simple spider with zero input lines and one output can be thought of a basis state
  + The color of the spider determines the basis
  
  + Matrix representation
    + $\text{GreenSpider}(0,1) = |0\rangle \cdot 1 + |1\rangle \cdot 1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \propto |+\rangle$
    + $\text{GreenSpider}(0,1,\pi) = |0\rangle \cdot 1 + |1\rangle \cdot e^{i\pi} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \propto |-\rangle$
    + $\text{RedSpider}(0,1) = |+\rangle \cdot 1 + |-\rangle \cdot 1 = \begin{pmatrix} 2 \\ 0 \end{pmatrix} \propto |0\rangle$
    + $\text{RedSpider}(0,1,\pi) = |+\rangle \cdot 1 + |-\rangle \cdot e^{i\pi} = \begin{pmatrix} 0 \\ 2 \end{pmatrix} \propto |1\rangle$

+ **Pauli Matrices**
  + The Pauli Matrices can also be represented as spiders
  + Matrix representation

    + $\text{GreenSpider}(1,1,\pi) = |0\rangle \langle 0| + e^{i\pi}|1\rangle \langle 1| = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = Z$
    + $\text{RedSpider}(1,1,\pi) = |+\rangle \langle +| + e^{i\pi}|-\rangle \langle -| = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = X$

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

## Transforming Quantum Circuits into ZX-Graphs

+ Since classical Quantum Circuits are a subset of ZX-Diagrams, it is possible to construct ZX-Diagrams which are not valid Quantum Circuits
+ But this is no problem, aslong as we can transform the Diagram back into a valid Quantum Circuit
+ [Image Schematically](https://quantum-journal.org/papers/q-2020-06-04-279/pdf/)

### Example: CNOT

+ The CNOT gates are key components of quantum circuits

+ They are represented by the following circuit

[TODO: Picture]

+ We can transform any quantum circuit into a ZX-Graph
+ Each gate is represented by a Circuit in the ZX-Graph
  + Table. !TODO

+ How to represent this as a matrix?

#### Breaking down a diagram into generators

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

### Showing that only topology matters

+ Different ways of dividing up the graph into regions can lead to different matrices

+ ![Image](TODO)

+ However, the matrices are equivalent up to a factor

### Example applying CNOT to two qubits

+ We can now apply the CNOT gate to two qubits
+ ![Image](TODO)

+ But calculating a circuit in this way is just as slow as simulating the circuit classically

## Simplification Rules

### Spider-fusion

+ If two spiders of the **same color** are connected to each other, they can be fused into a single spider. If they have phases, the phases are simply added together

+ ![Image](TODO)

+ We now see that it is not needed to keep track of input and outputs of the spiders, since we can freely exchange them using this rule
  + Only topology matters

### Hopf Rule

+ If two spiders of **different color** are connected to each other with two lines, the connecting wires can be removed

+ ![Image](TODO)

### Bi-Algebra Rule

+ ??

### Copy Rules

+ ![Image](TODO)
+ ![Image](TODO)

+ WE say green copyies red, and red copies green

### Color Change Rule

+ We can change the color of a spider, by adding a Hadamard spider to all its inputs and outputs

+ ![Image](TODO)

#### Hadamard

+ In order to use the color change rule, we need to introduce a new spider, the Hadamard spider
+ Using the euler angle representation of the Hadamard gate, we can derive the following graph
+ ![Image](TODO)

## Example Circuit simplification

### Swap using 3 CNOTs

### Erzeugung von Bell States

### Quantum Teleportation

### BB84jj

### Quantum Fourier Transform

### Completness

+ ZX-Calculus is complete, meaning that any two ZX-Graphs that represent the same quantum circuit can be transformed into each other using the rules of the ZX-Calculus
  + But the path, between the two graphs, can traverse Graphs which dont represent valid quantum circuits

### Python ZX Library

+ Example
+ Metrics

## Todo

+ Phase Gadgets
+ From ZX to Circuit
