import time
from chapter6.aituiber_system import AITuberSystem
import traceback

aituiber_system = AITuberSystem()
while True:
  try:
    aituiber_system.talk_with_comment()
    time.sleep(5)
  except Exception as e:
    print("エラーが発生しました")
    print(traceback.format_exc())
    print(e)
    exit(200)
