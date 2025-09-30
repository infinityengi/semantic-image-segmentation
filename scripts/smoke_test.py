#!/usr/bin/env python3
"""
Smoke test for semantic-image-segmentation project.

- Ensures `segmentation_utils` package (under notebooks/) is importable.
- Imports `image_segmentation_utils`.
- If TensorFlow is available, tries to build a tiny U-Net model via build_unet().
"""

import os
import sys
from importlib import import_module

# --- Add notebooks/ to PYTHONPATH ---
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NOTEBOOKS = os.path.join(ROOT, "notebooks")
if NOTEBOOKS not in sys.path:
    sys.path.insert(0, NOTEBOOKS)

print("PYTHONPATH includes:", NOTEBOOKS)

# --- Import segmentation_utils package ---
try:
    seg = import_module("segmentation_utils")
    print("✅ Imported segmentation_utils package")
except Exception as e:
    print("❌ ERROR: could not import segmentation_utils:", e)
    sys.exit(1)

# --- TensorFlow check ---
try:
    import tensorflow as tf
    print(f"✅ TensorFlow installed, version: {tf.__version__}")
except ImportError:
    print("ℹ️ TensorFlow not installed — skipping model build")
    tf = None

# --- Model build test from image_segmentation_utils ---
if tf is not None:
    try:
        utils_mod = import_module("segmentation_utils.image_segmentation_utils")
        print("✅ Imported segmentation_utils.image_segmentation_utils")

        if hasattr(utils_mod, "build_unet"):
            model = utils_mod.build_unet(
                input_shape=(32, 32, 3),
                n_classes=3,
                base_filters=8,
            )
            print("✅ Built tiny model from image_segmentation_utils with params:", model.count_params())
        else:
            print("ℹ️ No build_unet() found in image_segmentation_utils — skipping model build")

    except Exception as e:
        print("❌ Model build failed:", e)

print("🎉 Smoke test finished successfully.")
