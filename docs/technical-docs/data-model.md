---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }
Dao Minh Duong Nguyen 

# [Data model]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## User

| #UserId | Name | Password | 
| ----------- | ----------- | ----------- |
|  |  |  |

## Event 

| #EventId | Titel | Beschreibung | Datum | 
| ----------- | ----------- | ----------- | ----------- |
|  |  |  |  | 

## Comment

| #CommentId | <fk>EventId | <fk>UserId | Content | 
| ----------- | ----------- |
|  |  |  |  |

## ToDo

| #ToDoId | <fk>EventId | Item |
| ----------- | ----------- |
|  |  |  |
