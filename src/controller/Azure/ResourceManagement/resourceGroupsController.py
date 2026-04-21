from azure.mgmt.resource import ResourceManagementClient

def get_azure_resourge_groups(credentials, subscription_id):
    resource_groups = []
    resourceGroups = ResourceManagementClient(credential=credentials, subscription_id=subscription_id)
    for rg in resourceGroups.resource_groups.list():
        resource_groups.append({
            "id":rg.id,
            "name": rg.name,
            "type": rg.type,
            "location": rg.location,
            "provisioning_state": rg.properties.provisioning_state,
            "tags": rg.tags 
        })
    return resource_groups