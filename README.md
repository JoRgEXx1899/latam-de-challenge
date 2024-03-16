# Challenge Data Engineer LATAM Airlines :plane:
## REPO ***latam-de-challenge***
Repository for the challenge of LATAM Airlines to apply to work as Data Engineer.

Solved by ***Jorge Daniel Gomez Vanegas*** - Data Engineer. 

Visit my professional profile in [Linkedin](https://www.linkedin.com/in/jorge-daniel-gomez-vanegas-a0055a204/).

Visit my [GitHub](https://github.com/JoRgEXx1899).

## 📕 Project Overview Description of repository

This project is a solution to the challenge presented by LATAM Airlines to apply for the position of Data Engineer with knowledge in GCP.

The questions or challenges presented are found in the provided [document](https://github.com/JoRgEXx1899/latam-de-challenge/blob/main/src/challenge_instructions.md). The challenges are solved in a modular manner, where each challenge and approach has its respective Python file with the necessary libraries to execute the constructed function."

The approaches for each challenge focus on runtime optimization and memory optimization.

The file [challenge.ipynb](src/challenge.ipynb) details the code along with the time measurements and memory usage of each module.

Additionally, a `Python` file is included to establish a connection with Google Cloud Storage, where the supplied `.json` file for this challenge is stored. This file's function is to query the blobs located in the **Google Cloud Storage bucket** and return the path or URL to the file for downloading. Using this same file, functionality could be extended to load Parquet files or alternatively, load the data into **BigQuery** for subsequent querying.

## ⚙️ Prerequisites

This project use the following technologies:

- `Google Cloud Platform`: Used for data warehousing in cloud. You must have an active Google Cloud Platform account, and a billing account. From this platform is used the Google Cloud Storage API.
- `gcloud CLI`: Used for log and interact with Google Cloud on Command line. To install it you can get it from: https://cloud.google.com/sdk/docs/install?hl=es-419
- `Git`: Used for code versioning on local repository for development. You can get it at: https://git-scm.com/
- `Github`: Used for code versioning on remote repository collaborative, and app deploy with GitHub Actions. Log in at: https://github.com/

For development it is recommended to use ``Visual Studio Code``. You can get it at: https://code.visualstudio.com/.

This project is running on Python, the ``Python`` version used is ``3.11.3``

The libraries and versions used for running the code are:
  - ``memory-profiler``- Version: 0.61.0
  - ``ujson``        - Version: 5.8.0
  - ``pandas``     - Version: 2.0.2
  - ``pyarrow``           - Version: 15.0.1
  - ``gcloud``    - Version: 0.18.3
  - ``python-dotenv``       - Version: 1.0.1
  - ``gcsfs``        - Version: 2024.2.0
  - ``emoji``  - Version: 2.8.0

## 🛠️ Installation
### A step-by-step guide on how to set-up your development environment:

1. Create a virtual environment with the virtual environment manager of your preference. Then on the terminal activate the environment.
2. Clone this repository
3. Run the command on the root folder of the git repository
```bash
pip install -r requirements.txt
```
This will install the library dependences needed to run the code.
4. Create a `.env` file in the project folder, with the following variables:

- `PROJECT_ID`: The Google Cloud Platform (GCP) project id.
- `BUCKET_NAME`: The name of the bucket in Google Cloud Storage.
- `BUCKET_FOLDER_ORIGIN`: Folder in bucket where files are stored.
- `GCP_CREDENTIALS`: The JSON content of the key of a GCP account service in a single line. This is used to log into Google Cloud.

## :herb: Github Repository Branches
This project has 2 main branches:
- main
- dev

And four (4) sub-branches from dev used to develop the features to solve challenges 1 to 3.

## ✍️ Authors
| [<img src="https://avatars.githubusercontent.com/u/42323429?v=4" width=115><br><sub>Jorge Daniel Gomez</sub>](https://github.com/JoRgEXx1899)
| :---: |