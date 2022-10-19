import requests
import IPython as IP

class Speaker:
    voicevox_url = "http://voicevox:50021"
    speakers = {}

    def __init__(
        self,
        speaker_id=None,
        text=None,
        audio_query=None,
    ):
        self.speaker_id = speaker_id
        self.text = text
        self.audio_query = audio_query
        if self.text is not None and self.audio_query is None:
            self.set_audio_query_from_text(self.text)

        self.voice = None
        self.is_voise_updated = False

    @classmethod
    def get_speakers(cls):
        endpoint = Speaker.voicevox_url + "/speakers"
        response = requests.get(endpoint)
        response.encoding = response.apparent_encoding
        Speaker.speakers = response.json()
        return Speaker.speakers

    def set_audio_query_from_text(self, text):
        self.text = text
        endpoint = Speaker.voicevox_url + "/audio_query"
        response = requests.post(
            url=endpoint,
            params={
                "text": self.text,
                "speaker": self.speaker_id,
            },
        )
        response.encoding = response.apparent_encoding
        self.is_voise_updated = False
        self.audio_query = response.json()

    def get_voice(self):
        # クエリの更新が合った場合のみ新規取得を行う
        if not self.is_voise_updated:
            endpoint = Speaker.voicevox_url + "/synthesis"
            response = requests.post(
                url=endpoint,
                params={
                    "speaker": self.speaker_id,
                },
                json=self.audio_query,
            )
            self.voice = response.content
            self.is_voise_updated = True
        return self.voice

    def speak_at_jupyter(self):
        if self.voice is None:
            self.get_voice()
        IP.display.display(IP.display.Audio(self.voice, rate=48000, autoplay=True))

if __name__ == "__main__":
    speakers = Speaker(
        speaker_id=2,
        text="こちふかば においおこせよ うめのはな あるじなしとて はるをわするな",
    )

    speakers.speak_at_jupyter()
