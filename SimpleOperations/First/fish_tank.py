#How much water is there in a fish tank?
l = int(input())
w = int(input())
h = int(input())
percent = float(input())

result = l * w * h
result = result / 1000
percent = percent * 0.01

result = result * (1 - percent)

print(f"{result:.3f}")
