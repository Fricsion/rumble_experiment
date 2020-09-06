# -*- coding: utf-8 -*-
from pydub import AudioSegment
import matplotlib.pyplot as plt

sound = AudioSegment.from_file("input.wav", "wav")

list_sound = sound.get_array_of_samples()

print(len(list_sound))

plt.plot(list_sound)
plt.grid()
plt.show()
