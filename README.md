# YyHelper

Free yourself from YinYangShi.

## Features

- [x] Automatic fight for Yuhun
- [x] Automatic fight for Juexing Materials
- [x] Automatic accept invite and ready when fight with group
- [x] Automatic fighting skills
- [x] Automatic fight for chapters

## Usage

1. Ensure `python` and `adb` command available in your terminal.

2. Connect your device with computer via USB, type `adb devices` to check if the connect is successful.

    ```sh
    $ adb devices
    List of devices attached
    cf264b8f        device
    ```

    Any connect issue can reference [here][1] to resolve.

3. Open YinYangShi and turn to Yuhun or Juexing Materials or other UI you are going to fight.

4. Run command:

    ```sh
    python YyHelper.py [mode]
    ```

    Argument `mode` is optional. Default value is `--material`.

    Available `mode` values:

    | arguments        | meaning                    |
    |------------------|----------------------------|
    | -m or --material | Yuhun or Juexing Materials |
    | -s or --skill    | Fighting skills            |
    | -g or --group    | Materials with group       |
    | -c or --chapter  | Fight for chapters         |

5. Enjoy it!

[1]: https://github.com/mzlogin/awesome-adb#%E8%AE%BE%E5%A4%87%E8%BF%9E%E6%8E%A5%E7%AE%A1%E7%90%86
