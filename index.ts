// Minimal Node globals for compilation without @types/node
declare const process: { argv: string[] };
declare const require: { main: unknown };
declare const module: unknown;
// Greets the provided name with a "Hello" message.
// Defaults to "world" when no name is given.
export function hello(name: string = 'world'): string {
  return `Hello, ${name}!`;
}

export function main(argv: string[] = process.argv): void {
  const name = argv[2] || 'world';
  console.log(hello(name));
}

if (require.main === module) {
  main(process.argv);
}
