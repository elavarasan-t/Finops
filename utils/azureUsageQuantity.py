from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import (
    QueryDefinition, QueryTimePeriod, QueryDataset,
    QueryAggregation,TimeframeType
)
from datetime import timezone, datetime

class AzureUsageQuantity:

    def __init__(self, scope, credential, grouping,  from_date, to_date, granularity, filtering=None):
        self.scope = scope
        self.credential = credential
        self.grouping = grouping
        self.from_date = from_date
        self.to_date = to_date
        self.granularity = granularity
        self.filtering = filtering

    def usageQuantity(self):
        costManagement = CostManagementClient(credential=self.credential)
        response = {}
        query = QueryDefinition(
            type="Usage",
            timeframe=TimeframeType.CUSTOM,
            time_period=QueryTimePeriod(
                from_property=datetime.strptime(str(self.from_date), "%Y-%m-%d").replace(tzinfo=timezone.utc),
                to=datetime.strptime(str(self.to_date), "%Y-%m-%d").replace(tzinfo=timezone.utc)
            ),
        dataset=QueryDataset(
            granularity=self.granularity,
            aggregation={"usageQuantity": QueryAggregation(name="UsageQuantity", function="Sum")},
            grouping=self.grouping,
            filter=self.filtering
            )
        )

        query_response = costManagement.query.usage(scope=self.scope,parameters=query)

        columns = [column.name for column in query_response.columns]

        response.update({
                #"query_id": query_response.id,
                "column":columns,
                "row":query_response.rows
            })
    
        return response