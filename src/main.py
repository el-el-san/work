"""
This script prints "Hello, World!" to the console.

It includes basic error handling to catch potential issues during the print operation.
"""

import sys

def main():
    """
    Main function to print the greeting message.

    Includes basic error handling for the print operation.
    If an error occurs during printing, an error message is printed to
    standard error, and the script exits with a non-zero status code.
    """
    try:
        # Print the greeting message to standard output.
        print("Hello, World!")
    except Exception as e:
        # Basic error handling: Catch any exception during print.
        # Print an informative error message to standard error.
        print(f"Error: Could not print greeting: {e}", file=sys.stderr)
        # Exit with a non-zero status code to indicate failure.
        sys.exit(1)

# Ensure the main function is called only when the script is executed directly.
if __name__ == "__main__":
    main()