# coding=utf-8
# batch.py

import subprocess as sp
import conf

dict_args = [conf.bin_dir+conf.dict_cmd,
        conf.model_dir+conf.kor_g2p,
        conf.in_dir,
        conf.dict_file]

align_args = [conf.bin_dir+conf.align_cmd,
         conf.in_dir,
         conf.dict_file,
         conf.model_dir+conf.kor_model,
         conf.out_dir]

# 입력문장을 소리로 변환
def dict():
    # print(dict_args)
    print("mfa_generate_dictionary")
    sp.call(dict_args)

# TextGrid 변환 
def align():
    # print(align_args)
    print("mfa_align")
    conf.mk_dir(conf.out_dir)
    sp.call(align_args)

if __name__ == "__main__":
    dict()
    align()
