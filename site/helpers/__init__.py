import re

def check_embed_dir(embed_dir):
    if embed_dir.exists() and not embed_dir.is_dir():
        err = 'Whoops! You somehow have an {} which isn\'t a directory!'
        print(err.format(str(embed_dir)), file=sys.stderr)
        exit(1)
    elif not embed_dir.exists():
        embed_dir.mkdir()


def is_podcast(path):
    return re.search(r'\d+-.*\.md', str(path)) is not None


EMBED_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <link rel='stylesheet' type='text/css' href='/embed.css' charset='utf-8'>
</head>
<body>
<div class='player'>
  <img
    src='{logo}'
    srcset='
      {cdn}/cover-100-2x.jpg 200w, 
      {cdn}/cover-200-2x.jpg 400w,
      {cdn}/cover-400-2x.jpg 800w,
      {cdn}/cover-800-2x.jpg 1600w,
      {cdn}/cover.jpg'
    alt='Mass Affection'
    title='Mass Affection'
    class='player__image' />
  
  <audio class='player__interface' controls preload='metadata'>
    <source src='{src}' type='audio/mpeg'></source>
    Your browser does not support the audio element.
  </audio>
</div>
</body>
</html>
"""


def embed(src, logo, cdn):
    full_src = cdn + '/' + src
    return EMBED_TEMPLATE.format(src=full_src, logo=logo, cdn=cdn)
