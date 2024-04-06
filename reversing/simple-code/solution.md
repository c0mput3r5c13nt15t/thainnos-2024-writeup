# SimpleCode – Solution

Just running the file we get:

```bash
$ ./getflag 
You're doing it wrong!
```

We can decompile the binary using Ghidra and look at the `main` function:

```c
undefined8 main(int param_1,long param_2)

{
  int iVar1;
  FILE *__s;
  
  if (param_1 == 3) {
    __s = fopen(*(char **)(param_2 + 8),"wb"); // Opens the first argument as file
    iVar1 = atoi(*(char **)(param_2 + 0x10)); // Gets the second argument as number
    if (iVar1 == 0x134d74e) {  // Checks if the number is `0x134d74e` (`20240206` in decimal)
      fwrite(&x1,1,1,__s);
      fwrite(&x2,1,1,__s);
      fwrite(&x3,1,1,__s);
      fwrite(&x4,1,1,__s);
      fwrite(&x5,1,1,__s);
      fwrite(&x6,1,1,__s);
      fwrite(&x7,1,1,__s);
      fwrite(&x8,1,1,__s);
      fwrite(&x9,1,1,__s);
      fwrite(&x10,1,1,__s);
      fwrite(&x11,1,1,__s);
      fwrite(&x12,1,1,__s);
      fwrite(&x13,1,1,__s);
      fwrite(&x14,1,1,__s);
      fwrite(&x15,1,1,__s);
      fwrite(&x16,1,1,__s);
      fwrite(&x17,1,1,__s);
      fwrite(&x18,1,1,__s);
    }
    fclose(__s);
  }
  else {
    puts("You\'re doing it wrong!");
  }
  return 0;
}
```

It seems like the program needs two arguments, the first one is the file to write to and the second one is a number. If the number is `20240206` (see line 10) it writes the flag to the file.

We can run the program with the correct arguments and get the flag:

```bash
$ ./getflag flag.txt 20240206
$ cat flag.txt 
[REDACTED]
```
