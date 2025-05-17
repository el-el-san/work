// Greets the provided name with a "Hello" message.
// Defaults to "world" when no name is given.
export function hello(
  name: string = 'world',
  options?: { upperCase?: boolean }
): string {
  let greeting = `Hello, ${name}!`;
  if (options?.upperCase) {
    greeting = greeting.toUpperCase();
  }
  return greeting;
}

export function main(args: string[]): void {
  const [name, flag] = args;
  const upperCase = flag === '--upper';
  console.log(hello(name, { upperCase }));
}

// If this file is executed directly, greet the first command line argument or
// use the default greeting.
if (require.main === module) {
  main(process.argv.slice(2));
}
