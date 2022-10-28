INPUT_FILE = "01_sonar_sweep.txt"

def NumberOfIncreases(data):
    with open(INPUT_FILE) as f:
        count = 0
        for i in range(1, len(data)):
            if int(data[i-1]) < int(data[i]):
                count += 1
        return (count)

with open(INPUT_FILE) as f:
    one = [int(x) for x in f.read().split()]

print(NumberOfIncreases(one))

three = []
for i in range(2, len(one)):
    three.append(one[i] + one[i-1] + one[i-2])
print(NumberOfIncreases(three))