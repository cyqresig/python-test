from paddlespeech.cli.asr.infer import ASRExecutor
asr = ASRExecutor()
print('asr -> ')
result = asr(audio_file="temp/audio/zh.wav")
print('result = ')
print(result)