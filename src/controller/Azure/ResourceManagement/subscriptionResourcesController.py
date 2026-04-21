from azure.mgmt.resource import ResourceManagementClient


def get_azure_subscription_resources(credentials, subscription_id):
    resources = []
    resourceGroup = ResourceManagementClient(credential=credentials, subscription_id=subscription_id)
    for rs in resourceGroup.resources.list():
        resources.append({
            "id":rs.id
        })
    return resources