![header](assets/static/mildew_hero_tall.png)

# Cherry Mildew Detector

The cherry mildew detector app is a ML project to develop a CNN model that can accurately detect if a leaf from a cherry tree is infected with powdery mildew. The app allows the user to upload image files of cherry leaves and predict if a mildew infection is present. The app also provides backgroud information on the project, performance metrics for the model and the results of an image visualisation study to define visual differences between healthy and mildew infected cherry leaves.

This app was developed as part of the Diploma in Full Stack Development with Predictive Analytics specialisation at Code Institute.

The live app can be accessed on streamlit cloud [here](https://cherry-mildew-detector-yk8tvuvywdewixijqpatlv.streamlit.app/) or on render [here](https://cherry-mildew-detector.onrender.com/)

We recommend accessing app on streamlit cloud if available as it has faster response and loading speeds.

## Dataset Content

The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). The dataset consists of 4208 .jpeg images, split evenly between 'healthy' and 'powdery_mildew' classes. All images are 256px x 256px.

Code Institute then created a fictitious user story for the dataset where predictive analytics can be applied in a real project in the workplace:
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. This infection can damage their cherry crops and result in significant loss in revenue. They are looking for a way to improve their monitoring and response to the occurrence of powdery mildew.

1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

Mildew infected leaves will have clear signs of white mildew that can differentiate them from a healthy leaf.
- Can be addressed with DL model to predict health status of leaf from leaf image(s)

Dataset is too small and model performance and accuracy of prediction will be negatively impacted.
- Can be addressed through augmentation of training dataset to increase sample size.

Mildew infection is not as easily distinguished from healthy leaves on low resolution images
- Can be addressed by comparing DL model performance between images with different image shape (resolution) using multiple .pkl files

Visual differentiation of healthy and infected leaves can be improved by aligning leaf images in the same orientation prior to carrying out study.
- Can be addressed by comparing Average Image, Variability Image and Difference between Averages studies before and after orientation adjustment of images.


## The rationale to map the business requirements to the Data Visualisations and ML tasks

#### Business Requirement 1: Data Visualization

- We will display an image montage for comparision of healthy and mildew infected cherry leaves.
- We will display the "average"(mean) and "variation"(standard deviation) images for healthy and mildew infected cherry leaves.
- We will display the difference between average healthy and mildew infected cherry leaves.

#### Business Requirement 2: Classification

- We want to predict if a given leaf is infected or not with powdery mildew.
- We want to build a binary classifier and generate reports.

## ML Business Case

### Cherry Mildew Detector
- We want an ML model to predict if a cherry leaf is infected with powdery mildew or not based on historical image data. It is a supervised model, a 2-class, single-label classification model.
- Our ideal outcome is to provide the cherry farm workers with a faster and more reliable diagnostic for powdery mildew detection.
- The model success metrics are:
    - Accuracy of 97% or above on the test set.
- The model output is defined as a flag, indicating whether a cherry leaf is healthy or infected with powdery mildew, along with the associated probability. Workers on the farm will use the app to take leaf images in real-time, allowing for immediate assessment and decision-making in the field.
- Heuristics: The current management process involves manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection. Additionally, this process of manual inspection leaves room for human error.
- The training data to fit the model comes from Kaggle. This dataset contains 4+ thousand images with kaggle datacard not indicating original provenance. 
    - Train data - target: mildew infected or not; features: all images

## Dashboard Design

### General Styling
- a logo, in small and large format, was designed for the sidebar
- a hero image for the project summary page was designed
- a custom colour theme was developed
- custom styling, including use of Google fonts, was implemented with css

### Page 1: Quick Project Summary
- General Information
    - Powdery mildew is an infection caused by the fungus Podosphaera clandestina. It presents as white powdery patches on new or young leaves, with growth typically starting on the underside of the leaf. 
    - Multiple cherry leaves are collected and visually inspected manually. Visual criteria are used to detect mildew infection. The inspection process takes 30 minutes per tree.
    - The infection will not kill the leaf but can cause distortion and discolouration. This infection can be transferred to the cherry fruit as they mature, causing damage and losses to the cherry crop.
- Project Dataset
    - The dataset provided by the client contains 4208 .jpg images of healthy and powdery-mildew infected cherry leaves taken from their cherry farms.
    - Link to additional information (Readme file)
- Business requirements
    - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Cherry Leaf Visualisation
- General information including:
    - Answers business requirement 1 - "TThe client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew."
    - description of page content
- Toggle 1 - Image Montage
- Toggle 2 - Average image and image variability for healthy and mildew infected classes
- Toggle 3 - Differences between the average images from healthy and mildew infected
- Toggle 4 - Conclusions of visualisation study

