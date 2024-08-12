import json
import requests
import io
import soundfile

class VoiceBoxAdapter:
  URL = 'http://localhost:50021/'

  # 1回目：変換。2回目：音声合成
  def __init__(self) -> None:
    pass

  def _creaate_audio_query(self, text: str, speaker_id: int) -> json:
    item_data = {
      "text": text,
      "speaker": speaker_id
    }

    response = requests.post(self.URL + 'audio_query', params = item_data)
    return response.json()

  def _creaate_request_audio(self, query_data, speaker_id: int) -> bytes:
    a_params = {
      "speaker": speaker_id
    }
    headers = {
      "accept": "audio/wav",
      "ContentType": "application/json",
    }
    res = requests.post(self.URL + 'synthesis', params = a_params, data = json.dumps(query_data), headers = headers)
    print(res.status_code)
    return res.content

  def _get_voice(self, text: str):
    speaker_id = 20
    query_data:json = self._creaate_audio_query(text, speaker_id = speaker_id)
    audio_bytes = self._creaate_request_audio(query_data, speaker_id = speaker_id)
    audio_stream = io.BytesIO(audio_bytes)
    data, sample_rate = soundfile.read(audio_stream)
    return data, sample_rate


if __name__ == "__main__":
  voicebox = VoiceboxAdapter()
  data, sample_rate = voicebox._get_voice("こんにちわ")
  print(sample_rate)
