---
title: App Behavior
parent: Technical Docs
nav_order: 2
---

{: .label }
[Tien Minh Nguyen]

# App behavior
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

# GIO Flowchart

<img width="900" alt="GIO Flowchart" src="https://github.com/mdxng/gio/blob/main/docs/assets/images/GIOFlowchart.jpg?raw=true">

# Bahvior

The user logs into their account if the user has an existing account. If not the user has to register themself to create an account. Both the Login and Register create a query to the User database. After been looged in the user's session beginns and can choose diffrent activities:

- Create an Event:
To create an event the user has to enter Title of the event, date of the event, items for the checklist (optional), comment (optional) and submit the entry by pressing the create button. A query in the database for event will be created.

- Calender View:
The Calender displays the created events.

- Friendslist:
The user can view their already added friends and adding friends can simply done by entering the UserID from the friend in the texfield and then submit it with the "add" button.  A query in the database for friendslist will be created.

- Settings:
In Settings the user can see their UserID and Username and can change their password via the "change password" button. A pop up window will open to enter the new password. After submitting the password a change in the User database will entry.

- Logout:
Pressing logout will end the current session and redirect to the Login page.

