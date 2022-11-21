import uuid
from typing import Protocol

from jenplane_backend.domain.organization import Organization


class OrganizationRepository(Protocol):
    def next_id(self) -> uuid:
        return uuid.uuid4()

    def find_all(self) -> list[Organization]:
        """
        Retrieve all organizations.

        :returns: A list of organizations, or an empty list if no organizations exist.
        """
        raise NotImplementedError

    def find_by_id(self, organization_id: str) -> Organization | None:
        """
        Find an organization by its ID.

        :param organization_id: The organization ID to be looked up
        :returns: the organization, or None if not found.
        """
        raise NotImplementedError

    def save(self, organization) -> None:
        """
        Saves the current state of the organization.

        :param organization: The organization to be saved.
        """
        raise NotImplementedError

    def delete(self, organization_id: str) -> None:
        """
        Delete the given organization.

        :param organization_id:
        """
        raise NotImplementedError
