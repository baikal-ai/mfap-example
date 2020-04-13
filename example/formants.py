# coding=utf-8
# formants.py

import os
import sys
import subprocess as sp
import conf

def make_script(speaker_info, w_path, tg_path, o_path):
    
    f = open('extract_formants.scr', mode = 'r')
    raw_script = f.readlines()
    f.close()
    
    script = ''
    script += 'outputPath$ = "'+o_path + speaker_info + '.csv"\n'
    script += 'w_path$ = "'+w_path + '"\n'
    script += 'tg_path$ = "'+tg_path + '"\n'
    script += 'do ("Read from file...", "\'w_path$\'" + "' + speaker_info + '.wav")\n'
    script += 'thisSound$ = selected$("Sound")\n'
    script += 'do ("Read from file...", "\'tg_path$\'" + "' + speaker_info + '.TextGrid")\n'
    script += 'thisTextGrid$ = selected$("TextGrid")\n'

    for l in range(len(raw_script)):
        if len(raw_script[l]) != 1:
            script += raw_script[l]
    
    return script

def run_script(praat_path, script_path, *args):

    if praat_path == '':
        if sys.platform == 'linux':
            praat_path = '/usr/bin/praat'
        elif sys.platform == 'darwin':
            praat_path = '/Applications/Praat.app/Contents/MacOS/Praat'

    com = [praat_path]
    if sys.platform == 'win32':
        com += ['-a']
        
    com += ['--run']
    com += [script_path] + list(map(str, args))
    text = script_path

    sp.call(com)
    return text

def extract():
    cur_path = os.getcwd()
    input_path = os.path.join(cur_path, conf.in_dir)
    speakers = [file.split('.')[-2] for file in os.listdir(input_path)]

    for speaker in speakers:
        script_file = speaker+'.praat'
        w_path = os.path.join(cur_path, conf.in_dir)
        tg_path = os.path.join(cur_path, conf.out_dir+conf.in_dir)
        o_path = os.path.join(cur_path, conf.out_dir+conf.fx_dir)

        conf.mk_dir(o_path)
        script = make_script(speaker, w_path, tg_path, o_path)

        scr_path = os.path.join(cur_path, script_file)
        f = open(scr_path, 'w')
        f.write(script)
        f.close()

        run_script('', scr_path)
        os.remove(scr_path)

if __name__ == "__main__":
    extract()
