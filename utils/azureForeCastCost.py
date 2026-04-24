from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import (
    ForecastDefinition, QueryTimePeriod, QueryDataset,
    QueryAggregation,TimeframeType
)
from datetime import timezone, datetime

class AzureForecastCost:
    def __init__(self, scope, credential, grouping, from_date, to_date, granularity, aggregation_cost, filtering=None):
        self.scope = scope
        self.credential = credential
        self.grouping = grouping
        self.from_date = from_date
        self.to_date = to_date
        self.granularity = granularity
        self.aggregation_cost = aggregation_cost
        self.filtering = filtering

    def foreCastCost(self):
        response = {}
        forecastCostMgmt = CostManagementClient(credential=self.credential)
        forecast_definition  = ForecastDefinition(
            type="Usage",
            timeframe=TimeframeType.CUSTOM,
            time_period=QueryTimePeriod(
                from_property=datetime.strptime(str(self.from_date), "%Y-%m-%d").replace(tzinfo=timezone.utc),
                to=datetime.strptime(str(self.to_date), "%Y-%m-%d").replace(tzinfo=timezone.utc)
            ),
            dataset=QueryDataset(
                granularity=self.granularity,
                aggregation={"totalCost": QueryAggregation(name=self.aggregation_cost, function="Sum")},
                    
                grouping=self.grouping,
                filter=self.filtering
            )
        )

        query_response = forecastCostMgmt.forecast.usage(scope=self.scope,parameters=forecast_definition)

        columns = [column.name for column in query_response.columns]

        response.update({
                #"query_id": query_response.id,
                "column":columns,
                "row":query_response.rows
            })
    
        return response