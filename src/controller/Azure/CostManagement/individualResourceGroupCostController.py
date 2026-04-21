from utils import costManagement
from utils import DataSetMethods


def get_resource_group_cost(scope, credential, grouping, cost_type, start_date, end_date, granularity):
     
    request = {}

    cost = costManagement(
        scope=scope,
        credential=credential,
        grouping=DataSetMethods.grouping(grouping_term=grouping),
        cost_type=cost_type,
        from_date=start_date,
        to_date=end_date,
        granularity=granularity
    )

    request.update({
         "resource_group_name" : scope.split('/')[4],
         "cost": cost
    })

    return request