# Lens Board

Lensboard is a keyboard! I did hackpad v1, but didn't get to do hackpad v2 due to exams :(
Other than being a keyboard, Lensboard has some unique features...

### Introducing...

ANALOG INPUTS!
Physical controls are the single most satisfying thing in the world. Clicky, scrolly, wavy, whatever - as long as it's physical, it's fun.

## The Plan

Quick overview:

- 1800 Compact Layout (Fullsize but squished)
- Low profile
- White backlight
- RGB underglow
- Audio Visualizer (physical)
- Scrolly Wheel (clicky)
- Fader
- Mini touchscreen (for color pickers, music player)

### Audio Visualizer

Basically, this is a line of little rods, that move up and down based on a fft of the audio input. They're moved by ten litte stepper motors (because servos are noisy as hell).

Here is my amazing diagram:

<img alt="A horizontal line of ten green rods, at various heights." src="./audio-visualiser-demo.png" style="width: 256px;-ms-interpolation-mode: nearest-neighbor;
  /* Firefox */
  image-rendering: crisp-edges;
  /* Chromium + Safari */
  image-rendering: pixelated;">

And these little green bars will move up and down with audio.

### Scrolly Wheel

Its a scrolly wheel!

Apologies for my absolutely atrocious drawing skills, but here is what I'm thinking for the profile. 

<img alt="Scrolly wheel diagram" src="./scrolly-wheel-demo.png" style="width: 256px;-ms-interpolation-mode: nearest-neighbor;
  /* Firefox */
  image-rendering: crisp-edges;
  /* Chromium + Safari */
  image-rendering: pixelated;">

This will likely be 3d printed, and use a rotary encode so its nice and clicky.

### Fader

I'm a bit of a lighting nerd, and as you know, lighting nerds love faders.

<img alt="Fader (slide potentiometer / slider)" src="./fader-demo.png" style="width: 64px;-ms-interpolation-mode: nearest-neighbor;
  /* Firefox */
  image-rendering: crisp-edges;
  /* Chromium + Safari */
  image-rendering: pixelated;">

This is just a user mappable fader, but I'll probably set it up as a lighting thing, so I can move it and have stuff happen with lights in my room lol.

### Mini Touchscreen

I just like the idea of having a tiny little display in the corner.

It'll probably have a little media control center or color picker for art stuff or lighting programming.

<img alt="Media Player with album art" src="./touchscreen-demo-1.png" style="width: 128px;-ms-interpolation-mode: nearest-neighbor;
  /* Firefox */
  image-rendering: crisp-edges;
  /* Chromium + Safari */
  image-rendering: pixelated;">
<img alt="HSV Color picker" src="./touchscreen-demo-2.png" style="width: 128px;-ms-interpolation-mode: nearest-neighbor;
  /* Firefox */
  image-rendering: crisp-edges;
  /* Chromium + Safari */
  image-rendering: pixelated;">

