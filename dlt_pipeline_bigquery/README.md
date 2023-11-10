## Setting up dlt pipeline to load data into bigquery with custom data

#### Step 1: Create a virtual Environment and activate it.
- python -m venv dlt_pipeline_bigquery
- dlt_pipeline_bigquuery\Scripts\activate.bat
- 
  **Note**: A virtual environment with name 'dlt_pipeline_bigquery' will be created and activated.
  
  ![create and activate virtual environment](https://github.com/oyemishra/dlt_case_study/assets/73794797/eae439c9-212f-4e68-87a7-86cee4cef831)

#### Step 2: Install dlt library using pip: 
- pip install -U dlt
- 
  **Note**: Command above installs (or upgrades) library core.

#### Step 3: Initialize dlt pipeline for bigquery. 
- dlt init bigquery_pipeline bigquery
- 
  **Note**: A new pipeline bigquery_pipeline will be created.

  ![dlt init bigquery](https://github.com/oyemishra/dlt_case_study/assets/73794797/304af796-e4a9-4f5a-bc88-813f96caf244)
  
  ![dlt init bigquery files and folders](https://github.com/oyemishra/dlt_case_study/assets/73794797/0bb083b4-e32f-43c5-843c-1e57568454f3)

#### Step 4: Install the requirements for the bigquery.
- pip install -r requirements.txt

#### Step 5: Setup service account in GCP to access BigQuery DW. Please provide the following roles to the account: 
- BigQuery Data Editor
- BigQuery Job User
- BigQuery Read Session User

#### Step 6: Go to actions in the service account created, select manage key. 
  ![service key manage keys](https://github.com/oyemishra/dlt_case_study/assets/73794797/c56ddda1-f930-44eb-b5b3-4fd1e5419dd2)
  
  #### then add key, create new key, select JSON format and store the file in a safe location.
  ![service key json](https://github.com/oyemishra/dlt_case_study/assets/73794797/a8a56a97-f4fc-4606-b370-2d09d0e46c06)

#### Step 7: Update dlt credentials file (secrets.toml) with appropriate values from the service account JSON file.
  ![update dlt credentials](https://github.com/oyemishra/dlt_case_study/assets/73794797/3c73ce92-d846-4b11-b5e3-2aa6794bcca4)

#### Step 8: Open the bigquery_pipeline.py pipeline template created and update the resource with your custom data.

  **Note**: this data will be uploaded to the bigquery table.
  ![customized resource and pipeline](https://github.com/oyemishra/dlt_case_study/assets/73794797/fe056f8c-590d-4517-8aeb-1e4fb5e9d5c6)

#### Step 10: Run the pipeline.
- python bigquery_pipeline.py
- 
  ![run the pipeline](https://github.com/oyemishra/dlt_case_study/assets/73794797/d0eedb00-7c0b-4616-94a5-812a9e24c36b)
_____________________________________________________________________________________________________________________________________________
### Bigquery Project "hive-project" before the pipeline run.
  ![BigQuery Before](https://github.com/oyemishra/dlt_case_study/assets/73794797/bae4d0cb-5ba0-40a7-8bee-54bda27f89b5)

### Bigquery Project "hive-project" after the pipeline run.
  ![bigquery after pipeline run](https://github.com/oyemishra/dlt_case_study/assets/73794797/4a9e1d13-7f5a-422b-b1cc-a14677e3c06b)

### Records loaded into the BigQuery Table "bigquery_pipeline_resource".
  ![bigquery table preview](https://github.com/oyemishra/dlt_case_study/assets/73794797/5cc5aafd-ccf2-4cc7-8017-cf9fbeedb965)






