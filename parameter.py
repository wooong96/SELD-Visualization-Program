# 특징 추출, 신경망 모델 및 SELDnet 훈련에 사용되는 매개 변수는 여기에서 변경할 수 있습니다.
#
# 이상적으로는 기본 매개 변수의 값을 변경하지 마십시오. 다음과 같이 고유 한 <task-id>로 별도의 사례를 만듭니다.
# 아래 코드 (if-else 루프)를 사용하여 사용합니다. 이렇게하면 나중에 구성을 쉽게 재현 할 수 있습니다.


def get_params(argv='1'):
    print("SET: {}".format(argv))
    # ########### 기본 매개 변수 #############
    params = dict(
        quick_test=False,   # 빠른 테스트를 수행합니다. 데이터 세트의 작은 하위 집합 및 Epoch 수에 대한 학습 / 테스트


        # INPUT PATH
        dataset_dir='C:\\Users\\TSP\\Desktop\\seld-dcase2020\\base_folder', # foa/mic 와 메타데이터가 포함된 base folder

        # OUTPUT PATH
        feat_label_dir='C:\\Users\\TSP\\Desktop\\seld-dcase2020\\base_folder\\make_data_test\\feat_label',  # 추출된 features와 labels을 덤프시키는 디렉토리
        model_dir='C:\\Users\\TSP\\Desktop\\seld-dcase2020\\base_folder\\make_data_test\\models',   # 이 폴더에 훈련 된 모델과 훈련 곡선을 덤프
        dcase_output=True,     # true 인 경우 'dcase_dir'경로에 기록 방식으로 결과를 덤프
                               # 이 폴더에 기록 방식의 네트워크 출력을 덤프합니다.
        dcase_dir='C:\\Users\\TSP\\Desktop\\seld-dcase2020\\base_folder\\make_data_test\\results',  #이 폴더에 기록 방식의 네트워크 출력을 덤프합니다.

        # DATASET LOADING PARAMETERS
        mode='eval',         # 'dev' - development or 'eval' - evaluation 데이터세트
        dataset='mic',       # 'foa' - ambisonic or 'mic' - microphone signals

        #FEATURE PARAMS
        fs=24000,
        hop_len_s=0.02,
        label_hop_len_s=0.1,
        max_audio_len_s=60,
        nb_mel_bins=64,

        # DNN MODEL PARAMETERS
        label_sequence_length=60,        # Feature sequence length
        batch_size=128,              # Batch 사이즈
        dropout_rate=0,             # Dropout rate, constant for all layers
        nb_cnn2d_filt=64,           # Number of CNN nodes, constant for each layer
        f_pool_size=[4, 4, 2],      # CNN frequency pooling, length of list = number of CNN layers, list value = pooling per layer

        rnn_size=[128, 128],        # RNN contents, length of list = number of layers, list value = number of nodes
        fnn_size=[128],             # FNN contents, length of list = number of layers, list value = number of nodes
        loss_weights=[1., 1000.],     # [sed, doa] weight for scaling the DNN outputs
        nb_epochs=75,               # Train for maximum epochs
        epochs_per_fit=5,           # Number of epochs per fit
        doa_objective='masked_mse',     # supports: mse, masked_mse. mse- original seld approach; masked_mse - dcase 2020 approach
        
        #METRIC PARAMETERS
        lad_doa_thresh=20
       
    )
    feature_label_resolution = int(params['label_hop_len_s'] // params['hop_len_s'])
    params['feature_sequence_length'] = params['label_sequence_length'] * feature_label_resolution
    params['t_pool_size'] = [feature_label_resolution, 1, 1]     # CNN time pooling
    params['patience'] = int(params['nb_epochs'])     # patience 도달시 훈련 종료

    params['unique_classes'] = {
            'alarm': 0,
            'baby': 1,
            'crash': 2,
            'dog': 3,
            'engine': 4,
            'female_scream': 5,
            'female_speech': 6,
            'fire': 7,
            'footsteps': 8,
            'knock': 9,
            'male_scream': 10,
            'male_speech': 11,
            'phone': 12,
            'piano': 13
        }


    # ########### 사용자 정의 파라미터 ##############
    if argv == '1':
        print("USING DEFAULT PARAMETERS\n")

    elif argv == '2':
        params['mode'] = 'dev'
        params['dataset'] = 'mic'

    elif argv == '3':
        params['mode'] = 'eval'
        params['dataset'] = 'mic'

    elif argv == '4':
        params['mode'] = 'dev'
        params['dataset'] = 'foa'

    elif argv == '5':
        params['mode'] = 'eval'
        params['dataset'] = 'foa'

    elif argv == '999':
        print("QUICK TEST MODE\n")
        params['quick_test'] = True
        params['epochs_per_fit'] = 1

    else:
        print('ERROR: unknown argument {}'.format(argv))
        exit()

    for key, value in params.items():
        print("\t{}: {}".format(key, value))
    return params
