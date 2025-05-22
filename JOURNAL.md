---
title: "Lens Board"
author: "@Chris B"
description: "Mechanical keyboard with physical elements :)"
created_at: "2025-05-15"
---

# Lens Board - Journal 1 - 15/05/2025

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

![line of ten green rods](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/audio-visualiser-demo.png)

And these little green bars will move up and down with audio.

### Scrolly Wheel

Its a scrolly wheel!

Apologies for my absolutely atrocious drawing skills, but here is what I'm thinking for the profile. 

![Scrolly Wheel](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/scrolly-wheel-demo.png)

This will likely be 3d printed, and use a rotary encode so its nice and clicky.

### Fader

I'm a bit of a lighting nerd, and as you know, lighting nerds love faders.

![Fader](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/fader-demo.png)

This is just a user mappable fader, but I'll probably set it up as a lighting thing, so I can move it and have stuff happen with lights in my room lol.

### Mini Touchscreen

I just like the idea of having a tiny little display in the corner.

It'll probably have a little media control center or color picker for art stuff or lighting programming.

![Touchscreen](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/touchscreen-demo-1.png)
![Color Picker](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/touchscreen-demo-2.png)

#### Welp...
Thats me for today! I'm gonna start some research on parts for tomorrow's entry, but thats my overall vision for this project. Looking forward to getting this going!

# Lens Board - Journal 2 - 17/05/2025

Today I'm just doing some more thinking on some specifics of the parts I'll be using for the analog input on the keyboard. I'm just going over all the parts (touchscreen, wheel, faders, etc.) and figuring out how they'll be actually integrated into the board.

So, without further ado:

#### Touchscreen
I'm just going to go with a generic TFT touchscreen for this. I'm decided between 1.8", 2.2", or 2.8"

If I go 1.8", then I have less of a problem with it fitting on the keyboard, but 2.2" seems to be the most common size (and has some pretty decent resolutions for cheap).

#### Scrolly Wheel

As I see it, I have two or three major options for the scrolly wheel. 

##### Option 1 - Rotary Encoder
Basically, mount a rotary encoder horizontally, attach the wheel, and its done. 

This approach is nice and easy, but also might have some problems.

![Rotary Encoder](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/scrolly-wheel-encoder-demo.png)

When the user presses down on the opposite side of the wheel to the encoder, there might be some flex, and there could also be some problems with the encoder legs bending, which might be very annoying.

##### Option 2 - Motor with Encoder

Option 2 is just a DC motor with a magnetic encoder.

By doing this, you can have the microcontroller be aware of the wheel position as with a rotary encoder, but you can also move the motor to simulate the detents of a regular rotary encoder. You can also program it to have different motion profiles, like maybe a snap back to the center after moving.

![Motor with Encoder](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/scrolly-wheel-motor-demo.png)

Unfortunately, this approach has about all the cons you could think of:
- More expensive
- More physically complicated
- Harder to implement
- Bulkier
- Still doesn't solve the bending problem

**Ultimately**, I'm probably going to go with the rotary encoder, mainly because of space, but I need to find a way to hide the actual encoder and support the other end, maybe this kind of system:

![Rotary Encoder with Support](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/scrolly-wheel-case-demo.png)

But I also want the wheel to be above the case, so more thought is required.

#### Faders

I think maybe two faders would be better, just looking at the layout of the touchscreen, scrolly wheel, and faders.

Heres my beautiful mockup of how it might look. This section will sit to the right of the keyboard and there are two main layouts I'm considering.

![Layout 1](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/layout-demo-1.png)![Layout 2](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/layout-demo-2.png)![Layout 3](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/layout-demo-3.png)

Honestly, I don't mind all of these (ignoring the ugly colours lol), but I think either the first or third will be what I go with. It doesn't make too big of a difference to the electronics which I do, so for now I'll just design as if I'm doing the first one.

As for the actual faders, they'll probably be around 60-80mm of travel, and other than that, just generic faders.

