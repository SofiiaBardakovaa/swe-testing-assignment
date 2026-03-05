# Testing Strategy

## Overview

The testing strategy for the **Quick-Calc** project focuses on verifying that the calculator's core calculation logic works correctly and that the application components interact properly. The project includes both **unit tests** and **integration tests** to ensure reliability and correctness.

Unit tests focus on testing the calculation logic in isolation, while integration tests verify that different parts of the system work together as expected.

The graphical user interface (Tkinter components) was **not directly tested**, because GUI testing often requires specialized tools and frameworks. Instead, testing focused on the core calculation functionality that powers the application.

---

# What Was Tested

The following components were tested:

* Arithmetic operations (addition, subtraction, multiplication, division)
* Expressions with parentheses
* Edge cases such as division by zero
* Negative numbers and decimal values
* Integration between the input expression and the calculation logic

These tests ensure that the most important functionality of the calculator works correctly.

---

# What Was Not Tested

The following aspects were intentionally **not tested**:

* Tkinter graphical interface elements (buttons, layout, styling)
* Visual behavior of the application window
* Performance testing

These areas were excluded because they are outside the scope of this assignment and require specialized GUI testing frameworks.

---

# Testing Concepts from Lecture

## The Testing Pyramid

The testing suite follows the **Testing Pyramid principle**, where the majority of tests are unit tests and only a small number are integration tests.

Structure of the test suite:

* **8 Unit Tests**
* **2 Integration Tests**

This structure reflects the pyramid approach where unit tests form the base (fast and numerous), while integration tests are fewer but verify system interactions.

---

## Black-box vs White-box Testing

Both testing approaches are reflected in this project.

**Unit tests** primarily use a **white-box testing approach**, because the internal logic of the `calculate()` function is known and tested directly.

**Integration tests** use a **black-box testing approach**, because they simulate user interactions by providing expressions as input and verifying the resulting output without focusing on internal implementation.

---

## Functional vs Non-Functional Testing

This project focuses on **functional testing**, which verifies that the calculator performs correct mathematical operations and produces expected outputs.

Examples of functional tests include:

* verifying that `2 + 3` returns `5`
* verifying that `(2 + 3) * 4` returns `20`
* handling division by zero correctly

**Non-functional aspects**, such as performance, usability, or graphical interface design, were not tested because they are outside the scope of the assignment.

---

## Regression Testing

The current test suite can also be used for **regression testing**. Whenever new features or changes are introduced to the calculator logic, the test suite can be executed using:

```
pytest
```

If any previously working functionality breaks, the failing tests will immediately indicate the issue, allowing developers to identify and fix regressions quickly.

---

# Test Results Summary

| Test Name                  | Test Type   | Status |
| -------------------------- | ----------- | ------ |
| test_addition              | Unit        | Pass   |
| test_subtraction           | Unit        | Pass   |
| test_multiplication        | Unit        | Pass   |
| test_division              | Unit        | Pass   |
| test_parentheses           | Unit        | Pass   |
| test_division_by_zero      | Unit        | Pass   |
| test_negative_numbers      | Unit        | Pass   |
| test_decimal_numbers       | Unit        | Pass   |
| test_user_addition_flow    | Integration | Pass   |
| test_user_parentheses_flow | Integration | Pass   |

All tests were executed using the **pytest** framework and passed successfully.
