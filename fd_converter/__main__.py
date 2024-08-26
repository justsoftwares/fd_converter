from os import system
from fd_converter import get_ffmpeg_cmd, default_ffparams
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', type=str, help='Video path')
    parser.add_argument('-a', '--audio', type=str, help='Audio path')
    parser.add_argument('-s', '--subs', default=None, type=str, help='Logo path')
    parser.add_argument('-l', '--logo', default='logo.png', type=str, help='Logo path')
    parser.add_argument('-i', '--intro', default=None, type=str, help='Intro path')
    parser.add_argument('-im', '--intro-img', default=False, type=bool, help='Intro is image')
    parser.add_argument('-lh', '--logo-height', default=50, type=int, help='Logo height')
    parser.add_argument('-fp', '--ffmpeg-params', default=default_ffparams, type=str, help='Out path')
    parser.add_argument('-o', '--out', default='out.mkv', type=str, help='Out path')
    parser.add_argument('-r', '--rewrite', default='y', type=str, help='Rewrite (y/n)')
    args = parser.parse_args()

    cmd = get_ffmpeg_cmd(args.video, args.audio, args.subs, args.logo, args.intro, args.intro_img, args.logo_height,
                         args.ffmpeg_params, args.out, args.rewrite)
    print(cmd)
    system(cmd)
    print('Success!')


if __name__ == '__main__':
    main()
