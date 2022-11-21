from unittest.mock import Mock

from jenplane_backend.domain.organization_service import OrganizationService
from jenplane_backend.spi.organizations import OrganizationRepository


def test_list_all_delegates_to_repository(fastapi_dep):
    fake_repo: OrganizationRepository = Mock()
    service = OrganizationService(fake_repo)

    service.list_all()

    fake_repo.find_all.assert_called_with()


def test_list_by_id_delegates_to_repository():
    fake_repo: OrganizationRepository = Mock()
    service = OrganizationService(fake_repo)

    service.list('SOME_ID')

    fake_repo.find_by_id.assert_called_with('SOME_ID')


def test_delete_delegates_to_repository():
    fake_repo: OrganizationRepository = Mock()
    service = OrganizationService(fake_repo)

    service.delete('SOME_ID')

    fake_repo.delete.assert_called_with('SOME_ID')
