# RS-274 – Solution

The title of the file guives us a hint that the content is base64 encoded. Decoding it gives us the following.

```gcode
G94     ( Inches per minute feed rate. )
G20     ( Units == INCHES.             )
G90     ( Absolute coordinates.        )
S10000  ( RPM spindle speed.           )
M3      ( Spindle on clockwise.        )

G64 P0.00500 ( set maximum deviation from commanded toolpath )

G04 P0 ( dwell for no time -- G64 should not smooth over this point )
G00 Z0.19685 ( retract )

G00 X2.03000 Y-1.69901 ( rapid move to begin. )
G01 Z-0.00197 F23.62205 ( plunge. )
G04 P0 ( dwell for no time -- G64 should not smooth over this point )
X2.03000 Y-1.69901
X2.03300 Y-1.69901
X2.03300 Y-1.70301
X2.03100 Y-1.70301
X2.03100 Y-1.70401
[TRUNCATED]
X-2.91900 Y-5.39401
X-2.92400 Y-5.39401
X-2.92400 Y-5.39501
X-2.92500 Y-5.39501
X-2.92500 Y-5.39601
G04 P0 ( dwell for no time -- G64 should not smooth over this point )
G00 Z0.19685 ( retract )

G00 X-2.84100 Y-5.39901 ( rapid move to begin. )
G01 Z-0.00197 F23.62205 ( plunge. )
G04 P0 ( dwell for no time -- G64 should not smooth over this point )
X-2.84100 Y-5.39901
X-2.84100 Y-5.46201
X-2.77400 Y-5.46201
X-2.77400 Y-5.39501
X-2.84100 Y-5.39501
X-2.84100 Y-5.39901

G04 P0 ( dwell for no time -- G64 should not smooth over this point )
G00 Z0.00000 ( retract )

M9 ( Coolant off. )
M2 ( Program end. )
```

The resulting text is gcode which when run (in a [simulator](https://ncviewer.com/)) shows two pcb boards, one of which shows the flag.
