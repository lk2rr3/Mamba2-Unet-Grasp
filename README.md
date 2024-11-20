# Generative Mamba-2 U-Net Grasp
The ME5400A project for A0290591Y Wang, Xinda, subjected to changes and cleanup.
The code is built using the stem code (preprocessing, dataloading, etc.) from https://github.com/skumra/robotic-grasping.git
Mamba-2 implementation is based on https://github.com/Human9000/nd-Mamba2-torch.
A U-Net shape network is built by myself using each stage of VMamba as encoder and convolution transpose layers as decoder, to generate pixel-wise predictions for grasp quality, angle and width.

#### Antipodal Robotic Grasping using Generative Mamba-2 U-Net structure

Wang, Xinda


## Requirements

- numpy
- opencv-python
- matplotlib
- scikit-image
- imageio
- torch
- torchvision
- torchsummary
- tensorboardX
- pyrealsense2
- Pillow

## Installation
- Create a virtual environment
```bash
$ python3.6 -m venv --system-site-packages venv
```

- Source the virtual environment
```bash
$ source venv/bin/activate
```

- Install the requirements
```bash
$ cd robotic-grasping
$ pip install -r requirements.txt
```

## Datasets

This repository supports both the [Cornell Grasping Dataset](https://www.kaggle.com/oneoneliu/cornell-grasp) and
[Jacquard Dataset](https://jacquard.liris.cnrs.fr/).

#### Cornell Grasping Dataset

1. Download the and extract [Cornell Grasping Dataset](https://www.kaggle.com/oneoneliu/cornell-grasp). 
2. Convert the PCD files to depth images by running `python -m utils.dataset_processing.generate_cornell_depth <Path To Dataset>`

#### Jacquard Dataset

1. Download and extract the [Jacquard Dataset](https://jacquard.liris.cnrs.fr/).


## Model Training

A model can be trained using the `train_network.py` script.  Run `train_network.py --help` to see a full list of options.

Example for Cornell dataset:

```bash
python train_network.py --dataset cornell --network <See inference/models/__init__.py for available networks> --dataset-path <Path To Dataset> --description training_cornell
```

Example for Jacquard dataset:

```bash
python train_network.py --dataset jacquard --network <See inference/models/__init__.py for available networks> --dataset-path <Path To Dataset> --description training_jacquard --use-dropout 0 --input-size 300
```

## Model Evaluation

The trained network can be evaluated using the `evaluate.py` script.  Run `evaluate.py --help` for a full set of options.

Example for Cornell dataset:

```bash
python evaluate.py --network <Path to Trained Network> --dataset cornell --dataset-path <Path to Dataset> --iou-eval
```

Example for Jacquard dataset:

```bash
python evaluate.py --network <Path to Trained Network> --dataset jacquard --dataset-path <Path to Dataset> --iou-eval --use-dropout 0 --input-size 300
```


