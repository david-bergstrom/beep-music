import sys
import re
from pprint import pprint

speed = 2

def generate_midi_table():
    a = 440
    midi = []
    for i in range(127):
        midi.append((a/32.0) * (2 ** ((i - 9.0) / 12)))
    return midi

re_on = re.compile(".*Note_on_c.*")
re_off = re.compile(".*Note_off_c.*")

table = generate_midi_table()

notes = []
current = {}

for line in sys.stdin:
    if re_on.match(line):
        split = line.split(', ')
        if split[3] == '1':
            if 'start' in current:
                current['sleep'] = (int(split[1]) - current['start']) / 1000.0
            else:
                current['sleep'] = 0
            current['start'] = int(split[1])
            current['frequency'] = table[int(split[4])]
    elif re_off.match(line):
        split = line.split(', ')
        if split[3] == '1':
            current['stop'] = int(split[1])
            current['duration'] = (current['stop'] - current['start'])
            notes.append(current.copy())

for note in notes:
    print note['frequency'], ',', speed * note['sleep'] , ',' , 2 * speed * note['duration']
