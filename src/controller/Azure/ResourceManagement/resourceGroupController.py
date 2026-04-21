from azure.mgmt.resource import ResourceManagementClient

def get_azure_resource_group(credentials, resource_group_id):
    resource_group = ResourceManagementClient(credential=credentials, subscription_id=resource_group_id.split('/')[2])
    resource_group_data = resource_group.resource_groups.get(resource_group_name= resource_group_id.split('/')[4])
    return resource_group_data.as_dict()