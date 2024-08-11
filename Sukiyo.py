import time
from threading import Thread, Lock
import sys

lock = Lock()

# print text character by character with a delay
def animated_text(text, delay=0.1):
    with lock:  # Ensure only one thread prints at a time
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

# sing a lyric with a delay before starting and a specific speed for printing
def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animated_text(lyric, speed)

# create threads for singing the lyrics
def sing_song():
    lyrics = [
        ("beli ciki beli koyo", 0.05),
        ("suki yo", 0.1),
        ("ima anata ni omoi nosete", 0.15),
        ("hora sunao ni naru no watashi", 0.15),
        ("kono saki motto soba ni ite mo ii ka na?", 0.14),
        ("koi to koi ga kasanatte", 0.15),
        ("suki yo", 0.1),
        ("ima anata ni omoi todoke", 0.16),
        ("nee kizuite kuremasen ka?", 0.18),
        ("dou shiyou mo nai kurai", 0.18),
        ("kokoro made suki ni natte yukuuUUuuUuu", 0.15)
    ]

    delays = [0.1, 3.7, 5, 9, 13.5, 16, 19.3, 22.6, 24, 27.8, 32.6, 36.3 ]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

sing_song()
