from pydub import AudioSegment
from pydub.playback import play
import threading
# Import an audio file
# Format parameter only
# for readability


duration = 0.25*1000


def play_note(name):
    wav_file = AudioSegment.from_wav(file=f"assets\\notes\\{name}.wav")
    slice = wav_file[:duration]
    play(slice)


def play_note_with_interactive_output(name):
    print(name)
    wav_file = AudioSegment.from_wav(file=f"assets\\notes\\{name}.wav")
    slice = wav_file[:duration]
    play(slice)
