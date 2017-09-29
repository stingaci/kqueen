from openbrokerapi import service_broker
from openbrokerapi.api import *
from openbrokerapi.catalog import ServicePlan
from openbrokerapi.log_util import *

logger = basic_config()


class KQueenServiceBroker(service_broker.ServiceBroker):
    def catalog(self) -> List[Service]:
        # DUMMY DATA
        service_plans_dict = [{
            "id": "48d209e5-be7b-40df-a749-4b82857f6e39",
            "name": "Dummy Cluster Small",
            "description": "Only provides small amount of dummies.",
            "metadata": None,
            "free": None,
            "bindable": None
        }]
        service_plans = [ServicePlan(**sp) for sp in service_plans_dict]
        # DUMMY DATA
        services_dict = [{
            "id": "af0f7b7b-5b2f-4c77-a26e-3f21334af92c",
            "name": "Dummy Cluster",
            "description": "Cluster made of plastic dummies.",
            "bindable": True,
            "plans": service_plans,
            "tags": None,
            "requires": None,
            "metadata": None,
            "dashboard_client": None,
            "plan_updateable": False
        }]
        return[Service(**s) for s in services_dict]

    def provision(self, instance_id: str, service_details: ProvisionDetails, async_allowed: bool) -> ProvisionedServiceSpec:
        pass

    def unbind(self, instance_id: str, binding_id: str, details: UnbindDetails):
        pass

    def update(self, instance_id: str, details: UpdateDetails, async_allowed: bool) -> UpdateServiceSpec:
        pass

    def bind(self, instance_id: str, binding_id: str, details: BindDetails) -> Binding:
        pass

    def deprovision(self, instance_id: str, details: DeprovisionDetails, async_allowed: bool) -> DeprovisionServiceSpec:
        pass

    def last_operation(self, instance_id: str, operation_data: str) -> LastOperation:
        pass


oba_api = get_blueprint(KQueenServiceBroker(), BrokerCredentials("",""), logger)

