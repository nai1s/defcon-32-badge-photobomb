# defcon-badge-photobomb
An interactive game using the DC32 Badges

# What I'm Trying to Do

I want to build off the [Defcon Badge Photoframe](https://github.com/nai1s/defcon-32-badge-photoframe) project to make an IR-based photosharing game. Each badge would let people display images from their SD Card; if another person with the Photobomb code gets close and presses:

| Key | Action |
| --- | ----- |
| Left | Previous Image |
| Right | Next Image |
| A | Copy the images from every badge around me to my device |
| B | Copy my image to every device around me |

I want this to be available for both sharing stickers/art and physical "hacking" (really just getting close enough to someone else's badge that you can load your own image on it). If a lot of people are playing, at the end of the con people would have a LOT of random images shared with them.

After thinking through those details I was like "oh right, people sometimes share unwanted images with each other"... there's some implied consent that should be made explicit:

By installing this on your badge, you consent to receive images you may not like.

That said, I'm hoping the DEFCON crowd won't be jerks. Most of us are pretty cool.

# Where I'm Stuck

Getting Badge IR to work has been really difficult. I've tried both using UART-based implementations modeled off the source code and a third-party library called [Micropython IR](https://github.com/peterhinch/micropython_ir)


Unfortunately I can't get a consistent signal between two badges. Included is the micropython code I'm using to test this, you'll need to run the setup steps from [here](https://github.com/nai1s/defcon-32-badge-photoframe) to load micropython then use these files instead.

I can sometimes see partial signals showing up between the two using the UART implementation, but not in a consistent way (especially when I"m using interrupts). With 2 badges running this code I sometimes get gibberish:

```
b'\x7f\x7f\x7fw\x7f'
b'_\x7f?\x7f'
b'_\x7f\x7fo'
```

but this may be a false positive.