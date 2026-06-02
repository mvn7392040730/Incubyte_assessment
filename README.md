# Incubyte Automation Assessment

## Overview

This project automates the Parabank user registration and login flow using **Playwright with Python**.

The framework follows:

* Page Object Model (POM)
* Behavior Driven Development (BDD)
* Pytest
* Logging
* HTML Reporting

## Test Scenario

* Register a new user account
* Login using the registered credentials
* Verify successful login
* Retrieve and log the account balance
* Capture screenshots during execution

## Project Structure

```text
features/      -> BDD feature files
pages/         -> Page Object Model classes
steps/         -> Step definitions
utils/         -> Logger and utility classes
reports/       -> HTML reports
screenshots/   -> Execution screenshots
videos/        -> Execution recordings
logs/          -> Execution logs
```

## Installation

```bash
pip install -r requirements.txt
playwright install
```

## Execution

Run the test suite:

```bash
python -m pytest -s -v
```

Generate HTML report:

```bash
python -m pytest -s -v --html=reports/report.html --self-contained-html
```

## Artifacts

* HTML Report: `reports/report.html`
* Logs: `logs/`
* Screenshots: `screenshots/`

## Framework Design

* BDD implemented using Gherkin feature files
* POM implemented for maintainability and reusability
* Logging added for execution tracking
* Screenshots captured during test execution
* HTML reports generated using pytest-html

```
```
