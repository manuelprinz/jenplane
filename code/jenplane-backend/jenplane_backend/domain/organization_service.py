from jenplane_backend.api.organizations import OrganizationUseCases
from jenplane_backend.domain.organization import Organization
from jenplane_backend.spi.organizations import OrganizationRepository


class OrganizationService(OrganizationUseCases):
    def __init__(self, repository: OrganizationRepository) -> None:
        # Constructor required for FastAPI
        self._repo = repository

    # TODO: This assumes the client can generate IDs, but it should most likely be done by the repo.
    #       In this case, only the parameters should be given and the controller interface should be changed.
    def create(self, organization: Organization) -> str:
        return ""  # FIXME: implementation

    def list_all(self) -> list[Organization]:
        return self._repo.find_all()

    def list(self, organization_id: str) -> Organization | None:
        return self._repo.find_by_id(organization_id)

    def delete(self, organization_id: str) -> None:
        return self._repo.delete(organization_id)
