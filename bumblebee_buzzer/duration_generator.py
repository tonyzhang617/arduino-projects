durations = []

for i in range(193):
    durations.append(82)
    
for i in range(7):
    durations.append(70)
    durations.append(12)
    
for i in range(8):
    durations.append(82)
    
for i in range(8):
    durations.append(70)
    durations.append(12)

for i in range(40):
    durations.append(82)
    
for i in range(8):
    durations.append(70)
    durations.append(12)
    
for i in range(8):
    durations.append(82)
    
for i in range(8):
    durations.append(70)
    durations.append(12)
    
for i in range(120):
    durations.append(82)
    
for i in range(26):
    durations.append(82*2)
    
for i in range(172):
    durations.append(82)
    
durations.append(82*2)

for i in range(30):
    durations.append(82)

durations.append(82*2)

for i in range(62):
    durations.append(82)
    
durations.append(82*2)

for i in range(30):
    durations.append(82)
    
durations.append(82*2)

for i in range(126):
    durations.append(126)
    
for i in range(9):
    durations.append(82*2)
    
durations.append(82*6)
    
print(', '.join(map(lambda item: str(item), durations[:511])))