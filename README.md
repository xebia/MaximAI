### Prerequisites
- Python 3.11 or above
- Google Cloud Platform (GCP) account
- GCLoud CLI

### Local Installation

1. Clone the repository:
shell
git clone <repository-url>
2. Install the required dependencies:

```bash
#/bin/bash
pip install poetry
poetry lock
poetry install --with dev

```
Authenticate to the GCLOUD CLI and set a default project.
```bash 
#/bin/bash
gcloud auth login
gcloud config set project $MY_PROJECT_ID
```

Start the FastAPI server.

```
uvicorn main:app
```

You can now make some API calls to the REST API. Source the `tesh.sh` file for some examples.

```
. test.sh
```