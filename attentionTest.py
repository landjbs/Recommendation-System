import numpy as np
import keras

def make_train_vec(length=20):
    trainVec =  np.random.uniform(-10, 10, size=length)
    trainVec[1] = 1
    return trainVec

def make_target_vec(length=20):
    targetVec = np.zeros(shape=(length))
    targetVec[1] = 1
    return targetVec

features = [make_train_vec() for _ in range(1000)]
targets = [1.0 for vec in features]
print(targets)

featureArray = np.asarray(features)
targetArray = np.asarray(targets)

print(featureArray.shape)
print(targetArray.shape)

inputs = keras.layers.Input(shape=(20,))
attentionProbs = keras.layers.Dense(units=20, activation='softmax')(inputs)
attentionMul = keras.layers.Multiply()([inputs, attentionProbs])
activation = keras.layers.Dense(units=1, activation='softmax')(attentionMul)

model = keras.models.Model(inputs=inputs, outputs=activation)
model.compile(optimizer='adam', loss='binary_crossentropy')
print(model.summary())
model.fit(featureArray, targetArray, epochs=10)

print(model.summary())
# print(f'Weights: {attentionMul.get_weights()}')
# attention_vector = keras.layers.get_activations(model, testing_inputs_1, print_shape_only=True)[1].flatten()

print(activation.output)
