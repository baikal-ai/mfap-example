***

*  **Montreal-Forced-Aligner**

Downloads (v1.0.1):

Linux: https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.0.1/montreal-forced-aligner_linux.tar.gz

MacOS: https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.0.1/montreal-forced-aligner_macosx.zip

Win64: https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.0.1/montreal-forced-aligner_win64.zip

Source: https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner

Pre-trained models: https://github.com/MontrealCorpusTools/mfa-models

*  **Praat**

MacOS: http://www.fon.hum.uva.nl/praat/praat6106_mac64.dmg

Linux: sudo apt-get install praat (for Ubuntu) OR http://www.fon.hum.uva.nl/praat/download_linux.html

Win64: http://www.fon.hum.uva.nl/praat/praat6106_win64.zip

*  **exmple:**

> Montreal-Forced-Aligner, Praat을 사용하여 음성 데이터에서 formant 추출하는 프로그램과 사용예 

```
aligner.py           : Montreal-Forced-Aligner로 음성과 문자 정렬 
conf.py              : 실행 환경 변수 정의
extract_formants.scr : Formant 추출 Praat Script(부분)
formants.py          : Praat로 Formant 데이터 추출 
in                   : input dir. 같은 이름의 .wav/.txt(or lab) 파일들이 각 1쌍으로 있어야 함
out                  : output dir.
```
