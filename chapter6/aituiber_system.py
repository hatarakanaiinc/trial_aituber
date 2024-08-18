from chapter3.openai_adapter import OpenaiAdapter
from chapter5.obs_adapter import OBSAdapter
from chapter5.youtube_comment_adapter import YoutubeCommentAdapter
from chapter4_2.voicebox_adapter import VoiceBoxAdapter
from chapter4_2.play_sound import PlaySound

from dotenv import load_dotenv
load_dotenv()
import os

class AITuberSystem:
  def __init__(self) -> None:
    video_id = os.getenv("YOUTUBE_VIDEO_ID")
    self.youtube_comment_adapter = YoutubeCommentAdapter(video_id)
    self.openai_adapter = OpenaiAdapter()
    self.voicebox_adapter = VoiceBoxAdapter()
    self.obs_adapter = OBSAdapter()
    # self.play_sound = PlaySound(output_device_name = "Headphones (High Definition Aud")
    self.play_sound = PlaySound(output_device_name = "CABLE Input")
    pass

  def talk_with_comment(self) -> bool:
    print("コメントを読み込みます・・・")
    comment = self.youtube_comment_adapter.get_comment()

    if comment==None:
      print("コメントがありませんでした")
      return

    response_text = self.openai_adapter._create_chat(comment)
    data, rate = self.voicebox_adapter.get_voice(response_text)
    self.obs_adapter.set_question(comment)
    self.obs_adapter.set_answer(response_text)
    self.play_sound.play_sound(data, rate)
    return True