#### Audio Visualiser

Alright, the big, annoying, *"how the hell will I do this"* part!
Well, I've had a bit of look and I've come up with a bit of a plan.

First of all, choosing the motors.

Aliexpress has once again come to the rescue, with some tiny steppers intended to be used in camera lenses, but will work perfectly fine for my use case. These are absolutely tiny motors, but they are fully dimensioned, which is an amazing attribute to have.

![Stepper Motor](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/motor-dimensions.png)

Now onto the actual mechanism for driving a pin.
I'm going to use a basic cam follower mechanism, which not only ensures smooth transitions between positions, but is also probably the easiest method to build, having no gears which are hellish to 3d print.

![Pin Mechanism](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/pin-mechanism-demo.gif)

By controlling the rotation of the cam (because they're going to be steppers, not DC motors), you can control the height of the pin.

*Quick sidenote, but the cam profile could technically be better utilized than the above diagram in order to maximise the distance resolution per degree, if it were similar to the following profile:*

![Spiral Cam Profile](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/spiral-cam-profile.png)

*But this also limits the cam to moving in one direction, and adds a sudden drop when looping, so a pear shaped cam is better for my requirements.*

Das ist alles, tomorrow I'll get started on the actual schematic design.

## Lens Board - Journal 3 - 20/05/2025 - 21/05/2025

Actual schematic design is taking place!

First of all, picking an mcu.

This is mainly determined by the number of pins required, which is as below.

For the audio visualizer, actually going to go with steppers, but some slightly nicer non plastic geared ones and have them running slowly so they don't make as much noise.

### Pins:
- <25 - Key Matrix
- 2 - Rotary Encoder (scrolly wheel)
- 1-2 - Faders
- 5-11 - Regular Screen / Touchscreen
- 10 - Audio Visualizer (1 per servo)
- 1 - Neopixels
Overall - <51 pins

To this end, I've decided to go with the rp2040, which has 25 gpios, and use 2 mcp23017s to get it up to 57 total pins. I've used the rp2040 before on another little macropad, and its got really good design documents and spec sheets, so it should be easy enough to get it working and running qmk.

I've already made a board using the rp2040 in the past, so I can luckily just copy the schematic over for the base design, and just add the key matrix, io expanders, and other stuff on top.

### The keyboard layout
As I've already said, this is going to be an 1800's compact layout, which is basically a fullsize keyboard but a bit squished. 

1800's layouts typically have only a few of the navigation keys (home, end, pgup, pgdn, del, ins), but I've decided to include all of them, at the expense of a few utility keys (menu, prtsc, right ctrl, right alt, right win). I also have included two macro keys (m1 and m2) which will probably be just user defined.

![Keyboard Layout](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/keyboard-layout.png)

### The schematic:

After several hours of work, I've got the basic schematic done for the key matrix with the io expanders. I used a 19x6 matrix, which isn't the most efficient, but it makes routing and layout a lot easier than a 10x10 matrix, and doesn't take up too many extra pins (only 5 more than a 10x10 matrix).

#### Key Matrix

![Keyboard layout wiring](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/keyboard-wiring.png)

![Key Matrix Schematic](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/key-matrix-schematic.png)

#### Microcontroller

![Microcontroller Schematic](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/microcontroller-schematic.png)

#### IO Expanders

<sub>*GPA7 and GPB7 cannot be used as inputs*</sub>

![IO expander schematic](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/io-expander-schematic.png)

Alright, thats all for today, continuing with the schematic tomorrow to finish up with the other components. Touchscreen is the only one I'm mildly concerned about, but it should be fine.

# Lens Board - Journal 4 - 22/05/2025

[Touchscreen](https://www.amazon.com/HiLetgo-240X320-Resolution-Display-ILI9341/dp/B073R7BH1B)

I have finished the schematic for the keyboard!
![Keyboard Schematic](./keyboard-schematic.png)
