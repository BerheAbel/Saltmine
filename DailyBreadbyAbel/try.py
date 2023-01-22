import re

new = re.findall(r"\([a-zA-Z0-9].+?\)", 'Mozilla/5.0 (webOS.TV-2022) Cobalt/22.lts.2.305573-gold (unlike Gecko) v8/8.8.278.8-jit gles Starboard/13, LG_TV_LM21AN_2022/02.00.45 (LG, 65UQ90006LA, Wired)')
print(new)