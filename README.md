# Sentiment-Analysis-web-app
Sentiment Analysis hotel review app is used to sentiment(Positive/negative) of the review left by the customer. Created using python's scikit-learn, nltk, Fastapi, numpy and joblib packages.

![python 3.11.0](https://img.shields.io/badge/Python-blue.svg)
![html](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![numpy](https://img.shields.io/badge/Numpy-777BB4?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/Scikit_learn-0078D4?logo=scikit-learn&logoColor=white)
![fastapi](https://img.shields.io/badge/Fastapi-109989?logo=FASTAPI&logoColor=white)
![jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?logo=Jupyter&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)


## Dataset Description

The dataset consist of one predictor (independent) variable, Review and one target (dependent) variable, Liked.

The data contains the following columns:

| Feature Name               | Feature Description                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Review                     | Review of the hotel left by the customer(text)                                                      |
| Liked                      | Positive/Negative(1/0)                                                                              |


## Installation

Open Anaconda prompt and create new environment

```
conda create -n your_env_name python = (any_version_number > 3.11.0)
```

Then Activate the newly created environment

```
conda activate your_env_name
```

Clone the repository using `git`

```
git clone gh repo clone Baktho-SN/Sentiment-Analysis-web-app
```

Change to the cloned directory

```
cd <directory_name>
```

To install all requirement packages for the app

```
pip install -r requirements.txt
```

Then, Run the app

```
uvicorn main:app --reload
```

## 📷 Screenshots

### Website

![app interface](markdown/Homepage1.png)
![app interface](markdown/Homepage2.png)

### Demo

![Demo.GIF](markdown/DEMO.webp)
