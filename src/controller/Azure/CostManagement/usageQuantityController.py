from finOpsAzure.utils import azureUsageQuantity
from utils import DataSetMethods

def get_usage(scope, credentials, grouping, start_date, end_date, granularity):
    request = azureUsageQuantity(
        scope=scope,
        credential=credentials,
        grouping=DataSetMethods.grouping(grouping_term=grouping),
        from_date=start_date,
        to_date=end_date,
        granularity=granularity
    )

    return request