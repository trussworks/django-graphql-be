# BE-002 Backend Framework is Python/Django

**Status:** Trial

**Drivers:** Sandy Wright

**Deciders:** Patrick Dickey, Lindsay Techel, Shimona Carvalho

**Decision Date:** 11/3/2021

## Context

Our context on the SITH project is weak, but we believe that we’ll need to implement a case management system, provide a means for data analysis on this system, and it will need to have top-notch security. This is not the strongest foundation for selecting a backend framework, but it gives us enough context to get started with one option to see how it goes.

The options being considered are:

- [Go](https://golang.org/), without a specific accompanying framework.
- [Django](https://www.djangoproject.com/), a Python web framework.
- [Node.js](https://nodejs.org/en/), a JavaScript runtime environment.

These are not directly comparable options. A language vs. a framework vs. a runtime environment? I did the comparison this way because:

- Go frankly does not have comprehensive web frameworks, and thus would require a significant amount of custom coding regardless of which one I picked. I decided that arbitrarily picking a framework for the decision now did not add anything meaningful to the comparison.
- Node’s web frameworks are all highly comparable, so it was difficult to pick one. I reviewed [Express.js](https://expressjs.com/) mostly, and most of the advantages were quality-of-life changes for the developer and the development environment. Performance was not significantly affected by any of them. Because of this and the fact that Node is already considered highly accessible, it actually seemed fairer to judge Node.js as-is.
- Python without Django is almost too broad to consider on its own for web development. Django is also exceptional and takes care of many of the disadvantages of using Python (the biggest one being performance). Honestly, the language alone would have lost this race.

You might notice that Ruby on Rails is missing from the consideration. Many of the pros and cons for Rails are comparable to Django, with the biggest tipping point being: No one on the team has significant experience with Ruby.

Given that we have Python experience and that the differences between Rails and Django are mostly negligible, I decided that Ruby on Rails would be trumped by Django based on experience alone. The data analysis component of the SITH project hurt its chances even further. So I cut it out of consideration.

## Decision

**Use Python/Django for our backend framework.**

Node.js was a compelling option for our case, but the project’s emphasis on security and data analysis pushed Django over the edge. Furthermore, we have team members who are experienced with Python and excited about the possibility of working with the language again. Enthusiasm is always a plus!

Go lost out for the opposite reason, being that our team _does_ have experience, but it was a negative experience. Lack of enthusiasm is always a huge negative.

Note that this decision does not dictate which API framework we may choose to go with, or our database architecture. Django is flexible and works with many different databases, and it also works with REST and GraphQL. Those options should be considered in separate ADRs.

## Consequences

Although the database and API framework should be decided in separate ADRs, the decision to go with Django does lean us heavily towards PostgreSQL and REST. We also know now that we will have a clear distinction from the frontend and the backend and can now set up different GitHub repositories for each.

For getting Django set up, we will also need to decide on linters, formatter, testing framework, and Python version managers. Putting together a comprehensive Python style guide and Django best practices guide would be helpful.

### Next.js

A question came up during standup about whether or not the choice of Django would make it more difficult or pointless to use Next.js. After researching our options, I don’t believe this would be the case. Our discussed architecture would have the frontend and backend being served separately, so server-side rendering would still be hugely relevant on the frontend server. We would simply have our data management sequestered on the Django/API server.

Pairing Django with Next.js would still be a beneficial and performant choice.

## Options Considered

### Go

- `+` **Statically typed.**
- `+` **Concurrency** is a strength of Golang (although we may not need to take advantage of this).
- `+` **Fast and scalable.** Go compiles into compact and efficient binaries, which means that well-written Go code will perform better than many other frameworks.
- `+` **Explicit and loosely coupled.** Because Go is so strictly typed and verbose, it’s easier to avoid complex dependencies and tight coupling within the codebase.
- `+` **Experience with Go** on team.
- `-` **Extremely verbose.** There aren’t many syntactic shortcuts in Go, which means that lots of functionality that you would expect to be built-in (such as checking for an element in a list) has to be completely written out.
- `-` **Lack of generics.** Because the language is strictly typed AND verbose, functionality needs to be copied over for different types.
- `-` **Ballooning codebases.** Because of both of the two negatives, Go codebases contain a LOT of code. Organization needs to be intentional and rigid from the beginning if we want to prevent it from becoming unwieldy and confusing.
- `-` **Time consuming.** Writing and rewriting explicit code, and staying vigilant with package organization, means that working in a significant Go codebase takes a lot of time and effort.
- `-` **Lack of web development support.** Go is still a relatively young language, so it doesn’t have many supportive frameworks for web development, nor does it have a robust/stable ORM yet.

### Python (w/ Django)

- `+` **Extremely well-known, supported, and loved** language. Python brings with it a wealth of community knowledge and support.
- `+` **Readable, easy-to-learn syntax.**
- `+` **Great for scripting and CLI tools.** Python can be used for lots of developer tooling beyond web developing, which could simplify our overall tech stack.
- `+` **Great for data science and machine learning.** SITH will very likely have a data analysis component, and Python is one of the best languages to use in this context.
- `+` **Multi-paradigm.** Object-oriented and functional code designs are well-supported in this language.
- `+` **Portable and dynamic.** Because it is interpreted, Python can be easily run on other systems. This also means it can be easily containerized.
- `+` **Django is secure.** As a framework, it has a well-developed security architecture and the fact that it is more high-level than Node and Go means less work is needed to manage security.
- `+` **Django is performant.** While well-designed Go code is much, much faster, it’s more difficult to create such a well-designed Go codebase. Node as a runtime environment is more performant than Python generally, but the design of Django closes that gap and actually surpasses the most popular Node frameworks (such as Express.js) in terms of performance.
- `+` **Experience with Python/Django** on team.
- `-` **No strict typing.** [MyPy](http://mypy-lang.org/) is an option to add static type-checking to the language, but it is still an immature tool (especially compared to languages like TypeScript).
- `-` **TOO creative.** The flexibility of the language can be a drawback when we need to tighten scope. It can also make it challenging to switch frameworks/languages later on.
- `-` **Runtime errors.** Because Python is interpreted, a lot of compile-time errors that would get caught early on with Go or TypeScript don’t show up until after deployment.
- `-` **Single-threaded.** Optimized CPU usage and multiple threads aren’t natively supported with Python/Django.

### Node.js (in TypeScript)

- `+` Both the **frontend and backend could use the same programming language.** This would make it easier for new engineers to onboard to the project.
- `+` **Promotes code reuse** and smaller, lightweight codebases.
- `+` **TypeScript** helps ensure type-safety.
- `+` Known for being **easy to deploy.**
- `+` **Asynchronous I/O requests** (although they are still single-threaded).
- `+` **Huge community** and selection of libraries and frameworks to work with.
- `-` **No support for concurrency.** Node.js is a runtime environment, not a framework, and the entire environment is single-threaded. Any processing that might be CPU-heavy would have huge performance implications in Node.
- `-` **Callbacks can quickly become confusing.** Because of the async request architecture, a lot of functionality is nested in callbacks, which are nested in callbacks, which are nested in…
- `-` **API is unstable.** Because of the quickly developing JavaScript environment, the burden of maintaining and updating a Node app is higher.
- `-` **Conscious effort required to code a loosely-couple server architecture.**
- `-` **Not a lot of experience** with Node on the team.

## Resources

- [Go](https://golang.org/)

  - [The pros and cons of programming in Go](https://www.willowtreeapps.com/craft/the-pros-and-cons-of-programming-in-go)

- [Python](https://www.python.org/)

  - [The web framework for perfectionists with deadlines | Django](https://www.djangoproject.com/)
  - [mypy - Optional Static Typing for Python](http://mypy-lang.org/)
  - [The Good and the Bad of Python Programming Language](https://www.altexsoft.com/blog/python-pros-and-cons/)
  - [Security in Django | Django documentation | Django](https://docs.djangoproject.com/en/3.2/topics/security/)
  - [What is Django? Advantages and Disadvantages of using Django](https://hackr.io/blog/what-is-django-advantages-and-disadvantages-of-using-django)

- [Node](https://nodejs.org/en/)

  - [6 Best Node.js Frameworks for Web Developers in 2022-2021](https://technostacks.com/blog/nodejs-frameworks/)
  - [The Good and the Bad of Node.js Web App Development](https://www.altexsoft.com/blog/engineering/the-good-and-the-bad-of-node-js-web-app-development/)
  - [Why Node.js is Great for Backend Development? | Engineering Education (EngEd) Program | Section](https://www.section.io/engineering-education/why-nodejs-is-great-for-backend-development/)
  - [Express - Node.js web application framework](https://expressjs.com/)
