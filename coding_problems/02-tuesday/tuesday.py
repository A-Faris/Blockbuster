"""Tuesday coding problem"""


def multi_table(number: int) -> str:
    """Solution"""
    return "\n".join([f"{i} * {number} = {i*number}" for i in range(1, 11)])
