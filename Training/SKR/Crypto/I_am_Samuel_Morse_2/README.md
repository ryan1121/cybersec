# I am Samuel Morse 2!

[toc]

## Description
Can encrypted messages be in audio files?

Flag format: SKR{flag_flag}

## Solution
This challenge is Morse Code challenge similar to the first `I am Samuel Morse !` challenge.
However, this is different from how Morse code is used, which is now audio.
We can use online [Morse Code Adaptive Audio Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) to decode the audio file provided : [morse_1.wav](./morse_1.wav)

Then we got the flag's content : 
```
AUD1OM0R53C0D315G0OD
``` 

> *You may need to try more than one times, beecause my accuracy with that decoder wasn't very good :/*


## Flag
```
SKR{AUD1OM0R53C0D315G0OD}
```