### Page 3: Mildew Detection
- General information including:
    - Answers business requirement two - "The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
    - Success metrics - greater than 97% accuracy
    - ‘How to use’ information for file uploader and predictions
    - Link to download a set of parasite-contained and uninfected cell images for live prediction.
- A user interface with a file uploader widget. The user can upload single or multiple cherry leaf images. It will display the image, image details and a prediction statement, indicating if the leaf is healthy or infected with mildew and the probability associated with this statement.
- Table with the image name and prediction results.
- Download button to download table.

### Page 4: Project Hypotheses
- Block for each project hypothesis, description of the conclusion and how it was validated.

### Page 5: Model Performance Metrics
- General information including:
    - Model architecture summary
    - Descriptions of performance metrics
- Toggle 1 - Label Frequencies for Train, Validation, and Test Sets
- Toggle 2 - Training History - Accuracy and Losses
- Toggle 3 - Performance on test set:
    - Test evaluation
    - Confusion matrix
    - Classification report
- Toggle 4 - conclusions


## Bugs

### Fixed
- Repo to large for deployment on Heroku

**Description:**
The slug size limit of 500MB for Heroku was exceeded when deploying an empty page streamlit app
**Resolution:**
Downgraded streamlit from V1.41.0 to V1.40.2 which saved 14.89MB in space. This only just brought slug size below 500MB so to future protect issues when app contains model switched deployment to Render and Streamlit cloud.

- np .append() deprecated

**Description:**
In original code from malaria walkthough project the function for plotting labels distribution used .append(). This was carried over when the function was used in this project.
**Resolution:**
ChatGPT was used to help diagnose the bug and refactor the code so that .append() was no longer required.

- not able to push to repo after model tuning

**Description:**
After model tunig using keras-tuner the tuning files were too large to push to the repo. Using git reset --soft and --hard did not work and put source control into an eternal update loop that never ended.
**Resolution:**
Downloaded the notebook, best paramaters .csv and tuning files and created a new workspace in gitpod. Did not reload tuning files, instead manually defined model using best model hyperparameters identified from training. Notebook and .csv were uploaded and pushed to repo successfully.

- fail to push first model to repo

**Description:**
After model training could not push to repo as saved model (V1) was too large (~160MB). Using git reset --soft and --hard did not work and put source control into an eternal update loop that never ended.
**Resolution:**
Using git reset --soft to remove problematic commit and installed Git LArge File Storage to allow model to be pushed to repo.

- V1 model preventing deployment

**Description:**
Having v1 saved in repo made total slug size too large once v5 model was also present and prevented deployment.
**Resolution:**
Downloaded and saved model and deleted from repo so only v5 model (11.6MB), which was being used for streamlit app, present in repo.

- multiple toggles on app page prevent page loading

**Description:**
Inserting 4 toggles on data visualisation page prevented page from loading when running app and produced an error message from streamlit saying toggles required unique key.
**Resolution:**
Followed guiudance from streamlit error message and added unique keys to each toggle.

- Toggles on visualisation page reset montage to dafault

**Description:**
Using toggles on data visualisation page causes the page to reload. If a new montage had been generated it was lost, with the montage reverting back to the default image.
**Resolution:**
Used ChatGPT to troubleshoot and refactor montage code to use st.session-state to store the generated montage so that it is not lost when page reloads after toggle activation.

- Confusion matrix does not assign scores to labels correctly

**Description:**
Output from confusion matrix and classification report conflict with model accuracy evaluation. The output is evenly split between correct and wrong suggesting there may be random label associations.
**Resolution:**
desertnaut's [response](https://stackoverflow.com/questions/48908641/how-to-get-a-single-value-from-softmax-instead-of-probability-get-confusion-ma) to a similar issue posted on stack overflow highlighted that 'shuffle' needed to be set to False (default is true) when loading test dataset with .flow-from-directory()

**Neutral Resolution**
App deployed to render is very slow to load pages and features and respond to requests. There is no fix for this. Instead the recommendation is to use the app deployed on Streamlit Cloud as it is faster and more responsive.

### Unfixed
**All bugs detected have been resolved**

## Deployment
** The app is too large for deployment on Heroku, exceeding the 500MB slug-size limit. As such it ws deployed onto Render and Streamlit Cloud.

### Render

- The App live link is: `https://cherry-mildew-detector.onrender.com/`
- Before starting, ensure your requirements.txt file is up to date.
- The project was deployed to Render using the following steps:

