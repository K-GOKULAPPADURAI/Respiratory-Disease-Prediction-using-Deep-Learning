Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Admin\Desktop\respiratory disease prediction\respiratory-disease.py
Finished feature extraction from  920  files
[['Bronchiectasis' 'Bronchiolitis' 'COPD' 'Healthy' 'Pneumonia' 'URTI']
 ['16' '13' '793' '35' '37' '23']]
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 39, 861, 16)       80        
                                                                 
 max_pooling2d (MaxPooling2D  (None, 19, 430, 16)      0         
 )                                                               
                                                                 
 dropout (Dropout)           (None, 19, 430, 16)       0         
                                                                 
 conv2d_1 (Conv2D)           (None, 18, 429, 32)       2080      
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 9, 214, 32)       0         
 2D)                                                             
                                                                 
 dropout_1 (Dropout)         (None, 9, 214, 32)        0         
                                                                 
 conv2d_2 (Conv2D)           (None, 8, 213, 64)        8256      
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 4, 106, 64)       0         
 2D)                                                             
                                                                 
 dropout_2 (Dropout)         (None, 4, 106, 64)        0         
                                                                 
 conv2d_3 (Conv2D)           (None, 3, 105, 128)       32896     
                                                                 
 max_pooling2d_3 (MaxPooling  (None, 1, 52, 128)       0         
 2D)                                                             
                                                                 
 dropout_3 (Dropout)         (None, 1, 52, 128)        0         
                                                                 
 global_average_pooling2d (G  (None, 128)              0         
 lobalAveragePooling2D)                                          
                                                                 
 dense (Dense)               (None, 6)                 774       
                                                                 
=================================================================
Total params: 44,086
Trainable params: 44,086
Non-trainable params: 0
_________________________________________________________________

Pre-training accuracy: 3.8043%
Epoch 1/10

Epoch 1: val_accuracy improved from -inf to 0.02174, saving model to mymodel2_01.h5

Epoch 2/10

Epoch 2: val_accuracy improved from 0.02174 to 0.86413, saving model to mymodel2_02.h5

Epoch 3/10

Epoch 3: val_accuracy did not improve from 0.86413

Epoch 4/10

Epoch 4: val_accuracy did not improve from 0.86413

Epoch 5/10

Epoch 5: val_accuracy did not improve from 0.86413

Epoch 6/10

Epoch 6: val_accuracy did not improve from 0.86413

Epoch 7/10

Epoch 7: val_accuracy did not improve from 0.86413

Epoch 8/10

Epoch 8: val_accuracy did not improve from 0.86413

Epoch 9/10

Epoch 9: val_accuracy did not improve from 0.86413

Epoch 10/10

Epoch 10: val_accuracy did not improve from 0.86413

Training completed in time:  0:00:24.549375
Training Accuracy:  79.39972877502441
Testing Accuracy:  82.6086938381195

Epoch 1/200

Epoch 1: val_accuracy did not improve from 0.86413

Epoch 2/200

Epoch 2: val_accuracy did not improve from 0.86413

Epoch 3/200

Epoch 3: val_accuracy did not improve from 0.86413

Epoch 4/200

Epoch 4: val_accuracy did not improve from 0.86413

Epoch 5/200

Epoch 5: val_accuracy did not improve from 0.86413

Epoch 6/200

Epoch 6: val_accuracy did not improve from 0.86413

Epoch 7/200

Epoch 7: val_accuracy did not improve from 0.86413

Epoch 8/200

Epoch 8: val_accuracy did not improve from 0.86413

Epoch 9/200

Epoch 9: val_accuracy did not improve from 0.86413

Epoch 10/200

Epoch 10: val_accuracy did not improve from 0.86413

Epoch 11/200

Epoch 11: val_accuracy did not improve from 0.86413

Epoch 12/200

Epoch 12: val_accuracy did not improve from 0.86413

Epoch 13/200

