from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import (
    QueryDefinition, QueryTimePeriod, QueryDataset,
    QueryAggregation,TimeframeType
)
from datetime import timezone, datetime


def usageQuantity(scope, credential,  grouping, from_date, to_date, granularity, filtering=None):
    costManagement = CostManagementClient(credential=credential)
    response = {}
    query = QueryDefinition(
        type="Usage",
        timeframe=TimeframeType.CUSTOM,
        time_period=QueryTimePeriod(
            from_property=datetime.strptime(str(from_date), "%Y-%m-%d").replace(tzinfo=timezone.utc),
            to=datetime.strptime(str(to_date), "%Y-%m-%d").replace(tzinfo=timezone.utc)
        ),
        dataset=QueryDataset(
            granularity=granularity,
            aggregation={"usageQuantity": QueryAggregation(name="UsageQuantity", function="Sum")},
            grouping=grouping,
            filter=filtering
        )
    )

    query_response = costManagement.query.usage(scope=scope,parameters=query)

    columns = [column.name for column in query_response.columns]

    response.update({
            #"query_id": query_response.id,
            "column":columns,
            "row":query_response.rows
        })
    
    return response