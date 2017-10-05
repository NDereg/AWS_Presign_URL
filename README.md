# AWS Lambda - Python 3.6
## Pre-sign URL for S3 Object
The intent of this script is to use AWS Lambda and preferably, GitLab CI.

## Instructions
### AWS Lambda
- Assuming that AWS Lambda function `AWS_Presign_URL` already exists.
- GitLab CI is optional however, if setup properly; it will automatically update the Lambda function when comitting code to *preferred branch*.

### Modifying
- The only file required to be updated:
  - `./data/config.json`

### Execute Locally
- Open `./scripts/debug.py`.
- Change the following items:
  - Bucket: `test-bucket`
  - File: `NewText.zip`
- Log into AWS and make sure that you have a matching Bucket and File. 
    - *If you have a folder inside your bucket such as **test-folder**, then you need to specify the file with prefix like so: `test-folder/NewText.zip`*
- If you wish to get fresh *Records* returned from Lambda, you can achieve this by creating a Lambda function with some basic `logging.getLogger()` and setup a quick S3 *put, post, copy* trigger, however I will not be providing information on how to do that here.
- Execute `./scripts/debug.py` which calls `./handler.py` which will pass in the `EVENT` inside lambda_handler as the main entry point which then calls the main code `./lib/presign_url.py`.


## Structure Overview
- Folders
  - `./vscode/`: vscode, project workspace settings.
  - `./lib`: contains the project's main code.
  - `./data`: contains config file.
  - `./scripts`: debug scripts - local debug.
- Files
  - `./data/config.json`: config file.
  - `./lib/presign_url.py`: main project code.
  - `./handler.py`: lambda handler that calls presign_url.py.
  - `./scripts/debug.py`: execute locally.