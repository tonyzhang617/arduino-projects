notes_to_chars = { 0: ' ' }

with open('standard_freqs', 'r') as f:
    c = '!'
    for line in f:
        notes_to_chars[int(line.strip())] = c
        c = chr(ord(c)+1)

for k in sorted(notes_to_chars.keys()):
    print "%s: %s || " % (k, notes_to_chars[k]),

compressed = []

with open('new_song_notes', 'r') as f:
    for line in f:
        freq = int(line.strip())
        compressed.append(notes_to_chars[freq])

print ''.join(compressed)
