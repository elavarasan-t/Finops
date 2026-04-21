from msgraph import GraphServiceClient

async def get_tenent_data(credential):
    graph_client = GraphServiceClient(credentials=credential)
    tenant = await graph_client.tenant_relationships.find_tenant_information_by_tenant_id_with_tenant_id(credential._tenant_id).get()
    return {
        "tenant_id" : tenant.tenant_id,
        "tenant_name" : tenant.display_name
    }