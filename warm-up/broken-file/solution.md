# Broken File – Solution

Since opening the file in a text editor does not reveal anything useful, we can run file `file` command on it.

```bash
$ file secret.txt
secret.txt: Netpbm image data, size = 2762 x 1801, rawbits, pixmap
```

It seems that the file is some sort of image.

When opening the file in GIMP we can see a string, which is the flag.