Epoch 13: val_accuracy did not improve from 0.86413

Epoch 14/200

Epoch 14: val_accuracy did not improve from 0.86413

Epoch 15/200

Epoch 15: val_accuracy did not improve from 0.86413

Epoch 16/200

Epoch 16: val_accuracy did not improve from 0.86413

Epoch 17/200

Epoch 17: val_accuracy did not improve from 0.86413

Epoch 18/200

Epoch 18: val_accuracy did not improve from 0.86413

Epoch 19/200

Epoch 19: val_accuracy did not improve from 0.86413

Epoch 20/200

Epoch 20: val_accuracy did not improve from 0.86413

Epoch 21/200

Epoch 21: val_accuracy did not improve from 0.86413

Epoch 22/200

Epoch 22: val_accuracy did not improve from 0.86413

Epoch 23/200

Epoch 23: val_accuracy did not improve from 0.86413

Epoch 24/200

Epoch 24: val_accuracy did not improve from 0.86413

Epoch 25/200

Epoch 25: val_accuracy did not improve from 0.86413

Epoch 26/200

Epoch 26: val_accuracy did not improve from 0.86413

Epoch 27/200

  File "C:\Users\Admin\Desktop\respiratory disease prediction\respiratory-disease.py", line 296, in <module>
    validation_data=(x_test, y_test), callbacks=callbacks, verbose=1)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
    return fn(*args, **kwargs)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 1650, in fit
    tmp_logs = self.train_function(iterator)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\util\traceback_utils.py", line 150, in error_handler
    return fn(*args, **kwargs)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\polymorphic_function\polymorphic_function.py", line 880, in __call__
    result = self._call(*args, **kwds)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\polymorphic_function\polymorphic_function.py", line 919, in _call
    results = self._variable_creation_fn(*args, **kwds)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\polymorphic_function\tracing_compiler.py", line 135, in __call__
    filtered_flat_args, captured_inputs=concrete_function.captured_inputs)  # pylint: disable=protected-access
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\polymorphic_function\monomorphic_function.py", line 1746, in _call_flat
    ctx, args, cancellation_manager=cancellation_manager))
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\polymorphic_function\monomorphic_function.py", line 383, in call
    ctx=ctx)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\execute.py", line 53, in quick_execute
    inputs, attrs, num_outputs)
KeyboardInterrupt
>>> 
======================== RESTART: C:\Users\Admin\Desktop\respiratory disease prediction\respiratory-disease.py ========================
Finished feature extraction from  920  files
[['Bronchiectasis' 'Bronchiolitis' 'COPD' 'Healthy' 'Pneumonia' 'URTI']
 ['16' '13' '793' '35' '37' '23']]
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 39, 861, 16)       80        
                                                                 
 max_pooling2d (MaxPooling2D  (None, 19, 430, 16)      0         
 )                                                               
                                                                 
 dropout (Dropout)           (None, 19, 430, 16)       0         
                                                                 
 conv2d_1 (Conv2D)           (None, 18, 429, 32)       2080      
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 9, 214, 32)       0         
 2D)                                                             
                                                                 
 dropout_1 (Dropout)         (None, 9, 214, 32)        0         
                                                                 
 conv2d_2 (Conv2D)           (None, 8, 213, 64)        8256      
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 4, 106, 64)       0         
 2D)                                                             
                                                                 
 dropout_2 (Dropout)         (None, 4, 106, 64)        0         
                                                                 
 conv2d_3 (Conv2D)           (None, 3, 105, 128)       32896     
                                                                 
 max_pooling2d_3 (MaxPooling  (None, 1, 52, 128)       0         
 2D)                                                             
                                                                 
 dropout_3 (Dropout)         (None, 1, 52, 128)        0         
                                                                 
 global_average_pooling2d (G  (None, 128)              0         
 lobalAveragePooling2D)                                          
                                                                 
 dense (Dense)               (None, 6)                 774       
                                                                 
