# Midi experiments

Various experiments how to transform data to music or at least sounds.

# Gettings started

Create virtualenv and install python modules:

`pip install -r requirements.txt`

## Midiutil

[Midiutil](https://midiutil.readthedocs.io/en/latest/)
normally creates a .mid file, which can be played, for example, which VLC.

## Realtime midi

Install [fluidsynth](https://www.fluidsynth.org/), if you want to use 
[python-rtmidi](https://spotlightkid.github.io/python-rtmidi/installation.html) 
(realtime midi) to play tunes in realtime.

### MacOS & Homebrew

`brew install fluid-synth`

In addition, you need to download FluidR3_GM.sf2 for example 
[here](https://member.keymusician.com/Member/FluidR3_GM/index.html).
Unzip the archive and place the soundfont file in this directory.

Running flounsynth creates virtual midi device which can be used from python-rtmidi. 

`fluidsynth -o midi.driver=coremidi -o audio.driver=coreaudio -o audio.coreaudio.device=default -o audio.period-size=256 FluidR3_GM.sf2`

# Convert a .mid file to a .wav file

`fluidsynth -F out.wav FluidR3_GM.sf2 source.mid` 

# Random links

* [Frequency and Pitch](http://www.animations.physics.unsw.edu.au/jw/frequency-pitch-sound.htm)
* [Note names, MIDI numbers and frequencies](http://www.phys.unsw.edu.au/jw/notes.html)
