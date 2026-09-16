from pycaw.pycaw import AudioUtilities

speakers = AudioUtilities.GetSpeakers()
volume = speakers.EndpointVolume

volume.SetMasterVolumeLevelScalar(0.5, None)
