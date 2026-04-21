from azure.mgmt.subscription import SubscriptionClient

def get_azure_subscriptions(credentials):
    subscriptions = SubscriptionClient(credential=credentials)
    subscriptions_data = [subscription.as_dict() for subscription in subscriptions.subscriptions.list()]
    return subscriptions_data