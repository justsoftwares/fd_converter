py "C:\Portable Programs\конвертер\main.py" -v "C:\Portable Programs\конвертер\ch_example\video.mkv" -a "C:\Portable Programs\конвертер\ch_example\audio.flac" -s "C:\Portable Programs\конвертер\ch_example\subs.ass" -l "C:\Portable Programs\конвертер\ch_logos\logo_cr.png" -lh 50 -o "C:\Portable Programs\конвертер\ch_example\out.mkv"

Помощь:
usage: main.py [-h] [-v VIDEO] [-a AUDIO] [-l LOGO] [-s SUBS] [-lh LOGO_HEIGHT] [-o OUT] [-fp FFMPEG_PARAMS]

options:
  -h, --help            show this help message and exit
  -v VIDEO, --video VIDEO
                        Video path
  -a AUDIO, --audio AUDIO
                        Audio path
  -l LOGO, --logo LOGO  Logo path
  -s SUBS, --subs SUBS  Logo path
  -lh LOGO_HEIGHT, --logo-height LOGO_HEIGHT
                        Logo height
  -o OUT, --out OUT     Out path
  -fp FFMPEG_PARAMS, --ffmpeg-params FFMPEG_PARAMS
                        Out path

Если надо добавить дополнительные аргументы, то дефолтные настройки к ffmpeg такие: -fp -c:a aac -c:v hevc_nvenc -b:a 224k -b:v 2M

Наиболее удобным способом запускать будет открытие консоли в специально созданной папке с переименованными в короткие названия файлами, указание py "C:\Portable Programs\конвертер\main.py" -l "C:\Portable Programs\конвертер\ch_logos\logo_cr.png" -lh 50, а дальше по help-у всех остальных аргументов.