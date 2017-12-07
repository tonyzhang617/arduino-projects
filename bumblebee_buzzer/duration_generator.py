durations = []

for i in range(193):
    durations.append(16)

for i in range(7):
    durations.append(20)
    durations.append(80)

for i in range(8):
    durations.append(16)

for i in range(8):
    durations.append(20)
    durations.append(80)

for i in range(40):
    durations.append(16)

for i in range(8):
    durations.append(20)
    durations.append(80)

for i in range(8):
    durations.append(16)

for i in range(8):
    durations.append(20)
    durations.append(80)

for i in range(120):
    durations.append(16)

for i in range(26):
    durations.append(8)

for i in range(172):
    durations.append(16)

durations.append(8)

for i in range(30):
    durations.append(16)

durations.append(8)

for i in range(62):
    durations.append(16)

durations.append(8)

for i in range(30):
    durations.append(16)

durations.append(8)

for i in range(126):
    durations.append(16)

for i in range(9):
    durations.append(8)

durations.append(8)

print(', '.join(map(lambda item: str(item), durations)))
