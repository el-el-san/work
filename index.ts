/**
 * Greets the provided name with a "Hello" message.
 * Defaults to "world" when no name is given.
 */
export function hello(name: string = 'world'): string {
  return `Hello, ${name}!`;
}

/**
 * Runs the CLI using the provided arguments.
 * The first argument is treated as the name to greet.
 */
export function main(args: string[] = process.argv.slice(2)): void {
  const [name] = args;
  console.log(hello(name));
}

// If this file is executed directly, run the CLI.
if (require.main === module) {
  main();
}
