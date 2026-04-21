from azure.mgmt.subscription import SubscriptionClient
from utils import costManagement
from utils import DataSetMethods
from datetime import  timezone, datetime
import calendar

def get_subscriptions_cost(credential):
    today = datetime.now(timezone.utc).date()
    start_date = today.replace(day=1)
    last_day = calendar.monthrange(today.year, today.month)[1]
    end_date = today.replace(day=last_day)

    response = {
        "subscription":[]
    }
        
    subscriptions = SubscriptionClient(credential=credential)
    for subscription in subscriptions.subscriptions.list():
        subscription_data = {}
        subscription_data.update({
        "subscription_id":subscription.id,
        "subscription_name":subscription.display_name,
        "state":subscription.state,
        "totalCost":costManagement(
            scope=subscription.id,
            cost_type="ActualCost",
            from_date=start_date,
            to_date=end_date,
            granularity="NONE",
            grouping=DataSetMethods.grouping(grouping_term="None"),
            credential=credential
            ),   
        "subscription_policies":subscription.subscription_policies.__dict__,
        "authorization_source":subscription.authorization_source
        })
        
        response["subscription"].append(subscription_data)
    
    return response