# coding=utf-8

import dashscope
from dashscope.audio.tts import SpeechSynthesizer

dashscope.api_key='sk-ede96ec3834f4f1cac053febe2d470e9'

result = SpeechSynthesizer.call(model='sambert-zhichu-v1',
                                text='今天天气怎么样',
                                sample_rate=48000)
if result.get_audio_data() is not None:
    with open('output.wav', 'wb') as f:
        f.write(result.get_audio_data())