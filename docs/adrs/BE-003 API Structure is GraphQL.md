# BE-003 API Structure is GraphQL

**Status:** Accepted

**Drivers:** Sandy Wright

**Deciders:** Patrick Dickey, Lindsay Techel, Shimona Carvalho

**Decision Date:** 11/18/2021

## Context

For the SITH project, we’ve decided to separate the backend and frontend so that each stack is independent and flexible, which will allow us to easily iterate and scale as we learn more about the project. This means we must have an **internal API** to communicate between the two servers.

We have decided on [**React** as our frontend framework](https://github.com/trussworks/next-graphql-fe/blob/main/docs/adrs/FE-002%20Frontend%20Framework%20is%20ReactJS.md#fe-002-frontend-framework-is-reactjs) and [**Django** as our backend framework](./BE-002%20Backend%20Framework%20is%20Python%20and%20Django.md). Whichever API structure we select, it will be hosted on the backend and must be compatible with the frontend. It must be secure, scalable, and flexible so that we can adapt as more project requirements become known.

The options being considered are:

- **REST** - A stateless architectural style that represents _resources_ (data types, objects) and exposes _paths_ (URLs) to those resources. HTTP methods are used to indicate which CRUD operations the client is requesting.
- **GraphQL** - A query language and runtime environment for fulfilling queries. Uses the HTTP POST method to complete requests.
- **gRPC** - A Remote Procedure Call (RPC) framework that defines services and methods for the API consumer to invoke. API calls are generally seamless function calls, generally indistinguishable from local function calls.
- **SOAP** - A messaging protocol that uses XML as its formatting and relies on application layer protocols, such as HTTP, to communicate.

## Decision

### Use GraphQL as the API structure.

GraphQL presents an exciting, powerful new API paradigm by behaving like a query language. For a vague prototype that needs to be flexible as we learn about our project, GraphQL is a powerful option. It loosely couples the frontend, backend, and data layer, making it easier to change one of these layers without affecting the others. And on the backend, Graphene-Django makes use of Django models to build the API in an intuitive, streamlined manner.

The team would get the opportunity to gain experience with a new technology as well. We are all familiar with REST and would be comfortable switching to that structure if necessary. However, its rigidity could limit us as time goes on.

As for SOAP and gRPC: They are both so specific and niche and we simply do not have the use-cases to take advantage of them.

## Consequences

We will have to use [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/) as a backend tool to create our API. We will also have to do some work to set up the frontend to consume the API, and we will need to familiarize ourselves with Apollo server.

## Options Considered

### REST

- `+` Instantly recognizable standard.
- `+` Consuming REST APIs is straight-forward and fairly consistent across technologies.
- `+` Uses basic CRUD patterns.
- `+` Lots of experience with REST on the team.
- `+` Django REST Framework is a well-known, well-supported framework in the Django/Python community. ([GitHub repo](https://github.com/encode/django-rest-framework) - 22k stars)
- `*` Resource/entity-based.
- `-` REST patterns can be fairly rigid, and making them flexible takes considerable development effort.
- `-` The API consumer doesn’t have any control of what information they receive.
- `-` Only handles certain data models well (such as a tree model).
- `-` Arguably, every path exposed by a REST API adds a _marginal_ security risk.

### GraphQL

- `+` Growing in popularity and use.
- `+` Because it’s a query language, the consumer has full control of what data they receive.
- `+` _Extremely_ flexible and scalable. APIs are easy to modify as the service evolves.
- `+` Handles a variety of data models well.
- `+` Not as limited as REST in terms of what mutations/actions are appropriate (since REST is closely linked to CRUD actions).
- `+` The API usable with Apollo server, even without a frontend consuming it.
- `*` A query language! Not clearly resource- or procedure-based.
- `-` Less experience with it on the team.
- `-` Requires specific tools to use. We would be limited to [Graphene](https://docs.graphene-python.org/projects/django/en/latest/) on the backend (GitHub repo - 6.9k stars).
- `-` Needs to be designed with the right mindset - do not couple the design with the data layer.

### gRPC

- `+` Efficient and scalable.
- `+` Designed for a seamless coding experience.
- `*` Procedural, function-based, but increased emphasis on entities compared to SOAP.
- `-` Too opinionated for our use-case - focus is on efficiency instead of flexibility. gRPC is best if you have a specific problem you want to solve.
- `-` Complicated, involves more knowledge of networking than other API structures.

### SOAP

- `+` Highly standardized.
- `+` Increased security with extensions.
- `*` Procedural, function-based. Not resource-based (like REST).
- `-` Not customizable or flexible. Extremely rigid and requires specific tools to use.
- `-` MUST be used with XML, cannot understand JSON.
- `-` High-bandwidth and low scalability.
- `-` Less popular than REST, therefore less support.

## Resources

- General
  - [What are the types of APIs and their differences?](https://searchapparchitecture.techtarget.com/tip/What-are-the-types-of-APIs-and-their-differences)
  - [An Architect's guide to APIs: SOAP, REST, GraphQL, and gRPC](https://www.redhat.com/architect/apis-soap-rest-graphql-grpc)
- REST
  - [What is REST? | Codecademy](https://www.codecademy.com/articles/what-is-rest)
  - [Home - Django REST framework](https://www.django-rest-framework.org/)
- GraphQL
  - [Graphene-Python](https://docs.graphene-python.org/projects/django/en/latest/)
  - [Using GraphQL in your Python Django application - Programming with Mosh](https://programmingwithmosh.com/backend/graphql/using-graphql-in-your-python-django-application/)
  - [Do you need GraphQL with Django? - LogRocket Blog](https://blog.logrocket.com/do-you-need-graphql-with-django/)
  - [Integrating GraphQL API into a Django application | Engineering Education (EngEd) Program | Section](https://www.section.io/engineering-education/integrating-graphql-api-in-a-django-application/)
  - [Introduction to Apollo Server](https://www.apollographql.com/docs/apollo-server/)
- SOAP
  - [SOAP API | SOAP API Example Protocol | SOAP APIs Interface](https://stoplight.io/api-types/soap-api/)
- gRPC
  - [Introduction to gRPC](https://grpc.io/docs/what-is-grpc/introduction/)
  - [FAQ](https://grpc.io/docs/what-is-grpc/faq/)
  - [gRPC vs REST: Understanding gRPC, OpenAPI and REST and when to use them in API design | Google Cloud Blog](https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them)
