from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import (
    ForecastDefinition, QueryTimePeriod, QueryDataset,
    QueryAggregation,TimeframeType
)
from datetime import timezone, datetime


def foreCastCost(scope, credential,  grouping, from_date, to_date, granularity, aggregation_cost ,filtering=None):
    response = {}
    forecastCostMgmt = CostManagementClient(credential=credential)
    forecast_definition  = ForecastDefinition(
        type="Usage",
        timeframe=TimeframeType.CUSTOM,
        time_period=QueryTimePeriod(
            from_property=datetime.strptime(str(from_date), "%Y-%m-%d").replace(tzinfo=timezone.utc),
            to=datetime.strptime(str(to_date), "%Y-%m-%d").replace(tzinfo=timezone.utc)

        ),
        dataset=QueryDataset(
            granularity=granularity,
            aggregation={"totalCost": QueryAggregation(name=aggregation_cost, function="Sum")},
                        
            grouping=grouping,
            filter=filtering
        )
    )

    query_response = forecastCostMgmt.forecast.usage(scope=scope,parameters=forecast_definition)

    columns = [column.name for column in query_response.columns]

    response.update({
            #"query_id": query_response.id,
            "column":columns,
            "row":query_response.rows
        })
    
    return response