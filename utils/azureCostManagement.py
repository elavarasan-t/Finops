from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import (
    QueryDefinition, QueryTimePeriod, QueryDataset,
    QueryAggregation,TimeframeType
)
from datetime import timezone, datetime

class AzureCostManagement:

    def __init__(self, scope, credential, grouping, cost_type, from_date, to_date, granularity, filtering=None):
        self.scope = scope
        self.credential = credential
        self.grouping = grouping
        self.cost_type = cost_type
        self.from_date = from_date
        self.to_date = to_date
        self.granularity = granularity
        self.filtering = filtering

    def costManagement(self):
        response = {}
        costMgmt = CostManagementClient(credential=self.credential)
        query = QueryDefinition(
            type=self.cost_type,
            timeframe=TimeframeType.CUSTOM,
            time_period=QueryTimePeriod(
                from_property=datetime.strptime(str(self.from_date), "%Y-%m-%d").replace(tzinfo=timezone.utc),
                to=datetime.strptime(str(self.to_date), "%Y-%m-%d").replace(tzinfo=timezone.utc)
            ),
            dataset=QueryDataset(
                granularity=self.granularity,
                aggregation={"totalCost": QueryAggregation(name="PreTaxCost", function="Sum"),
                         "totalCostUSD": QueryAggregation(name="PreTaxCostUSD", function="Sum")
                            },
                        
                grouping=self.grouping,
                filter=self.filtering
            )
        )
    
        query_response = costMgmt.query.usage(scope=self.scope,parameters=query)

        columns = [column.name for column in query_response.columns]

        response.update({
                #"query_id": query_response.id,
                "column":columns,
                "row":query_response.rows
            })
    
        return response