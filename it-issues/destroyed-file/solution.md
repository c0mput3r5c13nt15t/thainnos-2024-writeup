# Destroyed File – Solution

Since opening the file in a text editor does not reveal anything, we can run file `file` command on it.

```bash
$ file secretx3.txt
secretx3.txt: Netpbm image data, size = 3036 x 1592, rawbits, pixmap
```

It seems that the file is some sort of image.

When opening the file in GIMP we can see a distorted image.

We can use the Shear tool to correct the distortion. We then duplicate the layer and place it, so that the text is complete. After that we rotate everything 180° and get the flag.
