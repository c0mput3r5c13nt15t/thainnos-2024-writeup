# LicenseBypassV2 – Solution

For this one we can take a shortcut (which actually also works for V1) and just use  `strings` to get the flag:

```bash
$ strings business_solution_manager_v2 | grep "THA"
[TRUNCATED]
abortbufio: tried to fill full bufferuse of closed network connection" not supported for cpu option "THAINNOS{[REDACTED]}key-value delimiter not found:
[TRUNCATED]
```
