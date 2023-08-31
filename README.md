# schedule-scraper
## The Intention
With the switch from Veracross to Blackbaud a few years back we lost the ability to auto-create a pdf for our schedules. This program is my answer! I wanted something that I could quickly run to automatically create a pdf of my class rotation schedule. The script scrapes the portal of the needed information then cleans it all up so it can be put into a pdf from scratch.

## Installation and Setup
First, download the .exe in the Release Section. After it's downloaded start the setup.

## Configuration
After the setup a folder should be generated with all the scripts and necessary folders. You can ignore everything except two things:
```
schedule-creator.exe
pdf-config.ini
```
**BEFORE** running the script you must edit the `pdf-config.ini`! Once you open the file just change the login options under `[LOGIN]` to your Blackbaud credentials. Under the `[COLOR OPTIONS]` are just the choices for colors. You can, if you so choose, switch the pdf colors using the config file. To find a color search for "Color Picker" on Google and choose the color you want. Once chosen, copy the hex code value (e.g. #1c4f9c) and paste it into the `.ini` without the hashtag. The default colors are:

- ![#f4cccc](https://placehold.co/15x15/f4cccc/f4cccc.png) `#f4cccc -> A Block background color`
- ![#fce5cd](https://placehold.co/15x15/fce5cd/fce5cd.png) `#fce5cd -> B Block background color`
- ![#d9ead3](https://placehold.co/15x15/d9ead3/d9ead3.png) `#d9ead3 -> C Block background color`
- ![#c9daf8](https://placehold.co/15x15/c9daf8/c9daf8.png) `#c9daf8 -> D Block background color`
- ![#d9d2e9](https://placehold.co/15x15/d9d2e9/d9d2e9.png) `#d9d2e9 -> E Block background color`
- ![#ffaeeb](https://placehold.co/15x15/ffaeeb/ffaeeb.png) `#ffaeeb -> F Block background color`
- ![#f5ffc1](https://placehold.co/15x15/f5ffc1/f5ffc1.png) `#f5ffc1 -> G Block background color`
- ![#003366](https://placehold.co/15x15/003366/003366.png) `#003366 -> Header background color`
- ![#f3f3f3](https://placehold.co/15x15/f3f3f3/f3f3f3.png) `#f3f3f3 -> Header text color`
- ![#000000](https://placehold.co/15x15/000000/000000.png) `#000000 -> Normal text color`

## Use 
After the config file is fully setup you can continue on running the `schedule-creator.exe`. Once you open the .exe a console window will open and remain while the program runs, giving status updates as it goes through its program. As it runs a browser will open, ***DO NOT*** close the browser as the program is running or it will just crash after a while. Once the program runs its course it will ask for you to press "ENTER" to exit, which at once will generate the pdf in the folder where the .exe is located. The program can be executed multiple times but can also be deleted once the pdf is generated. The program is fully self-enclosed, meaning a simple delete of the folder will delete the program. 
