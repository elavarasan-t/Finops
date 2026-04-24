from utils import AzureCostManagement
from utils import DataSetMethods

def get_individual_resource_cost(scope, credential, grouping, cost_type, start_date, end_date, granularity):
    
    filter_term = str(scope.split('/providers')[1].split('.')[1].split('/')[0]).lower()

    azure_cost = AzureCostManagement(
                scope=scope.split('/providers')[0],
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term="ResourceId"),
                cost_type=cost_type,
                from_date=start_date,
                to_date=end_date,
                granularity=granularity,
                filtering=DataSetMethods.filterting(filtering_term=str(filter_term), resource_id= scope.lower())
            )
    
    cost = azure_cost.costManagement()

    return cost