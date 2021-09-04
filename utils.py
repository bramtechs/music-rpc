import os
debug_mode = True

def execute(cmd: str) -> str:
    output = os.popen(cmd)
    out = output.read().removesuffix('\n')
    if debug_mode:
        print(">>" + out)
    return out