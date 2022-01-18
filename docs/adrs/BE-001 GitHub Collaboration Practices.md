# BE-001 GitHub Collaboration Practices

**Status:** Accepted

**Drivers:** Sandy Wright

**Deciders:** Patrick Dickey, Lindsay Techel, Shimona Carvalho

**Decision Date:** 11/1/2021

## Context

As an engineering team, norming on `git` practices is important to make sure we can work together effectively. There are a number of ways we can leverage GitHub to make this process less painful. In particular, this ADR will look at workflows, naming conventions, and pull request (PR) best practices.

## Decision

### **Workflow: [Git Feature Branch](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)**

#### Each feature should be developed in its own, dedicated branch.

- `+` Encapsulates feature work into one space so that the main codebase is unaffected.
- `+` Makes PRs an especially effective way to review code.

#### Each dedicated feature branch should be branched off of the main branch (as opposed to another feature or development branch).

- `+` Ensures each feature branch is as up-to-date as possible when it is started.
- `+` Eliminates dependencies on incomplete features.
- `-` Means we might have to wait a little longer to start on work that is blocked by an incomplete or in-progress feature.

#### Each dedicated feature branch will be merged into the main branch once the feature is complete and reviewed.

- `+` Features aren’t left hanging before being incorporated into the codebase.
- `+` Encourages reducing dependencies between features and encapsulating development.
- `-` Means some work might need to be expanded to ensure it is complete and functional.

#### Only one engineer will work on a feature branch at a time (with exceptions for pairing).

- `+` Reduces the risk of merge conflicts.
- `+` Reduces the risk of duplicated work or errors due to miscommunication.
- `-` Might slow down some collaborative efforts.

### Branches: General

#### `main` will be the default branch for our repos (instead of `master`).

- `+` Follows the most up-to-date standard.
- `+` GitHub’s default is now main.
- `+` New project means we don’t have to worry about the risk to existing integrations.
- `-` Different from previous project.

#### The default branch will be protected so that pull requests are required.

- `+` Reduces the chance of serious bugs getting merged and affecting production.
- `+` Ensures all of our code gets reviewed.
- `-` Adds overhead.

#### Stale branches should be deleted.

- `+` Helps us keep track of active development work.
- `+` Reduces branch bloat in the repo.

#### HEAD branches should be automatically deleted after a PR merge.

- `+` Devs won’t have to worry about going back and removing their stale feature branches.

### Branches: Naming convention

Format:
`<dev initials>-<Jira ticket ID>-<description>`
Example:
`sw-SP-40-add-reset-button`

#### Branch names should be kebab-case (lowercase and delimited by dashes).

- `+` Consistency.

#### Branch names should start with the Jira ticket ID, if it is associated with a Jira ticket.

- `+` Jira + GitHub integrations will recognize the ID and automatically link that branch to the ticket.
- `-` Makes the name longer.

#### Branch names should include a brief description of what feature the branch is implementing.

- `+` Allows devs to understand what a branch is for at a glance, instead of forcing them to look up a ticket in Jira.

#### Optional: The dev who started the branch may prefix its name with their initials or username if that makes it easier to keep track of their work.

- `+` Devs can quickly identify their branches in a list.
- `-` Makes the name longer.

### Commits: General

#### All commits must be associated with a recognized email/GitHub account (no unrecognized commits).

- `+` Allows us to keep track of who is doing what in the repo.

#### No dependencies should be committed.

- `+` Keeps our codebase lean.
- `+` Makes it clear which code we have written.

#### No built or generated code should be committed.

- `+` Keeps our codebase lean.
- `+` We don’t have to worry about unexpected changes or inconsistencies when adding generated code.
- `-` All local builds must rebuild/generate this code.

#### We will not squash commits.

- `+` All original commits are preserved, so we have a more complete history.
- `+` If issues arise after a merge, it is possible to track down the exact commit that caused the problem.
- `-` Lots of commits to wade through.

#### Rebase whenever possible (although merging and merge commits are fine).

- `+` Keeps the code up-to-date without a bunch of (relatively) meaningless merge commits.

### Commits: Style guide

Example:
[Once applied, this commit will…] `SP-40 Add a button that resets all input in the form`

#### Commits should be in the imperative mood. IE, it should fill in the sentence “Once applied, this commit will … <msg>”

- `+` Consistency.
- `+` This tense is the most brief (no extra “-s” or “-ed” morphemes, for example) and thus saves characters in the commit message.
- `-` Not necessarily the most natural tense to write in.

#### Optional: Commit messages should be capitalized.

- `+` Consistency, but it is only a suggestion.

#### Optional: Commit messages may include Jira ticket IDs where relevant.

- `+` Jira + GitHub integrations will recognize the IDs and automatically link the commit to the tickets.
- `-` Takes up space in the commit (limit of 50 characters for subject line).

### Pull requests

#### PRs should be opened as early as possible. Reviews and comments can and should be solicited before the work is technically “done.”

- `+` PRs help with visibility into the work as it progresses.
- `+` Helps save time so that there’s less of a review crunch at the end of the sprint.
- `-` More overhead for the developer.

#### PRs will have a template that includes an interactive checklist for the developer, the reviewer, and the designer.

- `+` Reminds the developer to take care of certain items.
- `+` Promotes more engagement from the reviewer and designer.
- `+` Makes our PRs look more organized and consistent.
- `-` Adds some maintenance burden keeping the checklists up-to-date and relevant.

#### All PRs should include a vote of confidence as the first comment.

- `+` Ensures that all developers give a PR a cursory glance.
- `+` Lets the dev and the team know how comfortable folks feel with the content of a PR.
- `+` Highlights code that might need more oversight or careful review.

#### If the vote of confidence shows that no one is confident in solo reviewing this PR, a PR walkthrough should be scheduled.

- `+` Keeps the full eng team engaged with new or unfamiliar code.
- `+` Keeps the team on the same page.
- `-` Scheduling meetings can be difficult.

#### PR walkthroughs should be led by the dev and should have time budgeted to go over the code, show a live demo, and answer questions.

- `+` Allows for thorough reviews and shows the reviewers everything they need to see.
- `-` Some walkthroughs might need 45 minutes to 1 hour to include all of this.

#### PR walkthroughs should be recorded.

- `+` New team members or members who cannot make a walkthrough can go through it async.
- `+` Keeps a record of progress on the system and its features.

### Reviewing PRs

#### 1 approval from an engineer is required before a PR can be merged. This approval should be from someone who voted as confident for reviewing the PR.

- `+` Reduces the overhead of reviewing with a small team.
- `+` Ensures that the approval comes from someone who feels comfortable reviewing the code.
- `-` Linking the review to “confidence” could overly limit who can review PRs.

#### If a PR walkthrough was held, the PR can be approved by anyone who attended the walk, regardless of confidence.

- `+` If the rule of having someone with a “confident” vote limits who can review PRs, this is a good way to open the pool up again.
- `+` Promotes walkthroughs and sharing knowledge.

#### PRs that modify the UI or look-and-feel of the app should be reviewed by design. Changes to HTML or CSS will trigger a design review.

- `+` Keeps design in the loop for the actual look-and-feel of the app.
- `-` Some code owner triggers can ping design too often and overburden them with reviews.

#### PRs that trigger design review but were just refactors should specify that look-and-feel should be the same so that design knows to check that nothing changed visually.

- `+` Being clear about the UI changes makes it easier for design to review PRs.

## Resources

- [Git Feature Branch Workflow Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
- [GitHub - A set of best practices for JavaScript projects](https://github.com/elsewhencode/project-guidelines)
