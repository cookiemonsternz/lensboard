# Lens Board

Lens Board is a custom mechanical keyboard, with a modified 1800's layout, more physical input methods (sliders, scrolly wheel, touchscreen) and an inbuilt, *physical* audio visualizer.

#### The Why

My inspiration for this project was my [Hackpad](https://hackpad.hackclub.com/) project, which I had a ton of fun designing and building. I wanted to make another thing to do with keyboards, and this was a great opportunity to do so.

In terms of the actual design choices of the keyboard, I'm a massive fan of analog / physical inputs and outputs. As a musician and LD, I like faders, so a few of those were an obvious choice. 

I decided to add a music visualizer because its just something I'm passionate about, putting some form of visual representation to sound. I do lighting for this reason, and I made my [music visualizer](https://cookiemonsternz.github.io/music-visualiser/) for high seas also because of this.

Anyways, here are some shots of my project :)

![Render of keyboard](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/keyboard-render-1-lit.png)
![Render of keyboard](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/keyboard-render-2-lit.png)
![Render of keyboard](https://raw.githubusercontent.com/cookiemonsternz/lensboard/refs/heads/main/img/keyboard-render-3-lit.png)
<video width="1280" height="720" src="https://github.com/user-attachments/assets/c497ad9b-a288-478b-a588-d2af06add98a"></video>


### BOM
| Component              | Qty | Link                                                                                           | Source                        | Price      | Notes                                                                 |
| ---------------------- | --- | ---------------------------------------------------------------------------------------------- | ----------------------------- | ---------- | --------------------------------------------------------------------- |
| SMD Capacitors         | 16  | N/A                                                                                            | JLCPCB Standard Parts Library | Minimal    |                                                                       |
| SMD Diodes             | 100 | [B0540WS](https://jlcpcb.com/partdetail/Hongjiacheng-B0540WS/C7420326)                         | JLCPCB Standard Parts Library | Minimal    |                                                                       |
| SMD LEDs               | 100 | [KT0603W](https://jlcpcb.com/partdetail/Hubei_KentoElec-KT0603W/C2290)                         | JLCPCB Standard Parts Library | \~1 USD    |                                                                       |
| SMD Resistors          | 108 | N/A                                                                                            | JLCPCB Standard Parts Library | Minimal    | Will be sourced outside of PCBA as they go on the bottom of the board |
| DC Barrel Jack         | 1   | [DC005](https://jlcpcb.com/partdetail/ShouHan-DC005/C431533)                                   | JLCPCB Extended Parts Library | Minimal    | Placed on bottom of board, will be manually sourced                   |
| USB Type-C Port        | 1   | [TYPE\_C\_31\_M12A](https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M12A/C5337088) | JLCPCB Extended Parts Library | \~0.25 USD | Ordering extra units (110) to account for possible errors             |
| Kailh Hotswap Sockets  | 100 | [Aliexpress Link](https://www.aliexpress.com/item/1005007476614771.html)                       | Aliexpress                    | \~6.50 USD | Price can drop to \~\$0.40 USD/unit if single units are sourced       |
| Rotary Encoder         | 1   | [Aliexpress Link](https://www.aliexpress.com/item/1005005678408977.html)                       | Aliexpress                    | \~4 USD    |                                                                       |
| RP2040 Microcontroller | 1   | [RP2040](https://jlcpcb.com/partdetail/RaspberryPi-RP2040/C2040)                               | JLCPCB Extended Parts Library | \~1 USD    | Slightly different than original spec, should be fine                 |
| Voltage Regulator      | 1   | [AMS1117-3.3](https://jlcpcb.com/partdetail/Tdsemic-AMS1117_33/C22466222)                      | JLCPCB Extended Parts Library | Minimal    |                                                                       |
| Flash Memory           | 1   | [W25Q128JVSIQ](https://jlcpcb.com/partdetail/WinbondElec-W25Q128JVSIQ/C97521)                  | JLCPCB Extended Parts Library | \~0.8 USD  |                                                                       |
| Crystal Oscillator     | 1   | [ABM8-27.2](https://jlcpcb.com/partdetail/AbraconLlc-ABM8_272T3/C20625731)                     | JLCPCB Extended Parts Library | \~0.4 USD  |                                                                       |
| IO Extender (MCP23017) | 2   | [MCP23017](https://jlcpcb.com/partdetail/MicrochipTech-MCP23017T_EML/C629439)                  | JLCPCB Extended Parts Library | \~3 USD    |                                                                       |
| LED MOSFET             | 1   | [IRLML6344TRPBF](https://jlcpcb.com/partdetail/TechPublic-IRLML6344TRPBF/C28646354)            | JLCPCB Extended Parts Library | Minimal    |                                                                       |
| Slide Potentiometer    | 2   | [PTA3043](https://jlcpcb.com/partdetail/Bourns-PTA30432010CIB103/C5357832)                     | JLCPCB Extended Parts Library | \~4 USD    |                                                                       |
| Touchscreen            | 1   | [HiLetGo2.8"SPI](https://www.aliexpress.com/item/1005006623369442.html)                        | Aliexpress                    | \~6 USD    |                                                                       |


| Component       | Qty | Link                                                                     | Source      | Price     | Notes                                               |
| --------------- | --- | ------------------------------------------------------------------------ | ----------- | --------- | --------------------------------------------------- |
| Plate           | 1   | N/A                                                                      | JLCCNC      | \~50 USD  | Aluminum preferred; will explore cheaper materials  |
| Top Case        | 1   | N/A                                                                      | 3D Print    | \~3 USD   | Printed by self                                     |
| Bottom Case     | 1   | N/A                                                                      | 3D Print    | \~3 USD   | Printed by self                                     |
| M2 Screws       | 14  | N/A                                                                      | Local Store | \~5 USD   | To be sourced from a nearby hardware store          |
| Heatset Inserts | 28  | [Aliexpress Link](https://www.aliexpress.com/item/1005006838108683.html) | Aliexpress  | \~1.5 USD | 100 pcs ordered — very cheap and small              |
| PCB             | 1   | N/A                                                                      | JLCPCB      | Included  |                                                     |
| Keyswitches     | 100 | [Aliexpress Link](https://www.aliexpress.com/item/1005007534872693.html) | Aliexpress  | \~18 USD  | Prefer not to mix, though 30 spare switches on hand |
| Keycaps         | 100 | [Aliexpress Link](https://www.aliexpress.com/item/1005008486798694.html) | Aliexpress  | \~5 USD   | TBD                                                 |
| PCBA            | 1   | N/A                                                                      | JLCPCB      | \~100 USD | Hoping to reduce cost with coupons                  |


| Description                         | Price Estimate  |
| ----------------------------------- | --------------- |
| Total (Pre-Coupons, with Shipping)  | \~216 USD       |
| Total (Post-Coupons, with Shipping) | \~136 USD       |

Actual Costs
| Description                         | Price  |
| ----------------------------------- | ------ |
| PCB + PCBA + shipping               | 198.41 |
| Aliexpress Components + shipping    | 41.71  |
| ----------------------------------- | ------ |
| Total pre coupons                   | 240.12 |
| Total Post coupons                  | 160.12 |

*This is without the plate, as I couldn't fit it into the budget. I am planning on machining this using my schools cnc.
