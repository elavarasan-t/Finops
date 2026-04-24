from utils import AzureCostUsage
from utils import DataSetMethods

def get_azure_cost_usage(scope, credential, grouping, cost_type, start_date, end_date, granularity):

    azure_cost_usage = AzureCostUsage(
                scope=scope,
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term=grouping),
                cost_type=cost_type,
                from_date=start_date,
                to_date=end_date,
                granularity=granularity
            )
    
    cost_usage = azure_cost_usage.costUsage()

    return cost_usage