from msgraph import GraphServiceClient

async def get_tenent_data(credential):
    graph_client = GraphServiceClient(credentials=credential)
    tenent = await graph_client.tenant_relationships.find_tenant_information_by_tenant_id_with_tenant_id(credential._tenant_id).get()
    return {
        "tenent_id" : tenent.tenant_id,
        "tenent_name" : tenent.display_name
    }