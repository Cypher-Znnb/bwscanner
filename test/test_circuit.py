
from bwscanner.circuit import ExitScan, TwoHop
from test.template import TorTestCase


class TestCircuitGenerators(TorTestCase):
    def test_exit_scan(self):
        all_exits = set(self.exits)
        num_circuits = 0
        seen = set()
        for circuit in ExitScan(self.tor_state):
            assert len(circuit) == 3
            assert 'exit' in circuit[-1].flags
            seen.add(circuit[-1])
            num_circuits = num_circuits + 1
        assert all_exits == seen
        assert num_circuits == len(all_exits)


    def test_there_and_back_again(self):
        pass


def expand_circuit_generator(circuit_generator, circuits):
    """
    Update a dictionary from a circuit generator.

    The dictionary tracks which routers have been present
    in circuits together.
    """
    for circuit in circuit_generator:
        for relay in circuit:
            circuits.setdefault(relay, set(circuit)).update(circuit)
