
import librosa



def audio_basic_process(audio_path):
    sound_sample1,sr=librosa.load(audio_path ,mono=True)

    return {"sound_sample1":len(sound_sample1),"sr":sr}




