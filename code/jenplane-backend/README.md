# `jenplane_backend` – Alternative Backend Implementation

Status: Prototype

This project provides a prototype implementation of the service using Hexagonal Architecture.

It uses [Poetry](https://python-poetry.org/) as a build tool, and [FastAPI](https://fastapi.tiangolo.com/) as web framework (currently synchronous).

## Running locally

Dependent software can be started with `docker compose -d up`.

Run with: `poetry uvicorn jenplane_backend.rest_api:app --reload`

## Architecture

This service is implemented using *Hexagonal Architecture* (HA), also known as *Ports & Adapters*. 
More information can be found in the references below.

It achieves separation of concerns by applying the *Dependency Inversion Principle* to the boundaries of the domain.
The main advantage is that the domain is isolated, and therefore fully unit-testable.
In addition, all technology becomes essentially a "plugin" to the system, making it easy to upgrade and replace, as long as adapters adhere to the contracts of the ports.
This can be verified by implementing contract tests against the port interfaces.

### Code organization

The code has been separated into the 5 main components of HA:

* The `domain` package contains all domain code, i.e. domain objects and services.
* The `api` (Application Programming Interface) package contains all input port definitions (aka "driving ports").
  These interfaces are named "use cases" because they should represent the use case operations and act as the entry point into your domain.
* The `spi` (Service Provider Interface) package contains all output port definitions (aka "driven ports").
  These interfaces represent services that the domain needs, such as  persisting or querying information (repositories) or querying a service.
* The `input` package contains all input adapter implementations, e.g. the REST controllers for a REST API.
  All implementations only call API interfaces or domain code.
* The `output` package contains all output adapter implementations, e.g. persistence to a database.
  All adapters have to implement API interfaces and provide only domain objects.
  If they are not working with domain objects directly, mapping needs to happen to make them independent of the technology used.

The code is not split further inside these packages, therefore representing everything as part of one domain.
In case there needs to be further separation, more packages can be introduced.
These should be created along *Bounded Contexts* (in *Domain-Driven Design* (DDD) terms), *not* by functionality.
For example, having an `organization` package does not make much sense, since organizations do not make sense without users, or roles.
Those form a cohesive domain that would be described as "user management" or similar, so all of those should go into a `user_management` package.
That should also be divided in the same "HA style" as described above.
Following this rule will lead to cohesive domains that can be split into services of their own and scaled independently, if the need arises (aka *microservices*).

### References

* [Hexagonal Architecture (Wikipedia)](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software))
* [Original article by Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
* [In-depth articles by Juan Manuel Garrido de Paz](https://jmgarridopaz.github.io/content/articles.html)
* [Hexagonal Architecture, there are always two sides to the story (Java)](https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c)
* [Ports & Adapters Explained](https://codesoapbox.dev/ports-adapters-aka-hexagonal-architecture-explained/)
* [Hexagonal Architecture in Python (Medium)](https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63)