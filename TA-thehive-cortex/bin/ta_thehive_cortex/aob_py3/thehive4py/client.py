from typing import Optional

from thehive4py.endpoints import (
    AlertEndpoint,
    CaseEndpoint,
    CommentEndpoint,
    ObservableEndpoint,
    OrganisationEndpoint,
    ProcedureEndpoint,
    ProfileEndpoint,
    TaskEndpoint,
    TaskLogEndpoint,
    TimelineEndpoint,
    UserEndpoint,
)
from thehive4py.endpoints.cortex import CortexEndpoint
from thehive4py.endpoints.custom_field import CustomFieldEndpoint
from thehive4py.endpoints.observable_type import ObservableTypeEndpoint
from thehive4py.endpoints.query import QueryEndpoint
from thehive4py.session import DEFAULT_RETRY, RetryValue, TheHiveSession


class TheHiveApi:
    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        organisation: Optional[str] = None,
        proxies={},
        verify=None,
        cert=None,
        max_retries: RetryValue = DEFAULT_RETRY
    ):
        self.session = TheHiveSession(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            proxies=proxies,
            verify=verify,
            cert=cert,
            max_retries=max_retries
        )
        self.session_organisation = organisation

        # case management endpoints
        self.alert = AlertEndpoint(self.session)
        self.case = CaseEndpoint(self.session)
        self.comment = CommentEndpoint(self.session)
        self.observable = ObservableEndpoint(self.session)
        self.procedure = ProcedureEndpoint(self.session)
        self.task = TaskEndpoint(self.session)
        self.task_log = TaskLogEndpoint(self.session)
        self.timeline = TimelineEndpoint(self.session)

        # user management endpoints
        self.user = UserEndpoint(self.session)
        self.organisation = OrganisationEndpoint(self.session)
        self.profile = ProfileEndpoint(self.session)

        # entity endpoints
        self.custom_field = CustomFieldEndpoint(self.session)
        self.observable_type = ObservableTypeEndpoint(self.session)

        # connector endpoints
        self.cortex = CortexEndpoint(self.session)

        # standard endpoints
        self.query = QueryEndpoint(self.session)

    @property
    def session_organisation(self) -> Optional[str]:
        return self.session.headers.get("X-Organisation")  # type:ignore

    @session_organisation.setter
    def session_organisation(self, organisation: Optional[str] = None):
        if organisation:
            self.session.headers["X-Organisation"] = organisation
        else:
            self.session.headers.pop("X-Organisation", None)
