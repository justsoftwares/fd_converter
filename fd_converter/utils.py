from __future__ import annotations

from os import system
from pathlib import Path
from subprocess import check_output


def q(s: str, q: str = '"') -> str:
    return f'{q}{s}{q}' if ' ' in s else s


def qp(s: str | Path, qt: str = '"', rdp: bool = False):
    if s:
        s = str(Path(s).absolute().as_posix())
        if rdp:
            s = f'{s[:1]}\\{s[1:]}'
        return q(s, qt)
    return ''


def img_to_video(img_path: Path | str, dur: float = 0.05) -> Path:
    out = Path(img_path).with_suffix('.mkv')
    cmd = f'ffmpeg -hwaccel cuda -loop 1 -i {qp(img_path)} -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -c:v hevc_nvenc -c:a aac -map 0 -map 1 -t {dur} -y {qp(out)}'
    print(cmd)
    system(cmd)
    return out


def get_video_size(video_path: str) -> str:
    cmd = f'ffprobe {video_path} -v error -select_streams v -show_entries stream=width,height -of csv=p=0:s=\':\''
    size = check_output(cmd).decode().strip()
    return size
