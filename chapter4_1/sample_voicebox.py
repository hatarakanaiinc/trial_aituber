import requests
import json

url = "http://localhost:50021/"
text = "こんにちわ"
# もち子さん(ノーマル)
speaker_id = 20
item_data = {
  "text": text,
  "speaker": speaker_id
}

res = requests.post(url + 'audio_query', params = item_data)
res_json = res.json()
query_data = res_json
a_params = {
  "speaker": speaker_id
}
res = requests.post(url + 'synthesis', params = a_params, data = json.dumps(query_data))
print(res.content)
