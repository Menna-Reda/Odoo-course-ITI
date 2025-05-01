# Odoo-course-ITI

## Overview
This project is a **Hospital Management System (HMS)** module for Odoo. It is designed to manage hospital operations, including patients, doctors, departments, and medical records.

## Features
- **Patient Management**: Manage patient details, medical history, and conditions.
- **Doctor Management**: Assign doctors to departments and manage their details.
- **Department Management**: Track department capacity and patient assignments.
- **Medical Reports**: Generate detailed patient reports in PDF format.
- **Access Control**: Role-based access for managers and users with specific permissions.

## Module Structure
- **Models**: Contains Python files defining the data models (`hms_patients`, `hms_doctors`, `hms_departments`, etc.).
- **Views**: XML files defining the user interface for patients, doctors, and departments.
- **Reports**: Templates for generating patient reports.
- **Security**: Access control rules and group definitions.

## Installation
1. Place the `hms` module in the `custom_addons` directory of your Odoo instance.
2. Update the app list in Odoo.
3. Install the module from the Odoo Apps menu.

## Usage
- Navigate to the **HMS** menu in Odoo.
- Manage patients, doctors, and departments through the provided views.
- Generate patient reports from the Reports section.

## Author
Developed by **Menna** as part of the Odoo course at ITI.