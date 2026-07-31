import os
import numpy as np
import tensorflow as tf

CALIB_DIR = "calib"

def representative_dataset():
    files = sorted(
        [f for f in os.listdir(CALIB_DIR) if f.endswith(".npy")]
    )

    for f in files:
        sample = np.load(os.path.join(CALIB_DIR, f)).astype(np.float32)

        # NCHW -> NHWC
        sample = np.transpose(sample, (0, 2, 3, 1))

        yield [sample]


converter = tf.lite.TFLiteConverter.from_saved_model("saved_model")

converter.optimizations = [tf.lite.Optimize.DEFAULT]

converter.representative_dataset = representative_dataset

converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS_INT8
]

converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

tflite_model = converter.convert()

with open("model_int8.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ model_int8.tflite created")
