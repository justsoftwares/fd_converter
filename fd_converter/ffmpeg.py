from .utils import q, qp, img_to_video, get_video_size

default_ffparams = '-c:a aac -c:v h264_nvenc -b:a 224k -b:v 5M'


def get_ffmpeg_cmd(video, audio, subs, logo, intro, intro_img, logo_height, ffmpeg_params, out, rewrite):
    ffparams = ffmpeg_params if ffmpeg_params else ''
    ffparams += f' -{rewrite}'
    video = qp(video)
    audio = qp(audio)
    subs = qp(subs, "'", True)
    logo = qp(logo)
    size = get_video_size(video)
    if intro_img:
        intro = img_to_video(intro, dur=0.05)
    intro = qp(intro)
    out = qp(out)
    vp = '0:v'
    ln = 2
    sn = 2
    cmd = 'ffmpeg -hwaccel cuda '
    cmd += f'-i {video} -i {audio} '
    if intro:
        cmd += f'-i {intro} '
        ln += 1
        sn += 1
    if logo:
        cmd += f'-i {logo} '
        sn += 1
    cmd += '-filter_complex "'
    if logo:
        cmd += f'[{ln}:v]scale=-1:{logo_height}[logo],[0:v][logo]overlay=W-w:H-h[wl];'
        vp = 'wl'
    if subs:
        cmd += f'[{vp}]ass={subs}[ws];'
        vp = 'ws'
    if intro:
        cmd += f'[2:v]scale={size}:force_original_aspect_ratio=decrease,pad={size}:-1:-1,setsar=1[si];'
        cmd += f'[si][2:a:0][2:a:0][{vp}][1:a:0][0:a:0]concat=n=2:v=1:a=2[ov][od][oa]" '
        cmd += '-map "[ov]" -map "[od]" -map "[oa]" '
    else:
        cmd += f'-map "[vp]" -map 1:a '
    cmd += f'{ffparams} {out}'
    return cmd
