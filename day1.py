with open('day1.txt') as f:
    numbers = [int(i) for i in f.read().splitlines()]

#part 1
increases = sum([numbers[i] > numbers[i-1] for i in range(1, len(numbers))])
print(increases)

#part 2
increases = sum([sum(numbers[i:i+3]) > sum(numbers[i-1:i+2]) for i in range(1, len(numbers))])
print(increases)