1. Log in to Render using your GitHub credentials and create a user profile.
2. Create an new App
2. Link the app to your GitHUb repository using the interface provided.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen automatically if all deployment files are fully functional. 
6. Once the repo is loaded click the link on the top of the page to access your App. The app will automatically redeploy with every new commit to repo.

### Streamlit Cloud

- The App live link is: `https://cherry-mildew-detector-yk8tvuvywdewixijqpatlv.streamlit.app/`
- Before starting, ensure your requirements.txt file is up to date.
- The project was deployed to Streamlit using the following steps:

1. Log in to Streamlit Cloud using your GitHub credentials and create a user profile.
2. Create an new App
2. Link the app to your GitHUb repository using the interface provided.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen automatically if all deployment files are fully functional. 
6. Once the repo is loaded click the link on the top of the page to access your App. The app will automatically redeploy with every new commit to repo.

If you wish to develop this app further, feel free. To do this, create a fork of this repository and save it to your own github profile. To do this, use the fork button at the top right of this repository. This brings you to a new window, where you select yourself as the owner and can add extra details to name and description of the repo. You will then, if required, deploy to your own Heroku account using the process described above. You will also need to generate you own env.py and Heroku config var values to ensure all featuires will work. If you chose to do this, please be respectful and credit me as the origin of this project and code.

![GitHub language count](https://img.shields.io/github/languages/count/Annytomica/cherry-mildew-detector)
![GitHub top language](https://img.shields.io/github/languages/top/Annytomica/cherry-mildew-detector?color=yellow)
![GitHub watchers](https://img.shields.io/github/watchers/Annytomica/cherry-mildew-detector)
![GitHub forks](https://img.shields.io/github/forks/Annytomica/cherry-mildew-detector?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/Annytomica/cherry-mildew-detector?style=social)

## Main Data Analysis and Machine Learning Libraries

- **OS**: Used for file and directory path handling
- **streamlit**: Used extensively for building the UI of streamlit app
- **numpy**: Examples of use include numerical operations and handling image data (eg. np.array(pil_image))
- **pandas**: Examples of use include handling dataframes, evaluation reports and structuring prediction probabilities.
- **matplotlib**: Examples of use include creating the montage layout, saving plots as images and creating fugures with mutliple plots.
- **seaborn**: For enhanced plot visualisation, such as model training history accuracy and losses line plots, label frequency bar plots
- **pillow**: Used for image processing such as resizing, retrieving image properties and image uploading.
- **joblib**: Examples of use include loading and saving .pkl files.
- **scikit-learn**: Examples of use include model evaluation such as confusion matrix and classification report.
- **tensorflow.keras**: Used for building training and testing models and making predictions using model.
- **keras_tuner**: used for tuning of model hyperparameters
- **Random**: Used for selecting images randomly from dataset folders
- **io** – Used for handling in-memory image storage
- **shutil** - used for organising dataset files
- **cv2(openCV)** - computer vision package used for leaf orientation functions
- **datetime** - used for associating date and time for .csv file prediction report generation
- **base64** - used for handling the prediction report .csv file for download

## Credits

I would like to acknowledge and thank the following people and resources used in the creation of this site.

I would also like to note that this app was developed during a period where I was effectively homeless amd couch surfing with friends and family. I was deprived of reliable internet connections and ideal work spaces for significant periods of time. As such, normal support routes of mentor meetings and tutoring were not always available and ChatGPT was used as a replacement. While no code was directly generated by ChatGPT it does write out corrections for exisiting code, in a way that mentors and tutors do not, and I would like to acknowledge this fact.

## Content
### Large contributions
- [CI Mildew project template repo](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves):
    - Basic code for setup and deployment including requirements.txt, Profile and setup.sh
    - jupyter notebook template
    - Readme template with intial dataset content and business requirements sections.
- [CI Malaria walkthrough project](https://github.com/Annytomica/WalkthroughProject01):
    - Basic code for setting up multipage streamlit apps
    - basic structure of all notebooks and dashboard pages
    - 
    - third-party wireups such as Cloudinary, summernote etc used same versions as used in walkthrough to ensure they connected correctly with Heroku etc.

- [ChatGPT](https://chatgpt.com):
    - typo identification
    - troubleshooting
    - optimising logic and refactoring code from walkthrough projects to suit this project
    - using st.session_state
    - displaying article like and comment counts on homepage
    - fixing cloudinary http bug
    - automated testing of difficult or novel features

### General contributions


### Media

- The logo and hero image were generated by Megan Abel, my wife, who gave permission for thier use.
- The XXX font is from [Google Fonts](https://fonts.google.com/specimen/Raleway)
- The Github summary bar used in README.md is from [shields.io](https://shields.io/badges/)

## Acknowledgements

- Thank the people who provided support throughout this project.