=================================================================
Total params: 44,086
Trainable params: 44,086
Non-trainable params: 0
_________________________________________________________________

Pre-training accuracy: 1.6304%
Epoch 1/10

Epoch 1: val_accuracy improved from -inf to 0.72283, saving model to mymodel2_01.h5

Epoch 2/10

Epoch 2: val_accuracy improved from 0.72283 to 0.86413, saving model to mymodel2_02.h5

Epoch 3/10

Epoch 3: val_accuracy did not improve from 0.86413

Epoch 4/10

Epoch 4: val_accuracy did not improve from 0.86413

Epoch 5/10

Epoch 5: val_accuracy did not improve from 0.86413

Epoch 6/10

Epoch 6: val_accuracy did not improve from 0.86413

Epoch 7/10

Epoch 7: val_accuracy did not improve from 0.86413

Epoch 8/10

Epoch 8: val_accuracy did not improve from 0.86413

Epoch 9/10

Epoch 9: val_accuracy did not improve from 0.86413

Epoch 10/10

Epoch 10: val_accuracy did not improve from 0.86413

Training completed in time:  0:00:24.482991
Training Accuracy:  66.8485701084137
Testing Accuracy:  69.021737575531

Epoch 1/10

Epoch 1: val_accuracy did not improve from 0.86413

Epoch 2/10

Epoch 2: val_accuracy did not improve from 0.86413

Epoch 3/10

Epoch 3: val_accuracy did not improve from 0.86413

Epoch 4/10

Epoch 4: val_accuracy did not improve from 0.86413

Epoch 5/10

Epoch 5: val_accuracy did not improve from 0.86413

Epoch 6/10

Epoch 6: val_accuracy did not improve from 0.86413

Epoch 7/10

Epoch 7: val_accuracy did not improve from 0.86413

Epoch 8/10

Epoch 8: val_accuracy did not improve from 0.86413

Epoch 9/10

Epoch 9: val_accuracy did not improve from 0.86413

Epoch 10/10

Epoch 10: val_accuracy did not improve from 0.86413



Warning (from warnings module):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\sklearn\metrics\_classification.py", line 1318
    _warn_prf(average, modifier, msg_start, len(result))
UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.

Warning (from warnings module):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\sklearn\metrics\_classification.py", line 1318
    _warn_prf(average, modifier, msg_start, len(result))
UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.

Warning (from warnings module):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\sklearn\metrics\_classification.py", line 1318
    _warn_prf(average, modifier, msg_start, len(result))
UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
                precision    recall  f1-score   support

Bronchiectasis       1.00      0.33      0.50         3
 Bronchiolitis       0.00      0.00      0.00         3
          COPD       0.95      0.94      0.94       159
       Healthy       0.00      0.00      0.00         7
     Pneumonia       0.12      0.43      0.19         7
          URTI       0.00      0.00      0.00         5

      accuracy                           0.83       184
     macro avg       0.35      0.28      0.27       184
  weighted avg       0.84      0.83      0.83       184

[[  1   0   2   0   0   0]
 [  0   0   1   0   2   0]
 [  0   0 149   0   8   2]
 [  0   0   0   0   7   0]
 [  0   0   4   0   3   0]
 [  0   0   1   0   4   0]]
