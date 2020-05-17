def fizzbuzz():
    start = 1
    end = 100
    jump = 1
    numbers = [15, 5, 3]
    while start <= end:
        if start % numbers[0] == 0:
            print('FizzBuzz')
        elif start % numbers[1] == 0:
            print('Buzz')
        elif start % numbers[2] == 0:
            print('Fizz')
        else:
            print(start)
        start += jump
fizzbuzz()
