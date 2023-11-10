import dlt
# from dlt.sources.helpers import requests 


@dlt.source
def sqlserver_pipeline_source(api_secret_key=dlt.secrets.value):
    '''
    A source is a logical grouping of resources i.e. endpoints of a single API.
    - A source can optionally define a schema with tables, columns, performance hints and more.
    - The source Python module typically contains optional customizations and data transformations.
    '''
    return sqlserver_pipeline_resource(api_secret_key)


def _create_auth_headers(api_secret_key):
    """Constructs Bearer type authorization header which is the most common authorization method"""
    headers = {"Authorization": f"Bearer {api_secret_key}"}
    return headers


@dlt.resource(write_disposition="append")
def sqlserver_pipeline_resource(api_secret_key=dlt.secrets.value):
    '''
    A resource is a function that yields data.
    - name: The name of the table generated by this resource. Defaults to decorated function name.
    - write_disposition: How should the data be loaded at destination? Currently, supported: append, replace and merge. 
        Defaults to append.
    '''
    headers = _create_auth_headers(api_secret_key)

    # check if authentication headers look fine
    print(headers)

    # test data for loading validation, delete it once you yield actual data
    test_data = [{"id": 1, "name": "Vikas"}, {"id": 1, "Name": "Ujjwal"}, {"id": 3}]
    yield test_data


if __name__ == "__main__":
    # configure the pipeline with your destination details
    pipeline = dlt.pipeline(
        pipeline_name='sqlserver_pipeline', destination='mssql', dataset_name='sqlserver_pipeline_data'
    )

    # print credentials by running the resource
    data = list(sqlserver_pipeline_resource())

    # print the data yielded from resource
    print(data)

    # run the pipeline with your parameters
    load_info = pipeline.run(sqlserver_pipeline_source())

    # pretty print the information on data that was loaded
    print(load_info)