>>> model
<keras.engine.sequential.Sequential object at 0x00000150B2B3C3C8>
>>> features
array([[[-4.25929626e+02, -4.74543427e+02, -5.26268555e+02, ...,
         -5.21922974e+02, -5.18371826e+02, -5.24104553e+02],
        [ 7.59593506e+01,  9.57673111e+01,  1.07862137e+02, ...,
          1.13700607e+02,  1.18766586e+02,  1.06290695e+02],
        [ 7.67765198e+01,  8.34067230e+01,  7.01855469e+01, ...,
          7.70387115e+01,  8.18043213e+01,  7.64635773e+01],
        ...,
        [ 3.02516103e-01,  7.77786791e-01,  3.45391810e-01, ...,
         -6.93254948e+00, -3.68614340e+00, -1.21863639e+00],
        [ 3.72309828e+00,  4.03583717e+00,  2.32282257e+00, ...,
         -2.24807978e+00, -2.22762990e+00, -9.33637738e-01],
        [ 2.72636032e+00,  3.96600580e+00,  4.09331608e+00, ...,
          3.13393116e+00, -9.88742232e-01, -4.00402451e+00]],

       [[-5.23843079e+02, -5.57566833e+02, -5.70132507e+02, ...,
         -4.97284393e+02, -4.91398682e+02, -5.07024902e+02],
        [ 6.80857086e+01,  9.42855377e+01,  1.08900223e+02, ...,
          1.78229462e+02,  1.89745941e+02,  1.70870193e+02],
        [ 6.97112885e+01,  6.79071198e+01,  6.13862648e+01, ...,
          6.72552185e+01,  8.14682465e+01,  8.44948502e+01],
        ...,
        [ 7.93595791e-01,  1.69063663e+00,  1.93637061e+00, ...,
          2.97555184e+00,  2.80524445e+00,  1.38320661e+00],
        [ 5.70877075e+00,  3.02921534e+00,  2.32096910e+00, ...,
         -2.30543375e-01,  1.13518804e-01, -1.66258466e+00],
        [ 5.59621382e+00,  1.56999946e+00,  8.22276652e-01, ...,
         -4.43165779e+00, -1.62131524e+00, -4.19453573e+00]],

       [[-4.67062286e+02, -4.74796997e+02, -5.33539612e+02, ...,
         -5.59948914e+02, -5.58220581e+02, -5.42373962e+02],
        [ 2.19346832e+02,  2.14409271e+02,  1.60924133e+02, ...,
          1.65051483e+02,  1.66153748e+02,  1.73107452e+02],
        [ 5.15500717e+01,  5.26684875e+01,  4.51723480e+01, ...,
          9.69564590e+01,  9.60886993e+01,  8.55847931e+01],
        ...,
        [ 5.43332291e+00,  5.14263201e+00,  4.27001905e+00, ...,
          2.08396769e+00,  1.47119272e+00, -5.84330082e-01],
        [ 3.02171707e+00,  3.54979134e+00,  4.02570486e+00, ...,
          2.18397045e+00,  2.40084362e+00,  3.69970703e+00],
        [ 3.54913306e+00,  3.35440493e+00,  2.66989541e+00, ...,
          9.57578659e-01,  3.04545522e+00,  4.69646072e+00]],

       ...,

       [[-5.41270874e+02, -5.44161621e+02, -5.44428772e+02, ...,
         -5.38873901e+02, -5.43086060e+02, -5.48335388e+02],
        [ 7.41401062e+01,  7.74765167e+01,  7.75629578e+01, ...,
          8.38977814e+01,  7.93003464e+01,  7.16372528e+01],
        [ 5.34874191e+01,  5.32623672e+01,  5.39372253e+01, ...,
          5.53442230e+01,  5.38246803e+01,  4.91301422e+01],
        ...,
        [-3.42850268e-01,  1.77218056e+00,  6.22304201e+00, ...,
          5.32452106e+00,  5.33961391e+00,  4.00897408e+00],
        [-1.89268148e+00,  1.51159382e+00,  6.30345201e+00, ...,
          2.60764480e+00,  2.15536618e+00,  2.54276085e+00],
        [-4.30831432e-01,  1.54389453e+00,  4.32400894e+00, ...,
          1.13124728e+00, -9.20630038e-01, -2.54349142e-01]],

       [[-4.58573120e+02, -4.96709534e+02, -5.07816956e+02, ...,
         -5.19135437e+02, -5.10667419e+02, -4.92354004e+02],
        [ 4.34720230e+01,  5.52355957e+01,  5.81193695e+01, ...,
          4.49364586e+01,  5.60589981e+01,  7.08909760e+01],
        [ 5.81432152e+01,  5.37707558e+01,  4.81697350e+01, ...,
          4.14378586e+01,  5.04584122e+01,  6.44260025e+01],
        ...,
        [-2.88646054e+00, -1.09168315e+00,  1.45189559e+00, ...,
          5.07071543e+00,  2.71075153e+00,  5.29224873e-01],
        [-1.16138351e+00, -1.37643099e+00, -2.22292125e-01, ...,
          5.57315683e+00,  3.66302824e+00,  3.11602068e+00],
        [ 4.13072109e+00,  1.73481643e+00, -8.28740478e-01, ...,
          5.38905430e+00,  5.32864189e+00,  4.76255846e+00]],

       [[-4.63947205e+02, -5.06420807e+02, -5.30272217e+02, ...,
         -4.87844055e+02, -4.94908234e+02, -5.02326721e+02],
        [ 5.94968414e+01,  7.20262756e+01,  7.27158966e+01, ...,
          1.27960289e+02,  1.21901215e+02,  1.13207626e+02],
        [ 9.67137985e+01,  7.95487366e+01,  4.92426414e+01, ...,
          9.11189346e+01,  9.17825623e+01,  8.76653366e+01],
        ...,
        [ 5.43445587e+00,  5.16458416e+00,  2.66037107e+00, ...,
          1.54472208e+00,  3.80879593e+00,  5.92417908e+00],
        [ 4.44979382e+00,  6.18138695e+00,  6.13529301e+00, ...,
          1.75754809e+00,  2.25188851e+00,  2.87845802e+00],
        [ 2.81087875e+00,  5.56319666e+00,  5.75641632e+00, ...,
          3.64545369e+00, -3.16145539e-01, -2.14443612e+00]]],
      dtype=float32)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> features[0]
