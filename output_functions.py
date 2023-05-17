import player

# print with new line


def pretty_print_list(input_list):
    for i in input_list:
        print(i)


def create_list_string(input_list):
    return '\n'.join(input_list)


def output_0(inputlist):
    pretty_print_list(inputlist)


def output_1(inputlist):
    str = create_list_string(inputlist)
    with open("output_text.txt", "w") as f:
        f.write(str)


def output_2(inputlist):
    for i in inputlist:
        player.play_note_with_interactive_output(i)


def output_3(inputlist):
    player.save_song_wav(player.create_song(inputlist), "output_audio.wav")


def output_4(inputlist):
    output_1(inputlist)
    output_3(inputlist)


def output_5(inputlist):
    pretty_print_list(inputlist)
    output_3(inputlist)
