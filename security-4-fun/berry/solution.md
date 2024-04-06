# 🍇

Extracting the zip, we get a file named `🍇` with the following content:

```emojicode
📦 testtube 🏠

🐇🦔🧪  🍇
  ✒️ ❗️ 🏁 🍇
      ⛔👇 22  ✖ 3  🙌 66 🔤22 times 3🔤❗️
    ⛔👇 ❎💯0 ❗️ 🙌 0.1 ❗️🔤float 0 != 0.1🔤❗️
    ⛔👇 🏧-9237173456 ❗️ 🙌 9237173456 🔤abs -9237173456🔤❗️
    ⛔👇 73.0  ➕ 7.0  🙌 80.0 🔤73.0 + 7.0 = 80.0🔤❗️
    ⛔👇 0  ◀️🙌 9 🔤0 <= 9🔤❗️😀🔤17o🔤❗️
    ⛔👇 ❎0  ◀ 0 ❗️🔤0 < 0🔤❗️
    ⛔👇 ❎1.2  ▶️🙌 1.26 ❗️🔤1.2 > 1.26🔤❗️
    ⛔👇 💧6❗ ✖ 3  🙌 18 🔤6 times 3🔤❗️
    ⛔👇 22  ➗ 2  🙌 11 🔤22 times 3🔤❗️
    ❎👇 ↔🔤abcdefg🔤 🔤abcdeff🔤❗️ 🙌 0 🔤String Compare🔤❗️😀🔤XD🔤❗️
    💯👇 🍺💯🔤+3.141592653589🔤❗️ 3.141592653589 🔤π to string🔤❗️
    [TRUNCATED]
    ⛔👇 ❎-0.22  ▶ -0.21 ❗️🔤-0.21 > -0.22🔤❗️
    🔢👇 📏🎶🔤🇧🇾🇧🇪🇨🇳🇧🇴🔤❗️❓ 4 🔤Count 4🔤❗️
    ❎👇 ↔🔤abcdefg🔤 🔤abcdef🔤❗️ 🙌 0 🔤String Compare🔤❗️😀🔤XY🔤❗️
    ⛔👇 🍺🔍🔤aaabb🔤 🔤aabb🔤❗️ 🙌 1 🔤Search A 1🔤❗️
    ⛔👇 🍺🔍🔤aa🔤 🔤a🔤❗️ 🙌 0 🔤Search A 0 2🔤❗️😀🔤XZ🔤❗️
    ⛔👇 -4  ◀️🙌 44 🔤-4 <= 44🔤❗️
    ⛔👇 🤜💧78❗ ❌ 55 🤛 🙌 121 🔤78 xor 55🔤❗️
    ⛔👇 🔋1.42❗ 🙌 -1.42 🔤-1 = -1🔤❗️
  🍉
🍉

🏁 ➡️ 🔢 🍇
  ↩️ 👔🆕🦔❗️❗️
🍉
```

This is [emojicode](https://www.emojicode.org/) which when executed gives us the following (you might have to rename it, so that the extension is `.emojic`):

```bash
$ emojicodec flag.emojic
$ ./flag 
17o
XD
15f
11m
19m
XP
10E
5N
XE
XH
XX
16r
XW
XL
XT
14i
XF
13j
XR
XG
3A
6N
XJ
7O
9{
12o
18m
XC
XS
22'
XM
4I
24}
XO
1T
XB
XQ
XU
XI
20y
8S
23D
XN
2H
XK
XV
XA
21:
XY
XZ
329 assertions, 0 failures
```

Removing the lines starting with `X` and sorting those with numbers gives us the flag.