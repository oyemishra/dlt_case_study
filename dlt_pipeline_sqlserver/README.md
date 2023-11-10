## Setting up dlt pipeline to load data into Azure SQLDatabases with custom data

#### Step 1: Create a virtual Environment and activate it.
- python -m venv dlt_pipeline_sqlserver
- dlt_pipeline_sqlserver\Scripts\activate.bat
- 
  **Note**: A virtual environment with name 'dlt_pipeline_sqlserver' will be created and activated.

#### Step 2: Install dlt library using pip: 
- pip install -U dlt
- 
  **Note**: Command above installs (or upgrades) library core.
  
**Note: Microsoft ODBC driver for SQL Server must be installed to use this destination. 
This can't be included with dlt's python dependencies so you must installed it separately on your system.**

#### Step 3: Initialize dlt pipeline for SQL Server. 
- dlt init sqlserver_pipeline mssql
- 
  **Note**: A new pipeline sqlserver_pipeline will be created, if not exists.

  ![files and folders after dlt init mssql](https://github.com/oyemishra/dlt_case_study/assets/73794797/8f83e9c0-e7df-4b7f-a2bc-6914f8383e39)

#### Step 4: Install the requirements for the mssql.
- pip install -r requirements.txt

#### Step 5: Update dlt credentials file (secrets.toml) with appropriate values.
  ![sqldatabase credentials](https://github.com/oyemishra/dlt_case_study/assets/73794797/1a7bb23c-77bc-443c-ae56-bb05e306ef3e)

#### Step 6: Open the sqlserver_pipeline.py pipeline template created and update the resource with your custom data.

  **Note**: this data will be uploaded to the sql database table.
  ![sqldatabase resource and pipeline](https://github.com/oyemishra/dlt_case_study/assets/73794797/4e88d453-8533-422d-8a1e-b8538998dd1a)

#### Step 7: Run the pipeline.
- python sqlserver_pipeline.py
- 
  ![sqldatabase_pipeline_run](https://github.com/oyemishra/dlt_case_study/assets/73794797/69bc86cd-1c33-4f9f-92ee-563f21def14d)

_____________________________________________________________________________________________________________________________________________
### SQL Database "database_name" before the pipeline run.
  ![sqldatabase before pipeline run](https://github.com/oyemishra/dlt_case_study/assets/73794797/3fba158d-93ef-4446-94e8-080c9d16133a)

### SQL Database "database_name" after the pipeline run.
  ![sqldatabase after pipeline run](https://github.com/oyemishra/dlt_case_study/assets/73794797/ae306d2b-98ae-4fd3-b31b-e5c44619c7eb)

### Records loaded into the SQL Database Table "sqlserver_pipeline_resource".
  ![sqldatabase table records](https://github.com/oyemishra/dlt_case_study/assets/73794797/d89ae252-2d59-41a8-ab2e-24da4734c2f2)

