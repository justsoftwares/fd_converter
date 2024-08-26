from __future__ import annotations

import argparse
from os import system

from fd_converter.ffmpeg import get_ffmpeg_cmd, default_ffparams


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', help='Video path', required=True)
    parser.add_argument('-a', '--audio', help='Audio path', required=True)
    parser.add_argument('-s', '--subs', default=None, help='Logo path')
    parser.add_argument('-l', '--logo', default='logo.png', help='Logo path')
    parser.add_argument('-i', '--intro', default=None, help='Intro path')
    parser.add_argument('-im', '--intro-img', default=False, type=bool, help='Intro is image')
    parser.add_argument('-lh', '--logo-height', default=50, type=int, help='Logo height')
    parser.add_argument('-fp', '--ffmpeg-params', default=default_ffparams, help='Out path')
    parser.add_argument('-o', '--out', default='out.mkv', help='Out path', required=True)
    parser.add_argument('-r', '--rewrite', default='y', help='Rewrite (y/n)')
    args = parser.parse_args()

    cmd = get_ffmpeg_cmd(args.video, args.audio, args.subs, args.logo, args.intro, args.intro_img, args.logo_height,
                         args.ffmpeg_params, args.out, args.rewrite)
    print(cmd)
    system(cmd)
    print('Success!')


if __name__ == '__main__':
    main()
