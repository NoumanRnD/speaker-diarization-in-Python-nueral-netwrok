 
import os
import numpy
import bob.bio.spear.extractor.Cepstral


def controller_Main(processed_Data):
     
    controller = bob.bio.spear.extractor.Cepstral(
            win_length_ms=20,
            win_shift_ms=10,
            n_filters=24,
            dct_norm=False,
            f_min=0.0,
            f_max=4000,
            delta_win=2,
            mel_scale=True,  
            with_energy=True,
            with_delta=True,
            with_delta_delta=True,
            n_ceps=19,   
            pre_emphasis_coef=0.95,
            features_mask=numpy.arange(0, 60),
            normalize_flag=True,
    )
    return controller(processed_Data)
