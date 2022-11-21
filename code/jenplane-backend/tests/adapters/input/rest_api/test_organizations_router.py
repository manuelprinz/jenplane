from unittest.mock import Mock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from jenplane_backend.adapters.input.rest_api.organizations import router
from jenplane_backend.adapters.input.rest_api.dependencies import organization_use_cases
from jenplane_backend.api.organizations import OrganizationUseCases
from jenplane_backend.domain.organization import Organization

# Only test the organization router. No need to bring up the full app.
app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_read_by_id_not_found(fastapi_dep):
    fake_response: OrganizationUseCases = Mock()
    fake_response.list.return_value = None

    with fastapi_dep(app).override({organization_use_cases: lambda: fake_response}):
        response = client.get("/organizations/TEST_ID")
        assert response.status_code == 404
        assert response.json() == {'detail': 'Organization with ID <TEST_ID> not found'}


def test_read_by_id_found(fastapi_dep):
    test_id = 'TEST_ID'
    fake_response: OrganizationUseCases = Mock()
    fake_response.list.return_value = Organization(
        id=test_id,
        name="Test Organization",
        description="Description of the test organization"
    )

    with fastapi_dep(app).override({organization_use_cases: lambda: fake_response}):
        response = client.get(f"/organizations/{test_id}")
        assert response.status_code == 200
        assert response.json() == {
            'id': test_id,
            'description': 'Description of the test organization',
            'name': 'Test Organization',
        }


def test_delete_should_return_204_and_empty_body(fastapi_dep):
    fake_response: OrganizationUseCases = Mock()
    fake_response.delete.return_value = None

    with fastapi_dep(app).override({organization_use_cases: lambda: fake_response}):
        response = client.delete("/organizations/TEST_ID")
        assert response.status_code == 204
        assert response.text == ""
