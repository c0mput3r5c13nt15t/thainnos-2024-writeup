# 中国音乐 (Chinese Music) – Solution

Running `strings mysong.ogg | grep "THAINNOS"` gives us multiple options for flags:

```bash
THAINNOS{Musiek is pragtig}COMM
THAINNOS{Musiek is pragtig}COMM
THAINNOS{Muzika 
THAINNOS{Musik itu indah}COMM
THAINNOS{Musika ederra da}COMM
THAINNOS{Musikk er vakker}COMM
THAINNOS{Muzika je prekrasna}COMM
THAINNOS{Musik er smuk}COMM
THAINNOS{Musik ist sch
THAINNOS{Music is beautiful}COMM
THAINNOS{Muziko estas bela}COMM
THAINNOS{Muusika on ilus}COMM
THAINNOS{Musiikki on kaunista}COMM
THAINNOS{La musique est belle}COMM
THAINNOS{Muzyk is prachtich}COMM
THAINNOS{[REDACTED]}COMM
THAINNOS{A m
THAINNOS{Tha ce
THAINNOS{Mizik b
THAINNOS{Music yana da kyau}COMM
THAINNOS{Egwu mara mma}COMM
THAINNOS{T
THAINNOS{T
THAINNOS{La musica
THAINNOS{Musik ayu}COMM
THAINNOS{La m
THAINNOS{A musica h
THAINNOS{Glazba je lijepa}COMM
THAINNOS{Mae cerddoriaeth yn brydferth}COMM
THAINNOS{Musica est pulcher}COMM
THAINNOS{Musek ass sch
THAINNOS{Tsara ny mozika}COMM
THAINNOS{Muzik cantik}COMM
THAINNOS{He ataahua te puoro}COMM
THAINNOS{Muziek is prachtig}COMM
THAINNOS{Musikk er vakker}COMM
THAINNOS{Nyimbo ndi zokongola}COMM
THAINNOS{A m
THAINNOS{Umuziki ni mwiza}COMM
THAINNOS{O musika e matagofie}COMM
THAINNOS{Mimhanzi yakanaka}COMM
THAINNOS{Musik
THAINNOS{Hudba je kr
THAINNOS{Muusiggu waa qurux badan yahay}COMM
THAINNOS{La m
THAINNOS{Mmino o motle}COMM
THAINNOS{Musik geulis}COMM
THAINNOS{Muziki ni mzuri}COMM
THAINNOS{Maganda ang musika}COMM
THAINNOS{Hudba je kr
THAINNOS{M
THAINNOS{Saz owadan}COMM
THAINNOS{Musiqa chiroyli}COMM
THAINNOS{Umculo mhle}COMM
THAINNOS{Umculo muhle}
THAINNOS{Musiek is pragtig}
```

Flags must have opening and closing parentheses and mustn't contain spaces. This leaves only one valid flag.


