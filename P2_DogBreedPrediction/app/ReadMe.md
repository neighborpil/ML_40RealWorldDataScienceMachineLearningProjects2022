# DogBreed System
 - Predicting dog breed
 - Used streamlit
 - upload dog image and predict

### Environment
 - M1 mac
 - conda interpreter
### how to install conda on m1 mac
```
% brew install cask
% brew install --cask miniforge
% conda init zsh
```

### Creating virtual venv
```
% conda create --name dogbreed python=3.9
```

### Package install
```
% conda install -c conda-forge opencv
 
% conda install streamlit

% conda install -c apple tensorflow-deps

% conda install bumpy
```

### Running streamlit 
```
% streamlit run /Users/neighborpil/Desktop/works/GitRepository/ML_40RealWorldDataScienceMachineLearningProjects2022/P2_DogBreedPrediction/app/main.py
```