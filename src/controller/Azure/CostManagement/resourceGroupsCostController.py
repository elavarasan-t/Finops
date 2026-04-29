from utils import AzureCostManagement
from utils import DataSetMethods

def get_resources_groups_cost(scope, credential, grouping, cost_type, start_date, end_date, granularity):

    azure_cost = AzureCostManagement(
                scope=scope,
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term="ResourceGroup"),
                cost_type=cost_type,
                from_date=start_date,
                to_date=end_date,
                granularity=granularity
            )
    
    cost = azure_cost.costManagement()

    subscription_id = scope.split('/')[2] 
    columns = cost.get("column",[])

    id_pretaxcost = columns.index("PreTaxCost")
    id_pretaxcost_usd = columns.index("PreTaxCostUSD")
    id_rg = columns.index("ResourceGroup")
    id_currency = columns.index("Currency")

    response = {
        subscription_id : {}
    }

    for row in cost.get("row", []):

        pretaxcost = row[id_pretaxcost]
        pretaxcost_usd = row[id_pretaxcost_usd]
        resource_group = row[id_rg] or f"unknown-rg"
        currency = row[id_currency]
        
        if resource_group not in response[subscription_id]:
            response[subscription_id][resource_group] = {
                "pretaxcost" : pretaxcost,
                "currency": currency,
                "pretaxcost_USD": pretaxcost_usd,
                }
            
    return response