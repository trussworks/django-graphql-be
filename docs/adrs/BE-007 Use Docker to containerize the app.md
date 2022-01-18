# BE-007 Use Docker to containerize the app

**Status:** Accepted

**Drivers:** Sandy Wright

**Deciders:** Lindsay Techel, Shimona Carvalho, Patrick Dickey

**Decision Date:** 11/18/2021

## Context

Containers package up code, including all its dependencies, in such a way that it can run consistently in many different server environments. They have become an industry standard for porting systems to production servers. Docker currently dominates the container scene, although some alternatives are starting to gain popularity.

Virtual machines (VMs) are another way to package and port code to production, but they are bulkier and less portable. Because of SITH’s lack of definition, we’ve been designing the system with flexibility in mind. Using a VM would be less compatible with this strategy, but they do offer increased isolation and security.

## Decision

### Use Docker to containerize the SITH system (frontend, backend, and database)

As far as containers go, Docker is still ubiquitous in the industry. Frankly, there just aren’t any compelling alternatives or incentives to try any container besides Docker. All the other tools we might consider would be compatible with Docker, and even the tools trying to replace Docker are, in fact, compatible with it.

Not containerizing the app is also not a viable option. It makes the system more vulnerable, buggy, and less convenient in the long run. It will actually save us time and effort to set up Docker, as counterintuitive as that might seem.

## Consequences

The frontend, backend, and database will need to be dockerized. This is not insignificant engineering work, and they might not all be completable within one sprint.

Once the app is fully dockerized, changes to the configuration should be minimal and motivated by infra concerns (although exceptions are always possible).

## Options Considered

### Docker

- `+` Industry standard with a wealth of community support and resources
- `+` Can be used for every aspect of the app - frontend, backend, and database - giving us consistent system architecture across the stack
- `+` Isolation in Docker makes the application more secure
- `+` Lightweight and OS-independent
- `+` Just about every infra tool we may use for the CI/CD pipeline will be compatible with Docker
- `+` Robust documentation
- `+` Existing infra tooling defaults to using Docker
- `-` Increasing number of paywalls is concerning

### Use an alternative to Docker

- `+` As Docker introduces more paywalls, more alternative options are going to take hold
- `+` Alternatives such as CoreOS rkt and Mesos are also compatible with Docker
- `-` Not much support or adoption yet - [in 2018, over 80% of production containers were still Docker](https://containerjournal.com/topics/container-ecosystems/5-container-alternatives-to-docker/)
- `-` Most team experience is with Docker, on SITH and at Truss as a whole
- `-` No clear benefits over Docker, and these tools often _also_ use Docker

### Use a Virtual Machine (VM) instead of a container

- `+` Grants full control of the app’s ecosystem, down to the operating system
- `-` Slow to boot and bulky
- `-` Since they contain a full copy of an operating system, they can be huge (>10GB)
- `-` More complex than containers

### No containerization

- `+` Don’t have to do the work to set up containers
- `-` Must do extra work to set the system up for deployment
- `-` No consistency, development environments are different on all engineers' machines
- `-` Vulnerable to operating system errors, difficult to debug

## Resources

- [What is a Container? | Docker](https://www.docker.com/resources/what-container)
- [What is Containerization? Containerization Definition - Citrix](https://www.citrix.com/solutions/app-delivery-and-security/what-is-containerization.html)
- [5 Container Alternatives to Docker](https://containerjournal.com/topics/container-ecosystems/5-container-alternatives-to-docker/)
- [Docker in Production: Getting it Right | Aqua](https://www.aquasec.com/cloud-native-academy/docker-container/docker-in-production-getting-it-right/)
