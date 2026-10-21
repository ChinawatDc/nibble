from .rules import THRESHOLD_THB, RATE


def apply_discount(total):
    """Orders of THRESHOLD_THB or more get RATE off."""
    if total > THRESHOLD_THB:
        return round(total * (1 - RATE), 2)
    return total
