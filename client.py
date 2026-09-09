import math
import random

class EchoStateNetwork:
    """Reservoir Computing Echo State Network (ESN) in pure Python."""
    def __init__(self, reservoir_size: int = 10, leak_rate: float = 0.3, seed: int = 42):
        self.size = reservoir_size
        self.leak_rate = leak_rate
        random.seed(seed)

        # Initialize fixed recurrent weights with spectral radius < 1
        self.W_res = [[(random.random() - 0.5) * 0.4 for _ in range(reservoir_size)] for _ in range(reservoir_size)]
        self.W_in = [(random.random() - 0.5) * 0.8 for _ in range(reservoir_size)]
        self.state = [0.0] * reservoir_size

    def step(self, u: float) -> list[float]:
        new_state = [0.0] * self.size
        for i in range(self.size):
            res_sum = sum(self.W_res[i][j] * self.state[j] for j in range(self.size))
            pre_activation = res_sum + self.W_in[i] * u
            # Leaky integration
            new_state[i] = (1.0 - self.leak_rate) * self.state[i] + self.leak_rate * math.tanh(pre_activation)
        self.state = new_state
        return list(self.state)

    def process_sequence(self, sequence: list[float]) -> dict:
        trajectory = []
        for val in sequence:
            s = self.step(val)
            trajectory.append([round(x, 4) for x in s[:4]])
        return {
            "reservoir_size": self.size,
            "input_steps": len(sequence),
            "final_state_norm": round(math.sqrt(sum(x**2 for x in self.state)), 4),
            "sample_state_trajectory": trajectory[:5]
        }
