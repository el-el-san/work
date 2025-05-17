// Greets the provided name with a "Hello" message.
// Defaults to "world" when no name is given.
export function hello(name: string = 'world'): string {
  return `Hello, ${name}!`;
}

console.log(hello());
