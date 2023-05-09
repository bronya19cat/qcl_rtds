from pyqpanda import *

if __name__=="__main__":
    qvm = NoiseQVM()
    qvm.init_qvm()
    qvm.set_noise_model(NoiseModel.DEPOLARIZING_KRAUS_OPERATOR, GateType.CZ_GATE, 0.005)

    #qvm = QCloud()
    #qvm.init_qvm("898D47CF515A48CEAA9F2326394B85C6")

    qubit_lists = [[3,4], [2,3,5]]

    ntrials = 100

    shots = 2000
    qv_result = calculate_quantum_volume(qvm, qubit_lists, ntrials, shots)
    print("Quantum Volume : ", qv_result)
    qvm.finalize()
