from voicebox_adapter import VoiceBoxAdapter
from play_sound import PlaySound

input_str = "いらっしゃいませ"
voicebox_adapter = VoiceBoxAdapter()
play_sound = PlaySound("Headphones (High Definition Aud")
data, rate = voicebox_adapter._get_voice(input_str)
play_sound.play_sound(data, rate)
