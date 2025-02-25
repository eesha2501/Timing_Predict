import argparse

def check_violation(logic_depth, clock_period_ns, gate_delay_ns=0.1):
    total_delay = logic_depth * gate_delay_ns
    return total_delay > clock_period_ns

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--logic_depth", type=float, required=True)
    parser.add_argument("--clock_period", type=float, required=True)
    args = parser.parse_args()
    
    violation = check_violation(args.logic_depth, args.clock_period)
    print(f"Timing Violation: {violation}")