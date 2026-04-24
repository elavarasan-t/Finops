from utils import DataSetMethods
from finOpsAzure.utils import azureUsageQuantity

def get_individual_resource_usage(scope, credential, grouping, start_date, end_date, granularity):
    
    filter_term = str(scope.split('/providers')[1].split('.')[1].split('/')[0]).lower()

    response = azureUsageQuantity(
                scope=scope.split('/providers')[0],
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term="ResourceId"),
                from_date=start_date,
                to_date=end_date,
                granularity=granularity,
                filtering=DataSetMethods.filterting(filtering_term=str(filter_term), resource_id= scope.lower())
            )

    return response