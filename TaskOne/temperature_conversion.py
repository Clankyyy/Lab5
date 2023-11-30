COEFFICIENT: float = 9.0/5
OFFSET = 32


def celToFahr(cellDegrees: float) -> float:
    return (cellDegrees * COEFFICIENT) + OFFSET

def fahrToCell(fahrDegrees: float) -> float:
    return (fahrDegrees - OFFSET) * COEFFICIENT