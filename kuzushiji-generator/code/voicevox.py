import requests
import json


class Speaker:
    voicevox_url = "http://voicevox:50021"
    speakers = {}

    def __init__(
        self,
        speaker_id = None,
        text=None,
        audio_query=None,
    ):
        self.text = text
        self.set_audio_query(audio_query)
        self.audio_query = {}
        self.speaker_id = speaker_id
        self.voice = None
        self.is_voise_updated = False

    @classmethod
    def get_speakers(cls):
        endpoint = Speaker.voicevox_url + "/speakers"
        response = requests.get(endpoint)
        response.encoding = response.apparent_encoding
        Speaker.speakers = response.json()
        return Speaker.speakers

    def set_audio_query_from_text(
        self,
        text
    ):
        self.text = text
        endpoint = Speaker.voicevox_url + "/audio_query"
        response = requests.get(endpoint)
        response.encoding = response.apparent_encoding
        self.is_voise_updated = False
        self.audio_query = response.json()
    
    def get_voice(self):
        # クエリの更新が合った場合のみ新規取得を行う
        if not self.is_voise_updated:
            endpoint = Speaker.voicevox_url + "/synthesis"
            self.voice = requests.get(endpoint)
            self.is_voise_updated = True
        return self.voice


if __name__ == "__main__":
    speakers = Speaker.get_speakers()
    print(json.dumps(speakers, indent=2, ensure_ascii=False))
    speaker = Speaker()
