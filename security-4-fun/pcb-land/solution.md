# PCB Land

The `.gb` extension and the `file` command suggest that this is a Game Boy ROM. Let's try to run it in an [online emulator](https://taisel.github.io/GameBoy-Online/).

To get the flag we just have to play the game.

![1.png](./1.png)

The door is protected but, we can use voodoo.

![2.png](./2.png)

Just move him ...

![3.png](./3.png)

... and magically we can enter.

![4.png](./4.png)

The scanned QR gives us: `THAINNOS{<Key-A>Z7X3<Key-B>}`

![5.png](./5.png)

Key A is `D8ZR`

![6.png](./6.png)

![7.png](./7.png)

First the radio is useless, but after a few attempts we get:

![8.png](./8.png)

Key B is (hex as ASCII) `EE5U`.

Putting these pieces together we get the flag.