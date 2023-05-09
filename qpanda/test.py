from pyqpanda import *

init(QMachineType.CPU)
prog = QProg()
q = qAlloc_many(2)
c = cAlloc_many(2)
prog.insert(H(q[0]))
prog.insert(CNOT(q[0],q[1]))
prog.insert(measure_all(q,c))
result = run_with_configuration(prog, cbit_list = c, shots = 1000)
print(result)
finalize()