array([[-4.25929626e+02, -4.74543427e+02, -5.26268555e+02, ...,
        -5.21922974e+02, -5.18371826e+02, -5.24104553e+02],
       [ 7.59593506e+01,  9.57673111e+01,  1.07862137e+02, ...,
         1.13700607e+02,  1.18766586e+02,  1.06290695e+02],
       [ 7.67765198e+01,  8.34067230e+01,  7.01855469e+01, ...,
         7.70387115e+01,  8.18043213e+01,  7.64635773e+01],
       ...,
       [ 3.02516103e-01,  7.77786791e-01,  3.45391810e-01, ...,
        -6.93254948e+00, -3.68614340e+00, -1.21863639e+00],
       [ 3.72309828e+00,  4.03583717e+00,  2.32282257e+00, ...,
        -2.24807978e+00, -2.22762990e+00, -9.33637738e-01],
       [ 2.72636032e+00,  3.96600580e+00,  4.09331608e+00, ...,
         3.13393116e+00, -9.88742232e-01, -4.00402451e+00]], dtype=float32)
>>> model
<keras.engine.sequential.Sequential object at 0x00000150B2B3C3C8>
>>> model.predict(features[0])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    model.predict(features[0])
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Temp\__autograph_generated_fileaf8plzgv.py", line 15, in tf__predict_function
    retval_ = ag__.converted_call(ag__.ld(step_function), (ag__.ld(self), ag__.ld(iterator)), None, fscope)
ValueError: in user code:

    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2137, in predict_function  *
        return step_function(self, iterator)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2123, in step_function  **
        outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2111, in run_step  **
        outputs = model.predict_step(data)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2079, in predict_step
        return self(x, training=False)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
        raise e.with_traceback(filtered_tb) from None
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\input_spec.py", line 296, in assert_input_compatibility
        f'Input {input_index} of layer "{layer_name}" is '

    ValueError: Input 0 of layer "sequential" is incompatible with the layer: expected shape=(None, 40, 862, 1), found shape=(None, 862)

