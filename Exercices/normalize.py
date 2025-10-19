def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')
      
def normalize2(numbers2):
    max_number = max(numbers2)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers2)):
        numbers2[i]  /= float(max_number)
        assert(0.0 <= numbers2[i] <= 1.0), "output not between 0 and 1"
    return numbers2