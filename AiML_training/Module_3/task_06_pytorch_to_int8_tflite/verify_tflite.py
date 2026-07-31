import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="model_int8.tflite")
interpreter.allocate_tensors()

inp = interpreter.get_input_details()[0]
out = interpreter.get_output_details()[0]

print("Input dtype :", inp["dtype"])
print("Output dtype:", out["dtype"])
print("Input quant :", inp["quantization"])
print("Output quant:", out["quantization"])
