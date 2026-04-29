from azure.mgmt.costmanagement.models import QueryGrouping, QueryFilter, QueryComparisonExpression

class DataSetMethods:

    def filterting(filtering_term, resource_id = None):
        if filtering_term == "eventgrid":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["Event Grid"]))

        if filtering_term == "web":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["Web"]))
        
        if filtering_term == "logic":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["Logic"]))
        
        if filtering_term == "insights":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["Insights"]))
        
        if filtering_term == "migrate":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["Migrate"]))
        
        if filtering_term == "dependencymap":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["DependencyMap"]))
        
        if filtering_term == "applicationmigration":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["ApplicationMigration"]))
        
        if filtering_term == "mysqldiscovery":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["MySqlDiscovery"]))
        
        if filtering_term == "recoveryservices":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["RecoveryServices"]))
        
        if filtering_term == "offazure":
            return QueryFilter(dimensions=QueryComparisonExpression( name="MeterCategory",operator="In",values=["OffAzure"]))

        return QueryFilter(dimensions=QueryComparisonExpression( name="ResourceId",operator="In",values=[resource_id]))
    
    def grouping(grouping_term):

        if grouping_term == "None":
            return []

        if grouping_term == "ResourceGroup":
            return [QueryGrouping(type="Dimension", name="ResourceGroup")]
        
        if grouping_term == "ResourceId":
            return [QueryGrouping(type="Dimension", name="ResourceId")]

        if grouping_term == "ServiceName":
            return [QueryGrouping(type="Dimension", name="ServiceName")]

        if grouping_term == "ServiceFamily":
            return [QueryGrouping(type="Dimension", name="ServiceFamily"),
                    QueryGrouping(type="Dimension", name="UnitOfMeasure")]
        
        if grouping_term == "MeterCategory":
            return [QueryGrouping(type="Dimension", name="MeterCategory")]
        
        if grouping_term == "MeterSubCategory":
            return [QueryGrouping(type="Dimension", name="MeterSubcategory")]
        
        if grouping_term == "Meter":
            return [QueryGrouping(type="Dimension", name="Meter")]

        if grouping_term == "Product":
            return [QueryGrouping(type="Dimension", name="Product")]
        
        if grouping_term == "Location":
            return [QueryGrouping(type="Dimension", name="ResourceLocation")]
         
        if grouping_term == "CostAllocation":
            return [QueryGrouping(type="Dimension", name="CostAllocationRuleName")]   

        if grouping_term == "PricingModel":
            return [QueryGrouping(type="Dimension", name="PricingModel")]     
        
        if grouping_term == "RGS":
            return  [QueryGrouping(type="Dimension", name="ResourceGroup"),
                    QueryGrouping(type="Dimension", name="ServiceName")]
         
        if grouping_term == "RGRID":
            return [QueryGrouping(type="Dimension", name="ResourceGroup"),
                     QueryGrouping(type="Dimension", name="ResourceId")]

        if grouping_term == "RIDMC":
            return [QueryGrouping(type="Dimension", name="ResourceId"),
                    QueryGrouping(type="Dimension", name="MeterCategory")]
        
        if grouping_term == "Usage":
            return [QueryGrouping(type="Dimension", name="MeterCategory"),
                    QueryGrouping(type="Dimension", name="UnitOfMeasure")]
        
        if grouping_term == "Service":
            return [QueryGrouping(type="Dimension", name="MeterCategory"),
                    QueryGrouping(type="Dimension", name="ServiceFamily"),
                    QueryGrouping(type="Dimension", name="ResourceId")]

        if grouping_term == "RGRIDS":
            return [QueryGrouping(type="Dimension", name="ResourceGroup"),
                     QueryGrouping(type="Dimension", name="ResourceId"),
                     QueryGrouping(type="Dimension", name="ServiceName")]
        
        if grouping_term == "ResourceInfo":
            return [QueryGrouping(type="Dimension", name="ResourceGroup"),
                     QueryGrouping(type="Dimension", name="ResourceId")]
        
        if grouping_term == "MeterInfo":
            return [QueryGrouping(type="Dimension", name="MeterCategory"),
                     QueryGrouping(type="Dimension", name="MeterSubCategory"),
                     QueryGrouping(type="Dimension", name="Meter")]
        
        if grouping_term == "BillingInfo":
            return [QueryGrouping(type="Dimension", name="SubscriptionId"),
                     QueryGrouping(type="Dimension", name="BillingAccountName"),
                     QueryGrouping(type="Dimension", name="BillingProfileId"),
                     QueryGrouping(type="Dimension", name="BillingProfileName"),
                     QueryGrouping(type="Dimension", name="InvoiceSection"),
                     QueryGrouping(type="Dimension", name="InvoiceSectionId"),
                     QueryGrouping(type="Dimension", name="InvoiceSectionName"),
                    ]
        
        if grouping_term == "CustomerInfo":
            return [QueryGrouping(type="Dimension", name="SubscriptionId"),
                     QueryGrouping(type="Dimension", name="CustomerName"),
                     QueryGrouping(type="Dimension", name="PartnerName")]
        
        if grouping_term == "ServiceInfo":
            return [QueryGrouping(type="Dimension", name="ServiceFamily"),
                    QueryGrouping(type="Dimension", name="ServiceName")]
        
        if grouping_term == "SubscriptionCost":
            return [QueryGrouping(type="Dimension", name="ResourceLocation"),
                     QueryGrouping(type="Dimension", name="ResourceGroupName"),
                     QueryGrouping(type="Dimension", name="ResourceId"),
                     QueryGrouping(type="Dimension", name="ServiceFamily"),
                     QueryGrouping(type="Dimension", name="ServiceName"),
                     QueryGrouping(type="Dimension", name="MeterCategory"),
                     QueryGrouping(type="Dimension", name="MeterSubCategory"),
                     QueryGrouping(type="Dimension", name="Meter"),
                     QueryGrouping(type="Dimension", name="Product"),
                     QueryGrouping(type="Dimension", name="UnitOfMeasure"),
                     QueryGrouping(type="Dimension", name="PricingModel"),
                     QueryGrouping(type="Dimension", name="ChargeType")
                    ]
        
        if grouping_term == "ResourceGroupCost":
            return [QueryGrouping(type="Dimension", name="ResourceLocation"),
                     QueryGrouping(type="Dimension", name="ServiceFamily"),
                     QueryGrouping(type="Dimension", name="ServiceName"),
                     QueryGrouping(type="Dimension", name="MeterCategory"),
                     QueryGrouping(type="Dimension", name="MeterSubCategory"),
                     QueryGrouping(type="Dimension", name="Meter"),
                     QueryGrouping(type="Dimension", name="Product"),
                     QueryGrouping(type="Dimension", name="UnitOfMeasure"),
                     QueryGrouping(type="Dimension", name="PricingModel"),
                     QueryGrouping(type="Dimension", name="ChargeType")
                    ]
        
        if grouping_term == "ResourceCost":
            return [QueryGrouping(type="Dimension", name="ResourceLocation"),
                     QueryGrouping(type="Dimension", name="ServiceFamily"),
                     QueryGrouping(type="Dimension", name="ServiceName"),
                     QueryGrouping(type="Dimension", name="MeterCategory"),
                     QueryGrouping(type="Dimension", name="MeterSubCategory"),
                     QueryGrouping(type="Dimension", name="Meter"),
                     QueryGrouping(type="Dimension", name="Product"),
                     QueryGrouping(type="Dimension", name="UnitOfMeasure"),
                     QueryGrouping(type="Dimension", name="PricingModel"),
                     QueryGrouping(type="Dimension", name="ChargeType")
                    ]
 

        #if grouping_term == "All":
            return [
                QueryGrouping(type="Dimension", name="ResourceGroup"),
                QueryGrouping(type="Dimension", name="ResourceId"),
                QueryGrouping(type="Dimension", name="ServiceFamily"),
                QueryGrouping(type="Dimension", name="ServiceName"),
                QueryGrouping(type="Dimension", name="MeterCategory"),
                QueryGrouping(type="Dimension", name="MeterSubCategory"),
                QueryGrouping(type="Dimension", name="Meter"),
                QueryGrouping(type="Dimension", name="UnitOfMeasure"),
                QueryGrouping(type="Dimension", name="Product"),
                QueryGrouping(type="Dimension", name="PricingModel"),
                QueryGrouping(type="Dimension", name="ResourceGuId"),
                QueryGrouping(type="Dimension", name="ProductOrderId"),
                QueryGrouping(type="Dimension", name="BillingAccountName"),
                QueryGrouping(type="Dimension", name="BillingProfileId"),
                QueryGrouping(type="Dimension", name="BillingProfileName"),
                QueryGrouping(type="Dimension", name="InvoiceSection"),
                QueryGrouping(type="Dimension", name="InvoiceSectionId"),
                QueryGrouping(type="Dimension", name="InvoiceSectionName"),
                QueryGrouping(type="Dimension", name="PublisherType"),
                QueryGrouping(type="Dimension", name="Frequency"),
                QueryGrouping(type="Dimension", name="ReservationId"),
                QueryGrouping(type="Dimension", name="ReservationName"),
                QueryGrouping(type="Dimension", name="InvoiceId"),
                QueryGrouping(type="Dimension", name="CostAllocationRuleName"),
                QueryGrouping(type="Dimension", name="MarkupRuleName"),
                QueryGrouping(type="Dimension", name="BillingMonth"),
                QueryGrouping(type="Dimension", name="Provider"),
                QueryGrouping(type="Dimension", name="BenefitId"),
                QueryGrouping(type="Dimension", name="BenefitName"),
                QueryGrouping(type="Dimension", name="CustomerTenantId"),
                QueryGrouping(type="Dimension", name="CustomerTenantDomainName"),
                QueryGrouping(type="Dimension", name="PartnerEarnedCreditApplied"),
                QueryGrouping(type="Dimension", name="CustomerName"),
                QueryGrouping(type="Dimension", name="PartnerName")
            ]