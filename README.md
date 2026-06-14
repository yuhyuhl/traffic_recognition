<<<<<<< HEAD
# traffic_recognition
MSc project on traffic sign image classification
=======
# Traffic Sign Recognition Using Machine Learning and Deep Learning

This project investigates traffic sign image classification using the German Traffic Sign Recognition Benchmark (GTSRB).

## Project Objectives

- Explore and prepare the GTSRB dataset.
- Implement a baseline convolutional neural network.
- Apply transfer learning using pre-trained models.
- Compare model performance using classification metrics.
- Analyse class-level errors and model limitations.

## Dataset

The project uses the GTSRB dataset, which contains:

- 39,209 training images
- 12,630 test images
- 43 traffic sign classes

The raw dataset is not included in this repository. It can be downloaded separately from the GTSRB or Kaggle dataset page.

## Current Progress

- Dataset selected and downloaded
- Exploratory data analysis completed
- Class distribution analysed
- Image dimensions analysed
- Missing and corrupted images checked
- Stratified training and validation split created
- PyTorch Dataset and DataLoader implemented
- Image preprocessing and augmentation pipeline completed

## Project Structure

```text
data/processed/     Saved dataset split files
notebooks/          Data exploration and preprocessing notebooks
results/            Tables and generated figures
src/                Reusable Python source code
>>>>>>> Dataset exploration and preprocessing pipeline completed
