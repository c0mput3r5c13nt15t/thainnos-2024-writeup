# LicenseBypass

When running the executable we get:

```bash
$ ./business_solution_manager 
USB dongle not connected. Permission denied.
```

But when we change the `app_mode` in `internal_settings.ini` to `developemnt` we get:

```bash
$ ./business_solution_manager 
2024/02/14 15:10:59 Checking for dongle ID 4242:1337
2024/02/14 15:10:59 USB ID 1d6b:0003 connected
2024/02/14 15:10:59 USB ID 1a2c:4094 connected
2024/02/14 15:10:59 USB ID 1d6b:0002 connected
2024/02/14 15:10:59 USB ID 1d6b:0003 connected
2024/02/14 15:10:59 USB ID 0bda:b00a connected
2024/02/14 15:10:59 USB ID 30c9:0035 connected
2024/02/14 15:10:59 USB ID 046d:c52b connected
2024/02/14 15:10:59 USB ID 1d6b:0002 connected
USB dongle not connected. Permission denied.
```

Now if we change the `dongle_id` to one of the connected USB IDs we get:

```bash
$ ./business_solution_manager 
2024/02/14 15:12:01 Checking for dongle ID 1d6b:0003
2024/02/14 15:12:01 USB ID 1d6b:0003 connected
2024/02/14 15:12:01 USB ID 1a2c:4094 connected
2024/02/14 15:12:01 USB ID 1d6b:0002 connected
2024/02/14 15:12:01 USB ID 1d6b:0003 connected
2024/02/14 15:12:01 USB ID 0bda:b00a connected
2024/02/14 15:12:01 USB ID 30c9:0035 connected
2024/02/14 15:12:01 USB ID 046d:c52b connected
2024/02/14 15:12:01 USB ID 1d6b:0002 connected
License check successful!

You can now make full use of our Product Creation Pipeline to efficiently create real VALUE for your shareholders. INSTANTLY generate valuable experiences for your customers with your personal Management Communicator. Usher in the FUTURE with our genuine portfolio of creative tools. MONETIZE your processes with our suite of Seamless Integration Modules. Achieve full SCALABILITY by making use of our B2B Customer Service Experience. Our platform enables SUSTAINABLE growth and FRICTIONLESS expansion for YOUR business.

CHANGE THE WORLD!

NOW!

This is your personal access code:
THAINNOS{[REDACTED]}
```

The output text contains the flag.
