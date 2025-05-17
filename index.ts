// Greets the provided name with a "Hello" message.
// Defaults to "world" when no name is given.
declare const process: { argv: string[] };
export function hello(name: string = 'world'): string {
  return `Hello, ${name}!`;
}

export function parseName(args: string[]): string | undefined {
  return args[2];
}

function main(): void {
  const name = parseName(process.argv) || 'world';
  console.log(hello(name));
}

main();
