import io
import requests
import wave
import simpleaudio as sa

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


if __name__ == "__main__":
    speakers = Speaker(
        speaker_id=2,
        text="こんにちは",
    )

    with wave.open(io.BytesIO(speakers.get_voice()), "rb") as wave:
        wave_obj = sa.WaveObject.from_wave_read(wave)
        play_obj = wave_obj.play()
        play_obj.wait_done()
