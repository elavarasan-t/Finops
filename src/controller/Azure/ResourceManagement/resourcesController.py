from azure.mgmt.resource import ResourceManagementClient

def get_azure_resources(credentials, resource_group_id):
    resources = ResourceManagementClient(credential=credentials, subscription_id=resource_group_id.split('/')[2])
    resources_data = [rs.as_dict() for rs in resources.resources.list_by_resource_group(resource_group_name= resource_group_id.split('/')[4])]
    return resources_data