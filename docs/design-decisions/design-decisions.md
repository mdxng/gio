---
title: Design Decisions
nav_order: 3
---

{: .label }
Tien Minh Nguyen

# Design decisions
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Creating own CSS or using Boostraps?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

Creating for every single page the same style of CSS would be to time consuming.

### Decision

We chose to use Bootstraps because by using their CSS templates we are able to have the same style and modern look throughout the website, while it is less time consuming and effectively.
But of course there will be parts to use our own CSS.
The Idea of using Bootstraps was Dao Minh Duong Nguyen's.

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## 02: Using SQL Lite or SQLAlchemy for the Database?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

We have not decided to use which of the two database platforms.

### Decision

SQLAlchemy was decided. By using SQLAlchemy we are able to work with Python objects.
The Idea was Tien Minh Nguyen's.

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## 03: Creating WO (WORKING)Branch

### Meta

Status
: Work in progress - Decided - **Obsolete**

Updated
: DD-MMM-YYYY

### Problem statement

Working directly in the main branch would be dangerous and not effectively when two people are working on the same project in the same branch.

### Meta

Yes Tien Minh created a WO (working) branch, so he could have his own branch to work on. Firstly it worked well, but at some point it got so chaotic that the app was not running anymore. Debugging would take to long. Tien Minh created a new branch for the Login function later. WO branch is not usable anymore.
Using Branches was Dao Minh Duong Nguyen's and Tien Minh Nguyen's idea.

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## 04: WTForms ?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

We have not decided to use which of the two database platforms.

### Decision

SQLAlchemy was decided. By using SQLAlchemy we are able to work with Python objects.
The Idea was Tien Minh Nguyen's.

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## 05: Using Pop up warning?

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

Having warnings like when a User enters the password wrong are shown currently in a new page with just warning. Overall it does not look professional.

### Decision

Instead of opening a new page a warning pop up should be shown, which can be closed by clicking the close button. This would make the warning look better.
The Idea was Tien Minh Nguyen's.

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## 05: Terminal updates output

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

While creating the Login and Register function i was not sure if a User was logged in or not or registered yet.

### Decision

Creating a Terminal output every time a User is logged in and registered gave me the confirmation of my work. I added the current page and user to the terminal output. It was something nice to have.
The Idea was Tien Minh Nguyen's.

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---