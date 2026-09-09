import sys
import json
from client import EchoStateNetwork

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "process":
        esn = EchoStateNetwork(params.get("size", 10))
        return esn.process_sequence(params.get("sequence", [0.5, 0.8, -0.2]))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
