from utils import AzureCostManagement
from utils import DataSetMethods

def get_subscription_cost(scope, credential, grouping, cost_type, start_date, end_date, granularity):
    
    request = {}

    azure_cost = AzureCostManagement(
                scope=scope,
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term="None"),
                cost_type=cost_type,
                from_date=start_date,
                to_date=end_date,
                granularity=granularity
            )
    
    cost = azure_cost.costManagement()
    
    total_cost_inr = sum(row[0] for row in cost["row"])
    total_cost_usd = sum(row[1] for row in cost["row"])
    
    request.update({
            "subscription_id":scope.split('/')[2],
            "totalCost": round(total_cost_inr, 2),
            "totalCostUSD":  round(total_cost_usd, 2)
        })

    if grouping != "None" or granularity != "None":
        request.update({
            "cost": cost
        })            
            
    return request