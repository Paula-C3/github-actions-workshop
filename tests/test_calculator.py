from app.calculator import sum, subtract

def test_sum() -> None:
    assert sum(2, 3) == 5


# Introducir un fallo premeditado
def test_subtract() -> None:
    assert subtract(5, 3) == 1