>>> features[0].shape
(40, 862)
>>> features[0][0].shape
(862,)
>>> features.shape
(920, 40, 862)
>>> model.predict(features)

array([[0.4078127 , 0.00282191, 0.13897394, 0.0089603 , 0.28684512,
        0.15458606],
       [0.40426606, 0.00647673, 0.11705599, 0.016038  , 0.37072113,
        0.08544216],
       [0.42276993, 0.00464415, 0.14508007, 0.009912  , 0.33064893,
        0.08694487],
       ...,
       [0.39288533, 0.00896468, 0.13463864, 0.02007602, 0.34003273,
        0.1034026 ],
       [0.3623898 , 0.00830106, 0.129323  , 0.0246962 , 0.37518653,
        0.10010346],
       [0.3638835 , 0.00732298, 0.11790882, 0.02370702, 0.38074946,
        0.10642824]], dtype=float32)
>>> model.predict(features[0])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    model.predict(features[0])
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\execute.py", line 53, in quick_execute
    inputs, attrs, num_outputs)
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node 'sequential/conv2d/Relu' defined at (most recent call last):
    File "<string>", line 1, in <module>
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 155, in main
      ret = method(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 550, in runcode
      exec(code, self.locals)
    File "<pyshell#15>", line 1, in <module>
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2350, in predict
      tmp_batch_outputs = self.predict_function(iterator)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2137, in predict_function
      return step_function(self, iterator)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2123, in step_function
      outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2111, in run_step
      outputs = model.predict_step(data)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2079, in predict_step
      return self(x, training=False)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 561, in __call__
      return super().__call__(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\base_layer.py", line 1132, in __call__
      outputs = call_fn(inputs, *args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 96, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\sequential.py", line 413, in call
      return super().call(inputs, training=training, mask=mask)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\functional.py", line 511, in call
      return self._run_internal_graph(inputs, training=training, mask=mask)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\functional.py", line 668, in _run_internal_graph
      outputs = node.layer(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\base_layer.py", line 1132, in __call__
      outputs = call_fn(inputs, *args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 96, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\layers\convolutional\base_conv.py", line 314, in call
      return self.activation(outputs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\activations.py", line 318, in relu
      x, alpha=alpha, max_value=max_value, threshold=threshold
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\backend.py", line 5369, in relu
      x = tf.nn.relu(x)
Node: 'sequential/conv2d/Relu'
convolution input must be 4-dimensional: [32,862]
	 [[{{node sequential/conv2d/Relu}}]] [Op:__inference_predict_function_5992]
>>> model.predict([features[0]])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    model.predict([features[0]])
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Temp\__autograph_generated_fileaf8plzgv.py", line 15, in tf__predict_function
    retval_ = ag__.converted_call(ag__.ld(step_function), (ag__.ld(self), ag__.ld(iterator)), None, fscope)
ValueError: in user code:

    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2137, in predict_function  *
        return step_function(self, iterator)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2123, in step_function  **
        outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2111, in run_step  **
        outputs = model.predict_step(data)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2079, in predict_step
        return self(x, training=False)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
        raise e.with_traceback(filtered_tb) from None
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\input_spec.py", line 296, in assert_input_compatibility
        f'Input {input_index} of layer "{layer_name}" is '

    ValueError: Input 0 of layer "sequential" is incompatible with the layer: expected shape=(None, 40, 862, 1), found shape=(None, 862)

>>> model.predict(np.array([features[0]]))

array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]], dtype=float32)
>>> model.predict(np.array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]], dtype=float32)
)
Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    0.15458609]], dtype=float32)
NameError: name 'float32' is not defined
>>> model.predict(np.array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]]))
Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    0.15458609]]))
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\execute.py", line 53, in quick_execute
    inputs, attrs, num_outputs)
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node 'sequential/conv2d/Relu' defined at (most recent call last):
    File "<string>", line 1, in <module>
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 155, in main
      ret = method(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 550, in runcode
      exec(code, self.locals)
    File "<pyshell#15>", line 1, in <module>
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2350, in predict
      tmp_batch_outputs = self.predict_function(iterator)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2137, in predict_function
      return step_function(self, iterator)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2123, in step_function
      outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2111, in run_step
      outputs = model.predict_step(data)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2079, in predict_step
      return self(x, training=False)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 561, in __call__
      return super().__call__(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\base_layer.py", line 1132, in __call__
      outputs = call_fn(inputs, *args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 96, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\sequential.py", line 413, in call
      return super().call(inputs, training=training, mask=mask)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\functional.py", line 511, in call
      return self._run_internal_graph(inputs, training=training, mask=mask)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\functional.py", line 668, in _run_internal_graph
      outputs = node.layer(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\base_layer.py", line 1132, in __call__
      outputs = call_fn(inputs, *args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 96, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\layers\convolutional\base_conv.py", line 314, in call
      return self.activation(outputs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\activations.py", line 318, in relu
      x, alpha=alpha, max_value=max_value, threshold=threshold
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\backend.py", line 5369, in relu
      x = tf.nn.relu(x)
Node: 'sequential/conv2d/Relu'
convolution input must be 4-dimensional: [1,6]
	 [[{{node sequential/conv2d/Relu}}]] [Op:__inference_predict_function_5992]
>>> model.predict(np.array([features[0]]))

array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]], dtype=float32)
>>> model.predict(np.array([features[0][0]]))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    model.predict(np.array([features[0][0]]))
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow\python\eager\execute.py", line 53, in quick_execute
    inputs, attrs, num_outputs)
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node 'sequential/conv2d/Relu' defined at (most recent call last):
    File "<string>", line 1, in <module>
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 155, in main
      ret = method(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 550, in runcode
      exec(code, self.locals)
    File "<pyshell#15>", line 1, in <module>
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2350, in predict
      tmp_batch_outputs = self.predict_function(iterator)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2137, in predict_function
      return step_function(self, iterator)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2123, in step_function
      outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2111, in run_step
      outputs = model.predict_step(data)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 2079, in predict_step
      return self(x, training=False)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\training.py", line 561, in __call__
      return super().__call__(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\base_layer.py", line 1132, in __call__
      outputs = call_fn(inputs, *args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 96, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\sequential.py", line 413, in call
      return super().call(inputs, training=training, mask=mask)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\functional.py", line 511, in call
      return self._run_internal_graph(inputs, training=training, mask=mask)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\functional.py", line 668, in _run_internal_graph
      outputs = node.layer(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\engine\base_layer.py", line 1132, in __call__
      outputs = call_fn(inputs, *args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\utils\traceback_utils.py", line 96, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\layers\convolutional\base_conv.py", line 314, in call
      return self.activation(outputs)
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\activations.py", line 318, in relu
      x, alpha=alpha, max_value=max_value, threshold=threshold
    File "C:\Users\Admin\AppData\Local\Programs\Python\Python37\lib\site-packages\keras\backend.py", line 5369, in relu
      x = tf.nn.relu(x)
Node: 'sequential/conv2d/Relu'
convolution input must be 4-dimensional: [1,862]
	 [[{{node sequential/conv2d/Relu}}]] [Op:__inference_predict_function_5992]
>>> model.predict(np.array([features[0]]))

array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]], dtype=float32)
>>> model.predict(np.array([features[1]]))

array([[0.40426624, 0.00647673, 0.11705601, 0.01603799, 0.37072092,
        0.0854421 ]], dtype=float32)
>>> lables
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lables
NameError: name 'lables' is not defined
>>> labels
array(['URTI', 'URTI', 'Healthy', 'Asthma', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'URTI', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'LRTI', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Bronchiectasis',
       'Bronchiectasis', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'LRTI', 'Bronchiectasis', 'Bronchiectasis', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'URTI',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Healthy', 'Healthy',
       'Pneumonia', 'Pneumonia', 'Pneumonia', 'Pneumonia', 'Pneumonia',
       'Pneumonia', 'Pneumonia', 'Pneumonia', 'Pneumonia', 'Healthy',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Healthy',
       'Healthy', 'Healthy', 'COPD', 'URTI', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'URTI',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'Pneumonia', 'Pneumonia', 'Pneumonia', 'Pneumonia',
       'Pneumonia', 'Pneumonia', 'Pneumonia', 'Pneumonia', 'Pneumonia',
       'Pneumonia', 'Pneumonia', 'Pneumonia', 'Pneumonia', 'Healthy',
       'URTI', 'URTI', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'Pneumonia', 'Pneumonia', 'Pneumonia',
       'Pneumonia', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'Healthy', 'Healthy', 'Healthy', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'URTI', 'Bronchiolitis', 'Bronchiolitis', 'Bronchiolitis',
       'URTI', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Healthy', 'Healthy',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Healthy',
       'Healthy', 'Healthy', 'Healthy', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'Bronchiolitis', 'Bronchiolitis', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'URTI', 'URTI', 'URTI', 'URTI',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Bronchiolitis',
       'Bronchiolitis', 'Bronchiectasis', 'Bronchiectasis',
       'Bronchiectasis', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'Healthy', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'Bronchiolitis', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Healthy', 'Healthy',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'Healthy', 'Healthy', 'Healthy', 'Healthy', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'Healthy', 'URTI', 'URTI', 'URTI',
       'URTI', 'COPD', 'URTI', 'Pneumonia', 'Pneumonia', 'Pneumonia',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'Healthy', 'Healthy', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Bronchiectasis', 'URTI',
       'URTI', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'Bronchiectasis', 'Bronchiectasis', 'Bronchiectasis',
       'Bronchiectasis', 'Bronchiectasis', 'Bronchiectasis', 'Healthy',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'Bronchiolitis', 'Bronchiolitis', 'Bronchiolitis',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Healthy', 'Healthy',
       'URTI', 'URTI', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'Healthy',
       'Bronchiectasis', 'Bronchiectasis', 'Bronchiolitis',
       'Bronchiolitis', 'Healthy', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'Pneumonia', 'Pneumonia', 'Pneumonia',
       'Pneumonia', 'Pneumonia', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD', 'COPD',
       'COPD', 'COPD', 'Healthy', 'Healthy', 'Healthy', 'Pneumonia',
       'Pneumonia', 'Pneumonia'], dtype='<U14')
>>> set(labels)
{'Bronchiectasis', 'Healthy', 'Asthma', 'LRTI', 'URTI', 'COPD', 'Pneumonia', 'Bronchiolitis'}
>>> model.predict(np.array([features[0]]))

array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]], dtype=float32)
>>> len(model.predict(np.array([features[0]])))

1
>>> model.predict(np.array([features[0]]))

array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]], dtype=float32)
>>> print(len(array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]], dtype=float32)))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(len(array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
NameError: name 'array' is not defined
>>> print(len(np.array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]], dtype=float32)))
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    0.15458609]], dtype=float32)))
NameError: name 'float32' is not defined
>>> print(len(np.array([[0.40781286, 0.00282191, 0.13897392, 0.0089603 , 0.28684494,
        0.15458609]])))
1
>>> max_pooling2d_2 (MaxPooling  (None, 4, 106, 64)       0
		 
SyntaxError: invalid syntax
>>> 
>>> 
>>> model.predict(np.array([features[11]]))

array([[0.34432802, 0.00814287, 0.38072217, 0.00841277, 0.18814225,
        0.07025192]], dtype=float32)
>>> model.predict(np.array([features[11]]))

array([[0.34432802, 0.00814287, 0.38072217, 0.00841277, 0.18814225,
        0.07025192]], dtype=float32)
>>> 0.34432802<0.38072217
True
>>> 