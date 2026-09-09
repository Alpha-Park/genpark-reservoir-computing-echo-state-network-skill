from client import EchoStateNetwork

def main():
    print("=== Reservoir Computing Echo State Network ===")
    esn = EchoStateNetwork(reservoir_size=16, leak_rate=0.3)
    inputs = [math.sin(i * 0.2) for i in range(25)]

    res = esn.process_sequence(inputs)
    print("Reservoir output summary:", res["reservoir_size"], "units,", res["input_steps"], "steps.")
    print("Final state norm:", res["final_state_norm"])
    assert res["final_state_norm"] > 0.05

    print("Echo State Network verified successfully!")

if __name__ == "__main__":
    main()
