#!/usr/bin/env python3
import os, sys
from importlib import import_module

ROOT = os.getcwd()
NOTEBOOKS = os.path.join(ROOT, "notebooks")
if NOTEBOOKS not in sys.path:
    sys.path.insert(0, NOTEBOOKS)

print("PYTHONPATH includes:", NOTEBOOKS)

try:
    seg = import_module("segmentation_utils")
    print("✅ Imported segmentation_utils")
except Exception as e:
    print("❌ ERROR importing segmentation_utils:", e)
    sys.exit(1)

# Try to build a model if TensorFlow exists (skip otherwise)
try:
    import tensorflow as tf
    models_mod = import_module("segmentation_utils.models")
    if hasattr(models_mod, "build_unet"):
        m = models_mod.build_unet(input_shape=(32, 32, 3), n_classes=3, base_filters=8)
        print("✅ Built tiny model with params:", m.count_params())
except ImportError:
    print("ℹ️ TensorFlow not installed — skipping model build")

print("Smoke test finished successfully.")
