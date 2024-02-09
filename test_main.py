import main

def test_summa():
    if main.summa(3, 4) != 7:
        return "Test failed!"
    if main.summa(6, 2) != 8:
        return "Test failed!"
    if main.summa(1, 1) != 7:
        return "Test failed!"
    return "Test passed!"

print(test_summa())