import pytest
from datetime import datetime
from main import User, Subscription, BasicPlan, PremiumPlan, FamilyPlan

@pytest.fixture
def sample_user():
    return User(first_name="Ayşe", last_name="Yılmaz", email="ayse@example.com")

@pytest.fixture
def plans():
    basic = BasicPlan(price=9.99, duration_months=1)
    premium = PremiumPlan(price=19.99, duration_months=1, extra_features=["HD","Offline"])
    family = FamilyPlan(price=29.99, duration_months=1, number_users=4)
    return [basic, premium, family]

def test_user_subscriptions(sample_user, plans):
    user = sample_user
    subscriptions = [Subscription(user_id=user.user_id, plan=p, start_date=datetime.now()) for p in plans]
    user.subscriptions.extend(subscriptions)

    fees = [sub.plan.calculate_fee() for sub in user.subscriptions]
    assert fees == [9.99, 19.99, 119.96]