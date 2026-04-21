from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import (
    QueryDefinition, QueryTimePeriod, QueryDataset,
    QueryAggregation,TimeframeType
)
from datetime import timezone, datetime

def costManagement(scope, credential, grouping, cost_type, from_date, to_date, granularity, filtering=None):
    response = {}
    costMgmt = CostManagementClient(credential=credential)
    query = QueryDefinition(
        type=cost_type,
        timeframe=TimeframeType.CUSTOM,
        time_period=QueryTimePeriod(
            from_property=datetime.strptime(str(from_date), "%Y-%m-%d").replace(tzinfo=timezone.utc),
            to=datetime.strptime(str(to_date), "%Y-%m-%d").replace(tzinfo=timezone.utc)
        ),
        dataset=QueryDataset(
            granularity=granularity,
            aggregation={"totalCost": QueryAggregation(name="PreTaxCost", function="Sum"),
                         "totalCostUSD": QueryAggregation(name="PreTaxCostUSD", function="Sum")
                        },
                        
            grouping=grouping,
            filter=filtering
        )
    )
    
    query_response = costMgmt.query.usage(scope=scope,parameters=query)

    columns = [column.name for column in query_response.columns]

    response.update({
            #"query_id": query_response.id,
            "column":columns,
            "row":query_response.rows
        })
    
    return response