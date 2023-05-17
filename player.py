from pydub import AudioSegment
from pydub.playback import play
import threading
# Import an audio file
# Format parameter only
# for readability


duration = 0.25*1000


def play_note(name, note_list):
    wav_file = AudioSegment.from_wav(file=f"assets\\notes\\{name}.wav")
    slice = wav_file[:duration]
    note_list.append(slice)
    return note_list


def play_note_with_interactive_output(name):
    print(name)
    wav_file = AudioSegment.from_wav(file=f"assets\\notes\\{name}.wav")
    slice = wav_file[:duration]
    play(slice)


def create_song(input_list):
    note_list = []
    for i in input_list:
        play_note(i, note_list)
    song = sum(note_list)
    return song


def save_song_wav(song, filename):
    song.export(filename, format="wav")
