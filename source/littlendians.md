### Little endians

CNOT 门的矩阵形式为：

$$
CNOT =
\left[
\begin{matrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0\\
\end{matrix}
\right]
$$

在 qiskit 中有 `UnitaryGate` 工具可以将矩阵转化为量子门，如：
```python
from qiskit import QuantumCircuit
from qiskit.extensions import UnitaryGate

matrix1 = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 1, 0]]
gatecx = UnitaryGate(matrix1)

circuit = QuantumCircuit(2,2)
circuit.x(0)
circuit.append(gatecx,[0,1])
circuit.draw('mpl',scale=0.6)
```

上述代码的结果应该是（1，1），然而结果出乎意料：

`插入图片`

---
原因是在 qiskit 中，qubit 编码方式为 “Little endians”，叫做 “小端编码”，或者 “末端编码”。即，倒序 $\ket{q1q0}$。

因此，在做计算时矩阵也是倒序作用$B \otimes A$，表示A和B分别作用在 $q0$ 和 $q1$ 上。据此分析，构造 CNOT 的思路应该是：

$$
CNOT = I \otimes P_0 + X \otimes P_1
$$

在这里，

$$
P_0 = \left[\begin{matrix}
1&0\\
0&0\\
\end{matrix}\right],
P_1 = \left[\begin{matrix}
0&0\\
0&1\\
\end{matrix}\right]
$$

所以在qiskit中，构造CNOT门应该使用的矩阵是：

$$
CNOT = \left[\begin{matrix}
1&0&0&0\\
0&0&0&1\\
0&0&1&0\\
0&1&0&0\\
\end{matrix}\right]
$$

