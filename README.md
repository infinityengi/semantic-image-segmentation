# semantic-image-segmentation

Reproducible starter kit for semantic image segmentation: notebooks, data pipelines, augmentation, baseline U-Net, Docker environment and an experiment folder structure.

---
## Quick overview

This repository is organized for reproducibility and easy extension:

```

semantic-image-segmentation/
│
├── docker/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── run.sh
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   └── 02_model_training.ipynb
│   ├── assets/
│   ├── datasets/
│   ├── grid_mapping/
│   ├── ipm_assets/
│   └── localization/
│   ├── object_detection/
│   ├── segmentation_utils/
│   ├── tensorflow_datasets/
├── experiments/
│   ├── runs/
│   └── configs/
├── literature/
│   ├── papers/
│   └── summaries.md
├── .gitignore
├── LICENSE
└── README.md

````

---

## What this repo contains

- `docker/` — Dockerfile + `requirements.txt` and `run.sh` for building/running a reproducible Jupyter environment.
- `notebooks/` — two Jupyter notebooks (preprocessing + model training) and subfolders for experiment assets and helper code.
- `experiments/` — place to store run logs, checkpoints and experiment configs (gitignored).
- `literature/` — store PDFs, bibtex and short summaries.
- `segmentation_utils/` (under `notebooks/` or repo root) — put helper modules (parsing, augmentation, metrics, model builders).

---

## Roadmap (detailed) — how to use & extend this repo

1. **Dataset & labels**
   - Organize images and RGB label maps in `notebooks/datasets/` or `datasets/`.
   - Provide mapping `rgb_to_class_id` to convert color masks → class IDs.

2. **Preprocessing**
   - Convert RGB color labels to segmentation maps (integer IDs).
   - Implement normalization and resizing.
   - Build `tf.data` or `torch.utils.data.Dataset` pipelines with caching/prefetch.

3. **Augmentation**
   - Implement augmentations (flip, noise, gamma, zoom).
   - Compose augmentations as subpolicies and apply one per sample during training.

4. **Modeling**
   - Baseline U-Net (configurable depth and encoder).
   - Support for switching encoders (ResNet, EfficientNet) and more advanced heads (DeepLabV3).

5. **Training & experiments**
   - Log metrics (TensorBoard or W&B).
   - Save checkpoints under `experiments/runs/<timestamp>/`.
   - Track hyperparameters in `experiments/configs/`.

6. **Evaluation & visualization**
   - Compute Mean IoU & per-class IoU.
   - Convert predictions to RGB for qualitative inspection.

7. **Export & deployment**
   - Save model (SavedModel / ONNX / TFLite).
   - Add a simple inference script or API.

---

## Step-by-step: clone, build and run

### 1) Clone
```bash
git clone https://github.com/<your-org>/semantic-image-segmentation.git
cd semantic-image-segmentation
````

### 2) Put data & notebooks

* Convert/place your notebooks into `notebooks/`:

  * `01_data_preprocessing.ipynb` — pipeline, parsing, RGB→class conversion, tf.data. (based on provided notebook). 
  * `02_model_training.ipynb` — augmentation policy, training experiments, evaluation. 

* Place datasets under `datasets/` or `notebooks/datasets/` as expected by the notebooks (e.g. `datasets/kitti/image_2`, `datasets/kitti/semantic_rgb`). 

### 3) Build + run (local)

From repo root:

```bash
# run using the helper script
./docker/run.sh
```

Open Jupyter Lab and open the two notebooks.


## Short descriptions of the included notebooks

* **01_data_preprocessing.ipynb** — dataset inspection & parsing, RGB→class-id mapping, segmentation-map conversion, `tf.data` pipeline, normalization, and visualization. (Contains class color mapping and pipeline examples). 

* **02_model_training.ipynb** — augmentation primitives (random flip, gamma, noise, random zoom), augmentation subpolicies & full policy, integration into the `tf.data` pipeline, U-Net training & evaluation (Mean IoU plots), and model save/load examples. 

---

## Acknowledgements

This repository builds on assignments and teaching material from RWTH Aachen / Institute for Automotive Engineering (ika). It acknowledges the **Automated and Connected Driving Challenges (ACDC)** MOOC on edX — a great resource to learn about challenges in automated and connected mobility.

> **Automated and Connected Driving Challenges (ACDC)** — a MOOC on edX.org teaching how to solve current challenges in automated and connected mobility. Enroll for free here: [https://www.edx.org/course/automated-and-connected-driving-challenges](https://www.edx.org/course/automated-and-connected-driving-challenges). The course is taught by the Institute for Automotive Engineering (ika) of RWTH Aachen University.

This repo *builds on assignments from RWTH/ika* and is intended for teaching, experimentation and extension.
