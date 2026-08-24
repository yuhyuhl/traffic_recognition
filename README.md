## MSc Project 

### Traffic Sign Recognition: Comparative Study of Machine Learning and Deep Learning Approaches

This project investigates traffic sign image classification using the German Traffic Sign Recognition Benchmark (GTSRB).

The four evaluated approaches are:
- HOG + Linear SVM
- Custom CNN
- ResNet18 with transfer learning
- MobileNetV3-Large with transfer learning

The project was developed as part of an MSc dissertation and focuses on comparing predictive performance, class-level behaviour, and computational cost under a CPU-based experimental environment.

#### Dataset

The project uses the GTSRB dataset, which contains:

- 39,209 training images
- 12,630 test images
- 43 traffic sign classes
- Images with varying spatial dimensions

The raw dataset is not included in this repository. It can be downloaded separately from the GTSRB or Kaggle dataset page.
https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign  

#### Project Workflow

The project follows a notebook-based experimental workflow:

01_data_exploration.ipynb
        ↓
02_data_preprocessing.ipynb
        ↓
Saved train / validation / test splits
        ↓
03_hog_svm_baseline.ipynb
04_cnn_baseline.ipynb
05_transfer_learning_resnet18.ipynb
06_transfer_learning_mobilenetv3.ipynb
        ↓
Saved models, predictions and evaluation results
        ↓
07_model_comparison_evaluation.ipynb

Each model notebook uses the same saved dataset split so that differences in performance are not caused by different sample allocations.

#### Project Structure

traffic_recognition/ 
│ 
├── data/
│   └── raw/            Original dataset files
│   └── processed/      Saved dataset split files
│ 
├── notebooks/          Data exploration and preprocessing notebooks
│ 
├── models/
│ 
├── results/            Tables and generated figures
│   └── figures/        
│   └── tables/
│ 
├── src/                Reusable Python source code
│   └── dataset.py
│   
├── README.md
└── .gitignore

Large dataset files, generated models, local environments, and temporary files may be excluded from version control through .gitignore. 


#### Author

Yuhan Liu

University of Leeds
