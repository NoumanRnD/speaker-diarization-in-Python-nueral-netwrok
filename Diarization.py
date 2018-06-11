 
import bob.bio.spear.preprocessor


def _load_Setting():
    
    return bob.bio.spear.preprocessor.Energy_2Gauss(
        max_iterations=10,
        convergence_threshold=0.0005,
        variance_threshold=0.0005,
        win_length_ms=20.,
        win_shift_ms=10.,
        smoothing_window=10
    )


def speaker(preprocessed_data):     
    preprocessor = _load_Setting()
    return preprocessor(preprocessed_data)
