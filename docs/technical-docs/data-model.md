---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }
Dao Minh Duong Nguyen 

# Data model
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

Here you can find our data model filled with exemplary data.

- \# equals primary key
- \<fk> equals foreign key
 
## User

| #UserId | Name | Password | 
| ----------- | ----------- | ----------- |
| 1 | minh | qwerty |

## Event 

| #EventId | Titel | Datum | 
| ----------- | ----------- | ----------- | 
| 01 | Sport | 01.01.2024 | 

## Comment

| #CommentId | \<fk>EventId | \<fk>UserId | Content | 
| ----------- | ----------- | ----------- | ----------- |
| 001 |01 | 1 | Volleyball? |

## ToDo

| #ToDoId | \<fk>EventId | Item |
| ----------- | ----------- | ----------- |
| 0001 | 01 | Volleyball |
