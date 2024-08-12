import sounddevice as sd

f = open('chapter4_1/sound_device.txt', 'w', encoding = 'utf-8')
f.write(str(sd.query_devices()))
f.close()
