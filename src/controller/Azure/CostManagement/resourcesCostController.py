from utils import costManagement
from utils import DataSetMethods

def get_resources_cost(scope, credential, cost_type, start_date, end_date, granularity):
    request = {}

    cost = costManagement(
                scope=scope,
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term="ResourceId"),
                cost_type=cost_type,
                from_date=start_date,
                to_date=end_date,
                granularity=granularity
            )
    
    resource_cost = sum(row[0] for row in cost["row"])
    resource_cost_usd = sum(row[1] for row in cost["row"])

    request.update({
        "total_Cost": round(resource_cost, 2),
        "total_Cost_USD":  round(resource_cost_usd, 2),
        "resources_cost": cost
    })

    return request