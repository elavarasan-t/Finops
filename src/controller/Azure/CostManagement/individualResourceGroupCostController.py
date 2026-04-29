from utils import AzureCostManagement
from utils import DataSetMethods


def get_resource_group_cost(scope, credential, grouping, cost_type, start_date, end_date, granularity):

    azure_cost = AzureCostManagement(
        scope=scope,
        credential=credential,
        grouping=DataSetMethods.grouping(grouping_term="ResourceGroupCost"),
        cost_type=cost_type,
        from_date=start_date,
        to_date=end_date,
        granularity=granularity
    )

    cost = azure_cost.costManagement()
    resource_group_name = scope.split('/')[4]

    columns = cost.get("column",[])
    rows = cost.get("row", [])

    id_pretaxcost = columns.index("PreTaxCost")
    id_pretaxcost_usd = columns.index("PreTaxCostUSD")
    id_resource_location = columns.index("ResourceLocation")
    id_service_family = columns.index("ServiceFamily")
    id_service_name = columns.index("ServiceName")
    id_meter_cat = columns.index("MeterCategory")
    id_meter_sub = columns.index("MeterSubCategory")
    id_meter = columns.index("Meter")
    id_product = columns.index("Product")
    id_unitofmeasure = columns.index("UnitOfMeasure")
    id_pricingmodel = columns.index("PricingModel")
    id_charge_type = columns.index("ChargeType")
    id_currency = columns.index("Currency")


    response = {
        resource_group_name : []
    }

    for row in rows:

        pretaxcost = row[id_pretaxcost]
        pretaxcost_usd = row[id_pretaxcost_usd]
        resource_location = row[id_resource_location]
        service_family = row[id_service_family]
        service_name = row[id_service_name]
        meter_category = row[id_meter_cat]
        meter_subcategory = row[id_meter_sub]
        meter = row[id_meter]
        product = row[id_product]
        unitofmeasure = row[id_unitofmeasure]
        pricingmodel = row[id_pricingmodel]
        charge_type = row[id_charge_type]
        currency = row[id_currency]
        
        
        response[resource_group_name].append({
            "pretaxcost" : pretaxcost,
            "currency": currency,
            "pretaxcost_USD": pretaxcost_usd,
            "resourceLocation": resource_location,
            "serviceFamily": service_family,
            "serviceName": service_name,
            "meterCategory": meter_category,
            "meterSubCategory": meter_subcategory,
            "meter": meter,
            "product": product,
            "unitofmeasure": unitofmeasure,
            "pricingmodel": pricingmodel,
            "charge_type": charge_type
        })

    return response