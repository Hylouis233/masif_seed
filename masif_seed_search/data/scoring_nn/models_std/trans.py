import tensorflow as tf
from tensorflow import keras


model = tf.keras.models.load_model('D:/github/masif_seed/masif_seed_search/data/masif_targets/targets/4QVF_A/model')
model.load_weights('D:/github/masif_seed/masif_seed_search/data/masif_targets/targets/4QVF_A/model/checkpoint')