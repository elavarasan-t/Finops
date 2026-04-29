from utils import DataSetMethods
from utils import AzureUsageQuantity

def get_individual_resource_usage(scope, credential, grouping, start_date, end_date, granularity):
    
    filter_term = str(scope.split('/providers')[1].split('.')[1].split('/')[0]).lower()

    azure_usage = AzureUsageQuantity(
                scope=scope.split('/providers')[0],
                credential=credential,
                grouping=DataSetMethods.grouping(grouping_term="ResourceCost"),
                from_date=start_date,
                to_date=end_date,
                granularity=granularity,
                filtering=DataSetMethods.filterting(filtering_term=str(filter_term), resource_id= scope.lower())
            )
    
    usage = azure_usage.usageQuantity()

    resource_name = scope.split('/')[-1]

    columns = usage.get("column",[])
    rows = usage.get("row", [])

    id_usage_quantity = columns.index("UsageQuantity")
    id_resource_location = columns.index("ResourceLocation")
    id_service_family = columns.index("ServiceFamily")
    id_service_name = columns.index("ServiceName")
    id_meter_cat = columns.index("MeterCategory")
    id_meter_sub = columns.index("MeterSubCategory")
    id_meter = columns.index("Meter")
    id_product = columns.index("Product")
    id_unitofmeasure = columns.index("UnitOfMeasure")

    response = {
        resource_name : { }
    }

    for row in rows:

        usage_quantity = row[id_usage_quantity]
        resource_location = row[id_resource_location]
        service_family = row[id_service_family]
        service_name = row[id_service_name]
        meter_category = row[id_meter_cat]
        meter_subcategory = row[id_meter_sub]
        meter = row[id_meter]
        product = row[id_product]
        unitofmeasure = row[id_unitofmeasure]

        response[resource_name] = {
            resource_name: []
            }
  
        response[resource_name].append({
            "usage_quantity": usage_quantity,
            "resourceLocation": resource_location,
            "serviceFamily": service_family,
            "serviceName": service_name,
            "meterCategory": meter_category,
            "meterSubCategory": meter_subcategory,
            "meter": meter,
            "product": product,
            "unitofmeasure": unitofmeasure
        })

    return response
