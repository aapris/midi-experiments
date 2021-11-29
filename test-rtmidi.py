"""
Play a few sounds to test is fluidsynth working.
"""
import time

import rtmidi

from rtmidi.midiconstants import (
    ALL_SOUND_OFF, BANK_SELECT_LSB,
    BANK_SELECT_MSB, CHANNEL_VOLUME,
    CONTROL_CHANGE, NOTE_ON, NOTE_OFF, PROGRAM_CHANGE
)


def usage():
    print("""Install fluidsynth and run it!
    brew install fluid-synth
    fluidsynth -o midi.driver=coremidi -o audio.driver=coreaudio -o audio.coreaudio.device=default -o audio.period-size=256 FluidR3_GM.sf2
    """)


midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print("Available ports:\n - {}".format("\n - ".join(available_ports)))

if available_ports:
    print("Opening '{}'".format(available_ports[0]))
    midiout.open_port(0)
else:
    usage()
    midiout.open_virtual_port("My virtual output")

try:
    for i in range(0, 15):
        channel = i

        note_on = [NOTE_ON | channel, 60, 112]  # channel 1, middle C, velocity 112
        note_on1 = [NOTE_ON | channel, 64, 112]  # channel 1, middle E, velocity 112
        note_on2 = [NOTE_ON | channel, 67, 112]  # channel 1, middle G, velocity 112

        note_off = [NOTE_OFF | channel, 60, 0]
        note_off1 = [NOTE_OFF | channel, 64, 0]
        note_off2 = [NOTE_OFF | channel, 67, 0]

        midiout.send_message(note_on)
        time.sleep(1.5)
        midiout.send_message(note_off)
        midiout.send_message(note_on)
        midiout.send_message(note_on1)
        midiout.send_message(note_on2)
        time.sleep(1.5)
        midiout.send_message(note_off)
        midiout.send_message(note_off1)
        midiout.send_message(note_off2)
except KeyboardInterrupt:
    del midiout
finally:
    del midiout
