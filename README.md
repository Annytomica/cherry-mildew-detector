![header](assets/static/mildew_hero_tall.png)

# Cherry Mildew Detector

The cherry mildew detector app is a ML project to develop a CNN model that can accurately detect if a leaf from a cherry tree is infected with powdery mildew. The app allows the user to upload image files of cherry leaves and predict if a mildew infection is present. The app also provides backgroud information on the project, performance metrics for the model and the results of an image visualisation study to define visual differences between healthy and mildew infected cherry leaves.

This app was developed as part of the Diploma in Full Stack Development with Predictive Analytics specialisation at Code Institute.

The live app can be accessed on streamlit cloud [here](https://cherry-mildew-detector-yk8tvuvywdewixijqpatlv.streamlit.app/) or on render [here](https://cherry-mildew-detector.onrender.com/)

We recommend accessing app on streamlit cloud if available as it has faster response and loading speeds.

## Dataset Content

The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). The dataset consists of XXX .jpeg images, split evenly between 'healthy' and 'powdery_mildew' classes. All images are 256px x 256px.

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

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Bugs

### Fixed
- Comment edit submitting new comment not changing old.

**Description:**
The submit process for edit not working and commentForm attribute not being assigned to allow submission of change. Is submitted as a new comment.
**Resolution:**
Found typo in submitButton single_article.html, but major issue was that the Abstract Id of contactForm was conflicting with the commentForm Id that needed to be identified to setAttribute of action="edit_comment" to change button action from submit to edit. The contactForm Id was removed to resolve.

**Neutral Resolution**

### Unfixed
**All bugs detected have been resolved**

## Deployment

### Render

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

### Streamlit community cloud

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

If you wish to develop this app further, feel free. To do this, create a fork of this repository and save it to your own github profile. To do this, use the fork button at the top right of this repository. This brings you to a new window, where you select yourself as the owner and can add extra details to name and description of the repo. You will then, if required, deploy to your own Heroku account using the process described above. You will also need to generate you own env.py and Heroku config var values to ensure all featuires will work. If you chose to do this, please be respectful and credit me as the origin of this project and code.

![GitHub language count](https://img.shields.io/github/languages/count/Annytomica/cherry-mildew-detector)
![GitHub top language](https://img.shields.io/github/languages/top/Annytomica/cherry-mildew-detector?color=yellow)
![GitHub watchers](https://img.shields.io/github/watchers/Annytomica/cherry-mildew-detector)
![GitHub forks](https://img.shields.io/github/forks/Annytomica/cherry-mildew-detector?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/Annytomica/cherry-mildew-detector?style=social)

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

I would like to acknowledge and thank the following people and resources used in the creation of this site.

I would also like to note that this app was developed during a period where I was effectively homeless amd couch surfing with friends and family. I was deprived of reliable internet connections and ideal work spaces for significant periods of time. As such, normal support routes of mentor meetings and tutoring were not always available and ChatGPT was used as a replacement. While no code was directly generated by ChatGPT it does write out corrections for exisiting code, in a way that mentors and tutors do not, and I would like to acknowledge this fact.

## Content
### Large contributions
- [CI Blog walkthrough project](https://github.com/Annytomica/django-blog-walkthrough):
    - Basic code for setting up Django projects and apps
    - all wireups for views, models, urls were adapted from the course code with significant generic code retained
    - deployment to Heroku
    - third-party wireups such as Cloudinary, summernote etc used same versions as used in walkthrough to ensure they connected correctly with Heroku etc.
- The free Abstract boostrap template from [StyleShout](https://styleshout.com/abstract-modern-masonry-blog-website-template/) for providing all styling html, css and js to create a responsive masonary-brick based site. StyleShout is acknowledged in footer as per usage requirement.

- [ChatGPT](https://chatgpt.com):
    - typo identification
    - troubleshooting
    - optimising logic for like functions
    - correcting like/comments view to remove clash of submission (see bug report)
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
