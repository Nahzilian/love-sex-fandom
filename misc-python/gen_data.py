import json

data = []
t = [
    ["Eventually", "Tame Impala"],
    ["18", "One Direction"],
    ["I heard you’re married", "The Weeknd (ft. Lil Wayne)"],
    ["hornyloveskickmess", "Girl in Red"],
    ["Christmas Tree", "V"],
    ["Story of my life", "One Direction"],
    ["Always a dream", "Dafna"],
    ["Avoid Things", "Tems"],
    ["Human", "Dodie and Tom Walker"],
    ["Polaroid Love", "ENHYPEN"],
    ["Sex money feelings die", "Lykke Li"],
]

counter = 0
for i in range(8, 19):
    d_piece = {
        "file": "new Audio('./assets/songs/track{count}.mp3')".format(count=i),
        "cover": "./assets/songs/cover{count}.jpeg".format(count=i),
        "name": t[counter][0],
        "artist": t[counter][1]
    }
    data.append(d_piece)
    counter += 1

json_string = json.dumps(data)
with open("temp.json", 'w') as f:
    f.write(json_string)


