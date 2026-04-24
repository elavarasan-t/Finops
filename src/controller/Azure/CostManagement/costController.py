from utils import DataSetMethods
from utils import AzureCostManagement

def get_azure_cost(scope, credential, grouping, cost_type, start_date, end_date, granularity):
    
    request = {}

    azure_cost = AzureCostManagement(
                scope=scope,
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term=grouping),
                cost_type=cost_type,
                from_date=start_date,
                to_date=end_date,
                granularity=granularity
            )
    
    cost = azure_cost.costManagement()

    total_cost = sum(row[0] for row in cost.get("row", []))
    total_cost_usd = sum(row[1] for row in cost.get("row", []))

    request.update({
            "subscription_id":scope.split('/')[2],
            "subscription_total_cost": round(total_cost, 2),
            "subscription_total_cost_USD":  round(total_cost_usd, 2)
        })

    if grouping != None or granularity != None:
        request.update({
            "cost": cost
        })

    return request