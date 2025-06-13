---
title: "Lens Board"
author: "@Chris B"
description: "Mechanical keyboard with physical elements :)"
created_at: "2025-05-15"
---

**Total time spent: 52.5 hours**

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

**Time spent: 2 hours**

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

**Time spent: 2 hours**

## Lens Board - Journal 3 - 20/05/2025 - 21/05/2025

```
*Note*
Forgot to write this but I changed to metal gear servos 
because stepper motor drivers were too bulky / expensive
```

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

**Time spent: 5 hours**

# Lens Board - Journal 4 - 22/05/2025 - 28/05/2025

[Touchscreen](https://www.amazon.com/HiLetgo-240X320-Resolution-Display-ILI9341/dp/B073R7BH1B)

My deepest apologies review team, I have not been doing much journalling for the last week or so, because i've only been able to work on this project in mini chunks at school, etc, and haven't really had time to properly write anything.

Regardless, the last 6 days have been dedicated to finalizing the schematic and laying out the pcb, both of which are now done!

I'll try to go over everything roughly in chronological order, but y'know, some things might be skipped over or improperly ordered.

### Schematicizing!

I finished the schematic on the 24th, and it wasn't too bad. I just chucked on the touchscreen, using a generic spi interface with touch also using spi, and then added in the faders and scrolly wheel. Faders are super simple, just a potentiometer effectively, and the scrolly wheel is just a rotary encoder.

**Time spent: 1.5 hours**

### PCBinizing!

Alright, this one was a bit of a rocky road, but its pretty much done now...

![PCB Components](<https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/Screenshot 2025-05-22 205957.png>)

#### Part 1. The Basics

The first part of the pcb I did was just laying out the actual keyswitches, because they've got a predefined layout which makes it super easy to just place them without worrying about routing and stuff. I decided to use Kailh hotswao sockets, because they're pretty cheap on aliexpress and seemed more reliable and easier to desolder than millmaxes.

I started by just dropping in all the footprints, and laying them out with the correct spacing. Spoiler alert, this was completely wrong, and I only realised this after I had done all the routing and everything...
Next I chucked in the diodes, LEDs, and resistors, which was decently easy but took literal hours because each of the 300 components had to be placed effectively by hand and then routed.

Regardless, at the time I thought it was fine, so I continued on with the basic layout, now the start of the microcontroller section.

I started by hunting JLCPCB parts for a couple suitable connectors, and miraculously found some that had readily available footprints online, so the usb c and dc barrel jack were both easy to sort out. The placement of the rp2040 relative to the connectors was pretty important to get right, so i spent some time making sure I wouldn't have any grounding, impedance or stupid usb issues.

After laying out the microcontroller section, I started routing it, starting with the usb D+ and D- lines, then the power lines (placing the decoupling caps as close as possible), and then the crystal and other random stuff.

![Routed Microcontroller Section](<https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/Screenshot 2025-05-27 205356.png>)

Next up was the io expanders, which were just chucked on either end of the board, and then quickly routed. If you look at the actual routing, you might notice I have a lot of parallel traces, which is a bit iffy, but hopefully it'll be fine, because there's a ground plane and they're not too long or close.

Getting the traces down to the actual key matrix was a pain, because there's 25 traces which have to cross the i2c lines, and in the end i kinda just gave up. There's a lot of vias, and a lot of bad practices, but I think it should be ok.

![Finished PCB](<https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/Screenshot 2025-05-28 075806.png>)

**Time Spent: 13 hours**

#### Part 2. My amazing design skills

Just yesterday, I searched up how kailh hotswap sockets actually work, and realised that I had placed them completely wrong. Not only were they on the wrong side of the board, but there were also no holes for the actual keyswitch poles to go through, so I kinda had to reroute the entire keymatrix and leds. This was a massive pain, and as of the time of writing this, I'm still fixing traces which now pass through holes in the board :(

Anyway, once that was all fixed, my board was finally nearly done-ish, just needed to add the faders, scrolly wheel, and audio visualizer, as well as mounting holes and other random stuff. 

**Time Spent: 4 hours**

**Total Time Spent: 18.5 hours**

All right, images and more details will be added to this journal later, but for now, hopefully this is enough to sate your eternal hunger.

# Lens Board - Journal 5 - 29/05/2025 - 30/05/2025

Alrighty! 

The past couple days have just been spent adding some finishing touches to the pcb, rerouting the keymatrix, tidying up some routing for the io expanders, and finding footprints and routing the faders, scrolly wheel, and servos.

Somehow I managed to find an actual footprint for the sliders which is available on jlcpcb as a part, so that was amazing.

For servos, i'm just using a 3 pin header and I'll just hope that they all fit lol.

Scrolly wheel I yet again found a encoder that was exactly what I needed, available on JLCPCB, and had footprints readily available. I went with the AlpsAlpine EC11 something something, I've used other pots of theirs before on my macropad (which is sitting right in front of me atm actually :), and it has the right form factor for my wheel to work well.

![alt text](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/image-1.png)

I'm going to start working on the case now, so wish me luck! Fusion 360 is a hellscape for a blender person like me :(

**Time Spent: 4 hours**

# Lens Board - Journal 6 - 31/05/2025

Hello again!

Today was focused on making up the plate for the keyboard and sorting out what I'm going to do roughly for the case.

### The Plate

To start with, I did some research on plate materials, and decided on 1.5mm aluminium, which should be decently cheap on jlccnc, and also be just a decent overall material. 

```
*UPDATE*
I have got a quote from jlcpcb for this, 
and it ended up being around 50 bucks,
which should be within my budget.

Onwards!
```

I tried a couple methods for getting the plate, but eventually just used [ai03's plate generator](https://kbplate.ai03.com/) and editing the final thing. This took way longer than I thought it would because fusion 360 kept on moving my plate around instead of resizing it. At the moment, I have a slightly better understanding of how it works, but I ended up having to redo everything three or four times before getting it right. Not only this, but because I kinda just eyeballed my pcb, I had some awkward dimensions to work with, but I think its all good now!

![Keyboard Plate](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/image.png)

**Time Spent: 3 hours**

# Lens Board - Journal 7 - 01/06/2025

So... 

Fusion 360 failures strike again!
I accidentally resized the plate to 10mm too big, so I had to redo a bunch of dimensioning rather than actually work on the case, and now I'm going to go to bed. Sorry for short journal, had final dress rehearsal tonight and am ubermüde rn.

**Time Spent: 2.5 hours**

# Lens Board - Journal 8 - 2/06/2025 - 09/06/2025

Again, super sorry for the lack of updates, this is mainly because I've had no time to work on this at all due to show dates for school production, so i only could work on it during school lol, but over the past day or so I've had some time to work on the case for the keyboard, and I've managed to get it to a point where it could almost technically be functional.

At its current point, I'm using a sandwich style mount, where there's a bottom case, plate, and then a top case. The pcb could technically just be supported by the plate, but I'm going to use some standoffs just because the keyswitches aren't soldered, and it should also help the sound a bit. 

![Keyboard Mounting Styles](https://thomasbaart.nl/wp-content/uploads/2019/04/20190407_KeyboardMountingStylesCheatSheet.png)
*Source: [Thomas Baart](https://thomasbaart.nl/2019/04/07/cheat-sheet-custom-keyboard-mounting-styles/)*

The main reason this took so long is because everything I do is actively fought against by the software, but it's looking fine-ish now so I'm happy. 

More images coming soon, I have to go back through fusions version history bc I forgot to take screenshots and it takes a while.

**Time Spent: 7 hours**

# Lens Board - Journal 9 - 10/06/2025

Today I did a bunch more work on the case, namely, adding screw holes, moving everything into their own components, adding the servos and their brackets, adding supports for the music visualizer pins, and fixing the plate (again...)

#### Screw Holes

As I'm using a sandwich style mount, I needed to have the screws go up through the bottom case (threaded) through the plate (unthreaded) and into the top case (also threaded), so that the top case pulls tight the plate.

I'm using some m2 threaded inserts, and I think I've got the right dimensions, but Aliexpress datasheets are confusing so y'know.

There are a total of 14 screws, 12 on the top and bottom edge, and an extra two in the middle. Hopefully this is enough to stick it together :)

![Case Wireframe view showing holes](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/image-3.png)

#### Servos

Not much to say here, I found a 3d model, added 10 in a line, and adapted the cutout in the plate to make it a bit prettier.

I'm pretty proud of the parts I made on the plate, as it was the first time I could actually get fusion to properly work how I wanted it. They're to support the pins and hopefully keep them vertical, although as I'm writing this I can forsee some issues with only one support section.

![Servo Plate Slots](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/image-2.png)

\*Saving this for later, ignore please\*
[link](https://www.aliexpress.com/item/1005006838108683.html?spm=a2g0o.productlist.main.14.320326cfewKQ9W&algo_pvid=1e4c2149-119d-42ee-bb56-cf44e9f5507b&algo_exp_id=1e4c2149-119d-42ee-bb56-cf44e9f5507b-13&pdp_ext_f=%7B%22order%22%3A%22142%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21NZD%215.91%214.22%21%21%213.50%212.50%21%40210308a417495335958211390e6073%2112000038467725083%21sea%21NZ%210%21ABX&curPageLogUid=Bb3fqsRIwcdQ&utparam-url=scene%3Asearch%7Cquery_from%3A#nav-specification)
m2
od 3.2
l 3mm

**Time Spent: 2 hours**

# Lens Board - Journal 10 - 11/06/2025

I'm just going to call it done now. I added a little chamfer ish bit to the bottom to make it more than just a flat case. It looks massively thick in the photos but in reality it's only very thick (only 5mm thicker than my current keyboard)

![Finished Case](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/case.png)

![Finished Case Chamfer](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/case-bottom.png)

Also worked on checking prices for production, not looking great :(

**Time Spent: 2 hours**

# Lens Board - Journal 11 - 13/06/2025

Hello! I've spent the last two days tidying up everything, reorganising, writing boms, and writing an actual readme instead of the journal. You can probably look at git if you want to see the major changes, but it's just generally making sure I meet the submission requirements.

Just now I've spent the last couple of hours rendering my keyboard.

I tried to do it in Fusion but gave up and just exported it to blender for rendering, and I must say, I think it looks pretty good.

![Keyboard Render](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/keyboard-render-1-lit.png)
![Keyboard Render](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/keyboard-render-2-lit.png)
![Keyboard Render](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/keyboard-render-3-lit.png)

Literally submitting it as I speak, wish me luck :)

**Time Spent: 4.5 hours**