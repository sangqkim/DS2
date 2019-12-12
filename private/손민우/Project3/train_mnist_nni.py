"""Configurable training loop for mnist."""

import os
import nni
import tensorflow.keras as keras

from tensorflow.keras import datasets     # data
from tensorflow.keras import layers       # model
from tensorflow.keras import losses       # loss
from tensorflow.keras import optimizers   # optimizer
from tensorflow.keras import callbacks    # callback


def main():
    hp_dict = nni.get_next_parameter()  # hp_dict is automatically suggested
    _, test_acc = tunable_train(hp_dict)
    nni.report_final_result(test_acc) # report final accuracy
    
    
class EpochCallback(callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        val_accuracy = logs["val_accuracy"]
        nni.report_intermediate_result(val_accuracy)  # report validation accuracy at each epoch


def get_dataset(hp_dict):
    """Return MNIST dataset"""
    # load data
    (train_x, train_y), (test_x, test_y) = datasets.mnist.load_data()
    # reshape & type cast
    train_x = train_x.reshape(train_x.shape[0], 28, 28, 1).astype('float32')
    train_y = train_y.astype('int64')
    test_x = test_x.reshape(test_x.shape[0], 28, 28, 1).astype('float32')
    test_y = test_y.astype('int64')
    # normalize data
    train_x /= 255.
    test_x /= 255.
    return train_x, train_y, test_x, test_y


def get_model(hp_dict):
    """Return CNN model"""
    model = keras.Sequential()
    model.add(layers.Conv2D(filters=64, kernel_size=2, padding='same', activation='relu', input_shape=(28,28,1))) 
    model.add(layers.MaxPooling2D(pool_size=2))
    model.add(layers.Dropout(0.3))
    model.add(layers.Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=2))
    model.add(layers.Dropout(0.3))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(10, activation='softmax'))
    
    return model


def get_loss(hp_dict):
    """Return xentropy loss"""
    return losses.SparseCategoricalCrossentropy(from_logits=True)

def get_optimizer(hp_dict):
    """Return ADAM optimizer"""
    lr = hp_dict["lr"]
    optimizer_name = hp_dict["optimizer_name"]
    if optimizer_name == "SGD":
        return optimizers.SGD(lr)
    if optimizer_name == "RMSprop":
        return optimizers.RMSprop(lr)
    if optimizer_name == "Adam":
        return optimizers.Adam(lr)
    raise NotImplementedError
    
os.makedirs("checkpoints", exist_ok=True)
experiment_id = nni.get_experiment_id()
trial_id = nni.get_trial_id()
model_path = f"checkpoints/{experiment_id}-{trial_id}.h5"
    
    
def tunable_train(hp_dict):
    # get components
    train_x, train_y, test_x, test_y = get_dataset(hp_dict)
    model = get_model(hp_dict)
    loss = get_loss(hp_dict)
    optimizer = get_optimizer(hp_dict)
    
    # define callback
    alert_callback = EpochCallback()
    checkpoint_callback = callbacks.ModelCheckpoint(filepath=model_path, monitor='val_accuracy', verbose=1, save_best_only=True)
    
    # compile and train(fit) model
    model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"])
    model.fit(
        train_x, train_y, 
        epochs=10, batch_size=hp_dict["batch_size"], 
        callbacks=[alert_callback, checkpoint_callback], 
        validation_data=(test_x, test_y)
    )
    
    # evaluate model
    test_loss, test_acc = model.evaluate(test_x, test_y, verbose=2, batch_size=512)
    
    return test_loss, test_acc


if __name__ == "__main__":
    main()
