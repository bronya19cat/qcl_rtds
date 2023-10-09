from qcodes import *
from pyqpanda import *
from pyqpanda.utils import *
if __name__ == '__main__':
    machine = init(QMachineType.CPU)
    qv = machine.qAlloc_many(2)
    cv = machine.cAlloc_many(2)
    prog = QProg()
    prog.insert(entg(qv,qc))
    result = run_with_configuration(prog, cbit_list = cv, shots = 1000)
    print(result)

    finalize()
