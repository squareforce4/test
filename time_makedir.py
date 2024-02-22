import datetime
import time
import subprocess
import pytz

# JSTタイムゾーンを設定する
JST = pytz.timezone('Asia/Tokyo')

# 実行する時間を設定する（例：毎日 　  の1午後15時）
target_time = datetime.time(hour=0, minute=0, second=0)
print("target", target_time)

while True:
    # 現在の時刻を取得する  0
    now = datetime.datetime.now(JST).time()
    print("now", now)

    # 実行する時間になったらスクリプトを実行する
    if now >= target_time:
        subprocess.run(['python', 'makedir.py'])
        #  待つ
        time.sleep(24 * 60 * 60)
    else:
        time.sleep(60)
