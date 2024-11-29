# Socket Chat Application - Test Suite

## Testing Overview

This project focuses on comprehensive testing for a socket-based chat application, demonstrating different testing approaches:

### Test Files

1. **Unit Testing** (`prueba_unitaria.py`):
   - Tests broadcast functionality
   - Verifies message sending to multiple clients
   - Handles edge cases like empty messages
   - Uses `unittest.mock` for simulating client interactions

2. **Username Validation Testing** (`prueba_tdd.py`):
   - Implements Test-Driven Development (TDD) approach
   - Validates username length constraints
   - Ensures usernames meet specific criteria

3. **Integration Testing** (`prueba_integracion.py`):
   - Tests end-to-end client-server interactions
   - Validates message broadcasting across multiple clients
   - Checks server's ability to handle client disconnections

## Running Tests

```bash
python -m unittest discover
```

### Test Cases Covered

#### Broadcast Functionality
- Sending messages to multiple clients
- Handling errors during message transmission
- Preventing empty message broadcasts

#### Username Validation
- Minimum length validation
- Maximum length validation
- Character type restrictions

#### Client-Server Interaction
- Successful client connection
- Message transmission between clients
- Graceful handling of client disconnections

## Testing Techniques

- Unit Testing
- Mock Objects
- Integration Testing
- Error Handling Validation

## Technologies Used

- Python `unittest` framework
- Socket programming
- Threading
- Mock objects

## Contributing

Contributions to expand test coverage are welcome. Please submit pull requests with additional test cases or improvements to existing tests.

