from onnx2tf import convert

convert(
    input_onnx_file_path="model.onnx",
    output_folder_path="saved_model",
)

print("SavedModel conversion completed.")
