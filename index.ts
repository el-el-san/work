// Greets the provided name with a "Hello" message.
// Defaults to "world" when no name is given.
/**
 * Capitalizes the first letter of the provided word. If the word is empty,
 * the empty string is returned.
 */
export function capitalize(word: string): string {
  if (!word) {
    return '';
  }
  return word.charAt(0).toUpperCase() + word.slice(1);
}

/**
 * Greets the provided name with a "Hello" message. If no name is provided, the
 * greeting defaults to "world".
 */
export function hello(name: string = 'world'): string {
  return `Hello, ${capitalize(name)}!`;
}

/**
 * Executes the CLI. The first argument after the script name is treated as the
 * name to greet. When no argument is supplied the default greeting is used.
 */
export function main(argv: string[] = process.argv): void {
  const [, , name] = argv;
  console.log(hello(name));
}

// If this file is executed directly, greet the first command line argument or
// use the default greeting.
if (require.main === module) {
  main();
}
