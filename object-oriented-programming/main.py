import uuid
from datetime import datetime


class User:
    def __init__(self,first_name,last_name,email,date_joined=None,is_active=True):
        self.user_id = uuid.uuid4()
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.date_joined=date_joined
        self.is_active=is_active
        self.subscriptions = []


class Subscription():
    def __init__(self,user_id,plan,start_date,end_date=None,is_active=True):
        self.subscription_id=uuid.uuid4()
        self.user_id=user_id
        self.plan=plan
        self.start_date=start_date
        self.end_date=end_date
        self.is_active=is_active

from abc import ABC,abstractmethod

class SubscriptionPlan(ABC):
    def __init__(self,name,price,duration_months):
        self.plan_id=uuid.uuid4()
        self.name=name
        self.price=price
        self.duration_months=duration_months

    @abstractmethod
    def calculate_fee(self):
        pass

class BasicPlan(SubscriptionPlan):
    def __init__(self,price,duration_months):
        super().__init__(name="Basic", price=price, duration_months=duration_months)

    def calculate_fee(self):
        return self.price * self.duration_months

class PremiumPlan(SubscriptionPlan):
    def __init__(self,price,duration_months,extra_features=None):
        super().__init__(name="Premium",price=price,duration_months=duration_months)
        self.extra_features= []

    def calculate_fee(self):
        return self.price * self.duration_months + len(self.extra_features) * 2


class FamilyPlan(SubscriptionPlan):
    def __init__(self,price,duration_months,number_users):
        super().__init__(name="Family",price=price,duration_months=duration_months)
        self.number_users = number_users

    def calculate_fee(self):
        return (self.price * self.duration_months)* self.number_users

