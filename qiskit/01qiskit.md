
```
pip install qiskit
pip install qiskit[visualization]
```

基本指令
1. circuit
```
from qiskit import QuantumCircuit
QuantumCircuit(2, 2)
h(0)
cx(0, 1)
measure([0,1], [0,1])
```
2. simulator
```
from qiskit import Aer
Aer.get_backend('qasm_simulator')
```
3. IBMQ
```
from qiskit import IBMQ
IBMQ.save_account('token')
IBMQ.load_account()
```
4. provider
```
IBMQ.get_provider('ibm-q')
```
5. backend
```
provider.get_backend('ibmq_lima')
```
6. job
```
execute(circuit,backend=simul,shots=1000)
from qiskit.tools.monitor import job_monitor
job_monitor(job2)
```
7. result
```
job1.result()
```
8. count
```
result1.get_counts()
```
9. plot
```
from qiskit.visualization import plot_histogram
plot_histogram(result1.get_counts())
```
