import tensorflow as tf

class GradientReversal(tf.keras.layers.Layer):
    def __init__(self, lambda_=1.0):
        super().__init__()
        self.lambda_ = lambda_

    def call(self, x):
        @tf.custom_gradient
        def _grl(x):
            def grad(dy):
                return -self.lambda_ * dy
            return x, grad
        return _grl(x)

def inception_module(input_tensor, stride=1, activation='linear', nb_filters=32, use_residual=True, use_bottleneck=True, bottleneck_size=32, depth=6, kernel_size=41):
    if use_bottleneck and int(input_tensor.shape[-1]) > bottleneck_size:
        input_inception = tf.keras.layers.Conv1D(filters=bottleneck_size, kernel_size=1,
                          padding='same', activation=activation, use_bias=False)(input_tensor)
    else:
        input_inception = input_tensor

    # kernel_size_s = [3, 5, 8, 11, 17]
    kernel_size_s = [kernel_size // (2 ** i) for i in range(3)]

    conv_list = []

    for i in range(len(kernel_size_s)):
        conv_list.append(tf.keras.layers.Conv1D(filters=nb_filters, kernel_size=kernel_size_s[i],
                         strides=stride, padding='same', activation=activation, use_bias=False)(
        input_inception))

    max_pool_1 = tf.keras.layers.MaxPool1D(pool_size=3, strides=stride, padding='same')(input_tensor)

    conv_6 = tf.keras.layers.Conv1D(filters=nb_filters, kernel_size=1,
                     padding='same', activation=activation, use_bias=False)(max_pool_1)

    conv_list.append(conv_6)

    x = tf.keras.layers.Concatenate(axis=2)(conv_list)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation(activation='relu')(x)
    return x


def shortcut_layer(input_tensor, output_tensor):
    shortcut_y = tf.keras.layers.Conv1D(filters=int(output_tensor.shape[-1]), kernel_size=1, padding='same', use_bias=False)(input_tensor)
    shortcut_y = tf.keras.layers.BatchNormalization()(shortcut_y)    
    
    x = tf.keras.layers.Add()([shortcut_y, output_tensor])
    x = tf.keras.layers.Activation('relu')(x)
    
    return x


def get_model(n_classes=32, input_shape=(None, 1), reduce=[tf.keras.layers.GlobalAveragePooling1D()],
              nb_filters=32, use_residual=True, use_bottleneck=True, depth=6, kernel_size=41):
    input_layer = tf.keras.layers.Input(input_shape)
    
    x = input_layer
    input_res = input_layer    
    
    for d in range(depth):    
        x = inception_module(x, nb_filters=32, use_residual=True, use_bottleneck=True, depth=6, kernel_size=41)
        if use_residual and d % 3 == 2:
            x = shortcut_layer(input_res, x)
            input_res = x

    reduced_outputs = [reduce_fn(x) for reduce_fn in reduce]
    if len(reduced_outputs) > 1:
        concatenated = tf.keras.layers.Concatenate()(reduced_outputs)
    else:
        concatenated = reduced_outputs[0]

    person_out = tf.keras.layers.Dense(units=n_classes, activation='softmax')(concatenated)
    
    grl = GradientReversal(lambda_=0.5)
    shoe_out = tf.keras.layers.Dense(4, activation="softmax")(grl(concatenated))
    speed_out = tf.keras.layers.Dense(4, activation="softmax")(grl(concatenated))
    
    model = tf.keras.models.Model(inputs=input_layer, outputs=[person_out, shoe_out, speed_out])

    return model
