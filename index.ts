// Greets the provided name with a "Hello" message.
// Defaults to "world" when no name is given.
/**
 * Returns a friendly greeting for the provided name.
 *
 * @param name - Name to greet. Defaults to 'world'.
 */
export function hello(name: string = 'world'): string {
  return `Hello, ${name}!`;
}

/**
 * Returns a farewell message for the provided name.
 *
 * @param name - Name to bid farewell. Defaults to 'world'.
 */
export function goodbye(name: string = 'world'): string {
  return `Goodbye, ${name}!`;
}

// If this file is executed directly, greet the first command line argument or
// use the default greeting.
if (require.main === module) {
  const [, , cmd, name] = process.argv;
  if (cmd === '--goodbye') {
    console.log(goodbye(name));
  } else {
    // treat the first argument as name when no option is provided
    console.log(hello(cmd));
  }
}
