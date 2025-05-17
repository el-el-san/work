// Greets the provided name with a "Hello" message.
// Defaults to "world" when no name is given.
export function hello(name: string = 'world'): string {
  return `Hello, ${name}!`;
}

// If this file is executed directly, greet the first command line argument or
// use the default greeting.
if (require.main === module) {
  const [, , name] = process.argv;
  console.log(hello(name));
}
