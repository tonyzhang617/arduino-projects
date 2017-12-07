song_freqs = []
std_freqs = []

with open('song_notes', 'r') as file_freqs:
    for line in file_freqs:
        if line.strip() == '_':
            continue
        freq = int(line.strip())
        song_freqs.append(freq)
    file_freqs.close()
    
with open('standard_freqs', 'r') as f:
    for line in f:
        freq = int(line.strip())
        std_freqs.append(freq)
    f.close()
    
def to_std(freq, stds):
    for s in stds:
        if abs(freq - s) <= 1:
            return s
    return None
    
new_song = []
for i in song_freqs:
    if i == 0:
        new_song.append(0)
        continue
    new_song.append(to_std(i, std_freqs))

with open('new_song_notes', 'w') as f:
    for freq in new_song:
        f.write("%d\n" % freq)
    f.truncate()
    f.close()