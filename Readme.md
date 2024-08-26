## Install

Firstly install python.

Visit [scoop.sh](https://scoop.sh/) or [python.org](https://www.python.org/downloads/).

`pip install fd-converter`

## GUI

usage: `python -OOm fd_converter.gui`

![main.png](https://raw.githubusercontent.com/justsoftwares/fd_converter/master/screenshots/main.png)

## CLI

### Help:

usage: `python -m fd_converter [-h] -v VIDEO -a AUDIO [-s SUBS] [-l LOGO] [-i INTRO] [-im INTRO_IMG] [-lh LOGO_HEIGHT] [-fp FFMPEG_PARAMS] -o OUT [-r REWRITE]`

```
options:
  -h, --help            show this help message and exit
  -v VIDEO, --video VIDEO
                        Video path
  -a AUDIO, --audio AUDIO
                        Audio path
  -s SUBS, --subs SUBS  Logo path
  -l LOGO, --logo LOGO  Logo path
  -i INTRO, --intro INTRO
                        Intro path
  -im INTRO_IMG, --intro-img INTRO_IMG
                        Intro is image
  -lh LOGO_HEIGHT, --logo-height LOGO_HEIGHT
                        Logo height
  -fp FFMPEG_PARAMS, --ffmpeg-params FFMPEG_PARAMS
                        Out path
  -o OUT, --out OUT     Out path
  -r REWRITE, --rewrite REWRITE
                        Rewrite (y/n)
```

ffmpeg defaults: -fp -c:a aac -c:v hevc_nvenc -b:a 224k -b:v 2M