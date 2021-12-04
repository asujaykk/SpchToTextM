#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 12:55:30 2021

@author: akhil_kk
"""
 
import speech_recognition as SpchToText
 
# Initialize the recognizer 

      
class SRModule():
     
     
    def __init__(self):
        self.Recognizer = SpchToText.Recognizer()
        self.setMic() 
        
    def getMicList(self):
        self.miclist=[]
        for index, name in enumerate(SpchToText.Microphone.list_microphone_names()):
            #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
            self.miclist.append(name)
        return self.miclist    
    def setMic(self,mic_index=0):
        self.mic=SpchToText.Microphone(mic_index)
        
    def getAudio(self,):
        with self.mic:
            audio = self.Recognizer.listen(self.mic)
            return audio 
 
    def getTextFromAudio(self,audio_object):
        try:
            MyText = self.Recognizer.recognize_google(audio_object)
            return MyText.lower() 
        except SpchToText.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None
        except SpchToText.UnknownValueError:
            print("unknown error occured")
            return None
        
    def adjustNoise(self,duration=0.5):
        with self.mic:
            self.Recognizer.adjust_for_ambient_noise(self.mic, duration=duration)
