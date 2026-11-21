from math import gcd

def analyze(data):
    people, step, days = data["participants"], data["step"], data["days"]
    size = len(people)
    if not 1 <= size <= 100 or len(set(people)) != size or not isinstance(step,int) or step < 1 or gcd(step,size) != 1:
        raise ValueError("Use unique participants and a positive step coprime to the group size")
    if not isinstance(days,int) or not 1 <= days <= size:
        raise ValueError("Days must fit within one complete rotation")
    schedule = [[people[(seat-day*step)%size] for seat in range(size)] for day in range(days)]
    return {"schedule":schedule}

if __name__ == "__main__":
    import json
    from pathlib import Path
    import sys
    try:
        path, = sys.argv[1:]
        result = analyze(json.loads(Path(path).read_text(encoding="utf-8")))
        print(json.dumps(result, ensure_ascii=True, allow_nan=False))
    except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError) as error:
        print(f"Invalid input: {error}", file=sys.stderr)
        sys.exit(2)
