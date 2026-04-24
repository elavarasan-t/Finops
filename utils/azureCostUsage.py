from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import (
    QueryDefinition, QueryTimePeriod, QueryDataset,
    QueryAggregation,TimeframeType
)
from datetime import timezone, datetime

class AzureCostUsage:

    def __init__(self, scope, credential, grouping, cost_type, from_date, to_date, granularity, filtering=None):
        self.scope = scope
        self.credential = credential
        self.grouping = grouping
        self.cost_type = cost_type
        self.from_date = from_date
        self.to_date = to_date
        self.granularity = granularity
        self.filtering = filtering

    def costUsage(self):
        response = {}
        costMgmt = CostManagementClient(credential=self.credential)
        query_cost = QueryDefinition(
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
    
        query_usage = QueryDefinition(
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

        cost_query_response = costMgmt.query.usage(scope=self.scope,parameters=query_cost)
        usage_query_response = costMgmt.query.usage(scope=self.scope,parameters=query_usage)

        cost_columns = [column.name for column in cost_query_response.columns]
        usage_columns = [column.name for column in usage_query_response.columns]

        cost_columns.insert(2, usage_columns[0])

        cost_rows = [row for row in cost_query_response.rows]
        usage_rows = [row for row in usage_query_response.rows]

        cost_usage_row = []

        for cost_row, usage_row in zip(cost_rows, usage_rows):
            cost_row.insert(2, usage_row[0])
            cost_usage_row.append(cost_row) 

        response.update({
            "column":cost_columns,
            "row": cost_usage_row
        })
    
        return response