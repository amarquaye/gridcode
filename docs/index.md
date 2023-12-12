# Asset Management System

## Introduction

The Asset Management System (AMS) is a Python-based **console** application designed to *manage* and *track* various **assets** within an organization. This system provides functionalities such as **creating**, **reading**, **updating**, and **deleting** assets, as well as **searching** for assets based on *specific criteria*. Additionally, users can log in to the system, and account information is securely stored.

## Table Of Contents

- [Overview](#overview)
- [Installation](#installation)
- [User Management](#user-management)
  - [Create User](#create-user)
  - [Log In](#log-in)
- [Asset Management](#asset-management)
  - [Create Asset](#create-asset)
  - [Read Asset](#read-asset)
  - [Update Asset](#update-asset)
  - [Delete Asset](#delete-asset)
  - [Search Asset](#search-asset)
- [Logging](#logging)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Overview

The Asset Management System is designed to provide a user-friendly interface for **managing assets**, making it easier for organizations to **keep track** of their inventory. The system allows users to perform various operations related to both user management and asset management.

## Installation

To install and use the *Asset Management System*, click [here](https://github.com/amarquaye/gridcode/releases/download/v2.0.0/ams.exe).  

This will take you to our release page where you'll find and download the executable.

## User Management

### Create User

The system allows administrators to create new user accounts securely. *Usernames* and *passwords* are stored in a CSV file with **hashed** passwords for security.

### Log In

Users can log in to the system using their credentials. The system validates the entered information against the stored data to grant or deny access.

## Asset Management

### Create Asset

Users can add new assets to the system by providing relevant information such as *serial number*, *category*, *type*, *location*, *assignee*, *description*, *color*, and *status*.

### Read Assets

The system provides multiple options for viewing assets, including a **spreadsheet** view, **PDF** view, and a default **terminal** view

### Update Asset

Users can **update** existing asset information by specifying the **serial number** and the **field to be updated**. The system logs changes for audit purposes.

### Delete Asset

Assets can be removed from the system by providing the **serial number**. The system *logs* the deletion for *tracking* purposes.

### Search Assets

Users can **search** for assets based on various criteria, such as *ID*, *serial number*, *category*, *type*, *location*, *assignee*, *description*, *color*, or *status*.

## Logging

The system logs **user activities**, including **login attempts**, **asset creations**, **updates**, **deletions**, and **searches**. The logs are stored in separate log files for both user activities and asset activities.

## Dependencies

The Asset Management System relies on the following Python libraries:

[colorama](https://pypi.org/project/colorama/): Used for terminal text colorization.  

[tabulate](https://pypi.org/project/tabulate/): Facilitates tabular data formatting for a better display.  

[csv2pdf](https://pypi.org/project/csv2pdf/): Enables the conversion of CSV data to PDF format.  

[pywriter](https://pypi.org/project/pywriter/): A utility library for printing characters in the classic typewriter effect.  

## Conclusion

The Asset Management System provides a flexible and efficient solution for organizations to manage their assets effectively. Regular updates and improvements may be made to enhance the functionality and security of the system. Users are encouraged to refer to the [documentation](https://amarquaye.github.io/gridcode/) for any queries or assistance.
