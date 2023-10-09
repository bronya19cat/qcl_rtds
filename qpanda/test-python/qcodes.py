from script import *
from pyqpanda import *
from pyqpanda.utils import *

def entg(q,c):
    circuit = CreateEmptyCircuit()
    controlVector = QVec()
    controlVector.append(q[0])
    controlVector.append(q[1])
    circuit.insert(H(q[0]))
    circuit.insert(CNOT(q[0], q[1]))
    return circuit