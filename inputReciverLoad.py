 
import os
import bob


def input_wav_file(file_name):    
    file_path =  'wav/'+file_name
    Base_Processor = bob.bio.spear.preprocessor.Base()
    return Base_Processor.read_original_data(file_path)
