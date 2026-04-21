from utils import foreCastCost
from utils import DataSetMethods

def get_azure_forecast_cost(scope, credential, grouping, start_date, end_date, granularity):

    request = {}
    
    forecast_inr = foreCastCost(
                scope=scope,
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term=grouping),
                aggregation_cost="PreTaxCost",
                from_date=start_date,
                to_date=end_date,
                granularity=granularity
            )
    
    forecast_cost = sum(row[0] for row in forecast_inr["row"])

    forecast_usd = foreCastCost(
                scope=scope,
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term=grouping),
                aggregation_cost="PreTaxCostUSD",
                from_date=start_date,
                to_date=end_date,
                granularity=granularity
            )
    
    forecast_cost_usd = sum(row[0] for row in forecast_usd["row"])

    request.update({
            "forecast_cost_inr": round(forecast_cost, 2),
            "forecast_cost_usd": round(forecast_cost_usd, 2)
        })

    return request