# coding=utf-8
# conf: config

import os

#mfa_base = "/opt/mfa/"
mfa_base = "/opt/montreal-forced-aligner/"
bin_dir = mfa_base+"bin/"
model_dir = mfa_base+"pretrained_models/"
in_dir = "in/"
out_dir = "out/"
dict_file = "dict.txt"
tg_dir = "tg/"
fx_dir = "fx/"
dict_cmd = "mfa_generate_dictionary"
align_cmd = "mfa_align"
kor_g2p = "korean_g2p.zip"
kor_model = "korean.zip"

def mk_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
