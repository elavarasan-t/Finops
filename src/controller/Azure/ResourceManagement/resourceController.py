from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest

def get_azure_ressource(credentials, resource_id):
    subscription_id = resource_id.split('/')[2]
    resource = ResourceGraphClient(credential=credentials)
    query =f""" Resources | where id == '{resource_id}' | project id, name, type, location, resourceGroup, subscriptionId, tags, kind, sku, properties """
    request = QueryRequest(query=query,subscriptions=[subscription_id])
    response = resource.resources(request)
    return response.data