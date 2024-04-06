# RustyImage – Solution

Open the file in ghidra.

Go to ``Namespaces -> r -> rusty_image -> SECRET_IMAGE``.

View ``SECRET_IMAGE`` in hex view.

Copy the bytes from the hex view into a simple text editor.

Replace ``ff ff ff ff`` with ``🟥`` and replace ``ff 86 c0 6c`` with ``🟩``.

Add a newline ``\n`` after every 160 chars (dimension from the randomly generated images). You can do this using python.

The resulting image shows the flag.

*Writeup by [QWERTZexe](https://github.com/QWERTZexe)*