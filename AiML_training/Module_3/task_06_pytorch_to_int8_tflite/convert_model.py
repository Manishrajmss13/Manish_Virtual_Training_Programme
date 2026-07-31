
import os
import logging
import numpy as np

import torch
import onnx

from model_definition import SimpleCNN

logging.basicConfig(
    filename="conversion_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(msg):
    print(msg)
    logging.info(msg)

def load_model():

    if not os.path.exists("model.pth"):
        raise FileNotFoundError("model.pth not found.")

    model = SimpleCNN()
    model.load_state_dict(torch.load("model.pth", map_location="cpu"))
    model.eval()

    log("✓ PyTorch model loaded successfully.")

    return model


def validate_calibration():

    calib_dir = "calib"

    if not os.path.exists(calib_dir):
        raise FileNotFoundError("Calibration folder missing.")

    files = sorted(
        [f for f in os.listdir(calib_dir) if f.endswith(".npy")]
    )

    if len(files) == 0:
        raise RuntimeError("Calibration folder empty.")

    for file in files:

        arr = np.load(os.path.join(calib_dir, file))

        if arr.shape != (1,1,28,28):
            raise ValueError(f"{file} invalid shape {arr.shape}")

        if np.isnan(arr).any():
            raise ValueError(f"{file} contains NaN")

        if np.isinf(arr).any():
            raise ValueError(f"{file} contains Inf")

    log(f"✓ Validated {len(files)} calibration samples.")

    return files


def export_onnx(model):

    dummy = torch.randn(1,1,28,28)

    torch.onnx.export(
        model,
        dummy,
        "model.onnx",
        export_params=True,
        opset_version=13,
        do_constant_folding=True,
        input_names=["input"],
        output_names=["output"]
    )

    log("✓ ONNX model exported.")


def verify_onnx():

    model = onnx.load("model.onnx")

    onnx.checker.check_model(model)

    log("✓ ONNX model verified.")


def main():

    log("========== Conversion Started ==========")

    model = load_model()

    validate_calibration()

    export_onnx(model)

    verify_onnx()

    log("Part 2 completed successfully.")


if __name__ == "__main__":
    main()
